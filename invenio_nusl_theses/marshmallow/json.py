# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

import csv
import os

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, validate, ValidationError, pre_load, post_load
from pycountry import languages, countries

from invenio_nusl_common.marshmallow import MultilanguageSchemaV1, ValueTypeSchemaV1, NUSLDoctypeSchemaV1, \
    OrganizationSchemaV1, RIVDoctypeSchemaV1


########################################################################
#                 IMPORT VALIDATION DATA                               #
########################################################################
def import_csv(file: str, start: int, end: int):
    path = os.path.dirname(__file__)
    path += f"/data/{file}"
    file = open(path, "r")
    reader = csv.reader(file)
    columns = []
    for col in range(start, end):
        columns.append([])
    for r in reader:
        i = 0
        for col in range(start, end):
            columns[i].append(r[col])
            i += 1
    file.close()
    return columns


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


def validate_programme_code(code):
    if code not in import_csv("programme.csv", 0, 2)[0]:
        raise ValidationError('The study programme code is not valid')


def validate_field_code(code):
    if code not in import_csv("field.csv", 0, 2)[0]:
        raise ValidationError('The study field code is not valid')


def validate_programme_name(name):
    if name not in import_csv("programme.csv", 0, 2)[1]:
        raise ValidationError('The study programme name is not valid')


def validate_field_name(name):
    if name not in import_csv("field.csv", 0, 2)[1]:
        raise ValidationError('The study field name is not valid')


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
    code = SanitizedUnicode(validate=validate_programme_code)
    name = SanitizedUnicode(validate=validate_programme_name)

    @post_load()
    def validate_code_name_fit(self, data):  # TODO: Dát do jednoho společného kódu
        if data["code"] and data["name"]:
            codes_names = import_csv("programme.csv", 0, 2)
            programme_code = data["code"]
            programme_name = data["name"]
            code_index = codes_names[0].index(programme_code)
            if codes_names[1][code_index] != programme_name:
                raise ValidationError("The code does not match the program name.")


class FieldSubSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(validate=validate_field_code)
    name = SanitizedUnicode(validate=validate_field_name)

    @post_load()
    def validate_code_name_fit(self, data):  # TODO: Dát do jednoho společného kódu
        if data["code"] and data["name"]:
            codes_names = import_csv("field.csv", 0, 2)
            programme_code = data["code"]
            programme_name = data["name"]
            code_index = codes_names[0].index(programme_code)
            if codes_names[1][code_index] != programme_name:
                raise ValidationError("The code does not match the field name.")


class DegreeGrantorSubSchemaV1(StrictKeysMixin):
    university = fields.List(Nested(MultilanguageSchemaV1, required=True), required=True,
                             validate=validate.Length(min=1))
    faculty = fields.List(Nested(MultilanguageSchemaV1))
    department = fields.List(Nested(MultilanguageSchemaV1))

    @post_load()
    def validate_university_name(self, data):
        if data.get("university"):
            for item in data["university"]:
                if item["lang"] == "cze":
                    imported_data = import_csv("universities.csv", 0, 1)
                    if item["name"] not in imported_data[0]:
                        raise ValidationError("The University name is not valid")

    @post_load()
    def validate_faculty_name(self, data):
        if data.get("faculty"):
            for item in data["faculty"]:
                if item["lang"] == "cze":
                    imported_data = import_csv("faculties.csv", 0, 1)
                    if item["name"] not in imported_data[0]:
                        raise ValidationError("The Faculty name is not valid")


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
    studyProgramme = Nested(ProgrammeSubSchemaV1, required=True)
    studyField = Nested(FieldSubSchemaV1)
    degreeGrantor = fields.List(Nested(DegreeGrantorSubSchemaV1), required=True, validate=validate.Length(min=1))


class ThesisRecordSchemaV1(StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
