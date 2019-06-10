# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, missing, validate, ValidationError, pre_load
from invenio_nusl_common.marshmallow import MultilanguageSchemaV1, ValueTypeSchemaV1, NUSLDoctypeSchemaV1, \
    OrganizationSchemaV1, RIVDoctypeSchemaV1
from pycountry import languages, countries
import csv
import os


########################################################################
#                 IMPORT VALIDATION DATA                               #
########################################################################
def import_fields_csv(file: str):
    path = os.path.dirname(__file__)
    path += f"/data/{file}"
    file = open(path, "r")
    reader = csv.reader(file)
    codes = []
    names = []
    for r in reader:
        code = r[0]
        name = r[1]
        codes.append(code)
        names.append(name)
    file.close()
    return codes, names


########################################################################
#                 VALIDATION MODELS                                    #
########################################################################
def validate_language(language):
    language = language.lower()
    alpha3 = languages.get(alpha_3=language)
    bib = languages.get(bibliographic=language)
    if alpha3 is None and bib is None:
        raise ValidationError('The language code is not part of ISO-639 codes.')


def validate_country(country):
    country = country.upper()
    alpha2 = countries.get(alpha_2=country)
    if alpha2 is None:
        raise ValidationError('The country code is not part of ISO-3166 codes.')


def validate_programme(code):
    if code not in import_fields_csv("programme.csv")[0]:
        raise ValidationError('The study programme code is not valid')


def validate_field(code):
    if code not in import_fields_csv("field.csv"):
        raise ValidationError('The study field code is not valid')


#########################################################################
#                      Sub-schemas                                      #
#########################################################################
class CCMetadataSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(required=True, validate=validate.OneOf(["CC BY",
                                                                    "CC BY-NC",
                                                                    "CC BY-SA",
                                                                    "CC BY-ND",
                                                                    "CC BY-NC-SA",
                                                                    "CC BY-NC-ND"]))
    version = SanitizedUnicode(required=True, validate=validate.Regexp(r"\d.\d"))
    country = SanitizedUnicode(required=True, validate=validate_country)

    @pre_load
    def country_code(self, data):
        if "country" in data:
            country = data["country"]
            if countries.get(alpha_3=country.upper()):
                country = countries.get(alpha_3=country.upper())
            elif countries.get(alpha_2=country.upper()):
                country = countries.get(alpha_2=country.upper())
            elif countries.get(name=country):
                country = countries.get(name=country)
            elif countries.get(official_name=country):
                country = countries.get(official_name=country)
            else:
                country = None
            if country is not None:
                data["country"] = country.alpha_2
        return data


class RightsMetadataSchemaV1(StrictKeysMixin):
    CC = fields.Nested(CCMetadataSchemaV1)
    copyright = fields.List(Nested(MultilanguageSchemaV1))


class SubjectMetadataSchemaV1(MultilanguageSchemaV1):
    taxonomy = SanitizedUnicode(validate=validate.OneOf(["czenas",
                                                         "mesh",
                                                         "czmesh",
                                                         "eurovoc",
                                                         "psh",
                                                         "ctt",
                                                         "pedag",
                                                         "agroterm",
                                                         "agrovoc",
                                                         "mednas",
                                                         "phffuk",
                                                         "ph",
                                                         "lcsh"]))
    id = fields.Url()

    @pre_load()
    def lower_taxonomy(self, data):
        if "taxonomy" in data:
            taxonomy = data["taxonomy"]
            data["taxonomy"] = taxonomy.lower()
            return data


class CreatorSubSchemaV1(StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1)


class ContributorSubSchemaV1(CreatorSubSchemaV1):
    role = SanitizedUnicode(required=True)


class DoctypeSubSchemaV1(StrictKeysMixin):
    NUSL = Nested(NUSLDoctypeSchemaV1, required=True)
    RIV = Nested(RIVDoctypeSchemaV1)


class ProgrammeSubSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(validate=validate_programme)
    name = SanitizedUnicode()

class FieldSubSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(validate=validate_field)
    name = SanitizedUnicode()


#########################################################################
#                     Main schema                                       #
#########################################################################
class ThesisMetadataSchemaV1(StrictKeysMixin):  # modifikace
    """Schema for the record metadata."""

    id = fields.Integer(required=True)
    language = fields.List(SanitizedUnicode(required=True,
                                            validate=validate_language))
    identifier = fields.List(Nested(ValueTypeSchemaV1), required=True)  # TODO: Dodělat validaci na type
    dateAccepted = fields.Date(required=True)
    modified = fields.DateTime()
    title = fields.List(Nested(MultilanguageSchemaV1), required=True)
    extent = SanitizedUnicode()
    abstract = fields.List(Nested(MultilanguageSchemaV1))
    rights = fields.Nested(RightsMetadataSchemaV1)
    subject = fields.List(Nested(SubjectMetadataSchemaV1))
    creator = fields.List(Nested(CreatorSubSchemaV1), required=True)
    contributor = fields.List(Nested(ContributorSubSchemaV1))
    doctype = Nested(DoctypeSubSchemaV1, required=True)
    subtitle = fields.List(Nested(MultilanguageSchemaV1))
    note = fields.List(SanitizedUnicode())
    accessibility = fields.List(Nested(MultilanguageSchemaV1))
    accessRights = SanitizedUnicode(validate=validate.OneOf(["open", "embargoed", "restricted", "metadata_only"]))
    provider = Nested(OrganizationSchemaV1)
    defended = fields.Boolean(SanitizedUnicode)
    studyProgramme = Nested(ProgrammeSubSchemaV1)


class ThesisRecordSchemaV1(StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
