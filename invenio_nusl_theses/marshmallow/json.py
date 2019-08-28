# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, validate, ValidationError, pre_load, post_load
from pycountry import languages, countries

from flask_taxonomies.marshmallow import TaxonomySchemaV1
from invenio_nusl_common.marshmallow.json import MultilanguageSchemaV1, ValueTypeSchemaV1, DoctypeSubSchemaV1
from invenio_records_draft.marshmallow import DraftEnabledSchema


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
    copyright = fields.List(Nested(MultilanguageSchemaV1()))


class SubjectMetadataSchemaV1(TaxonomySchemaV1, StrictKeysMixin):
    url = fields.Url()


class CreatorSubSchemaV1(DraftEnabledSchema, StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1())


class ContributorSubSchemaV1(DraftEnabledSchema):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1())
    role = SanitizedUnicode(required=True)


class DegreeGrantorSubSchemaV1(TaxonomySchemaV1):
    ICO = SanitizedUnicode(required=False, dump_to='IČO', load_from='IČO', attribute="IČO")
    RID = SanitizedUnicode(required=False)
    address = SanitizedUnicode(required=False)
    data_box = SanitizedUnicode(required=False)
    deputy = SanitizedUnicode(required=False)
    form = SanitizedUnicode(required=False)
    region = SanitizedUnicode(required=False)
    term_of_office_from = SanitizedUnicode(required=False)
    term_of_office_until = SanitizedUnicode(required=False)
    type = SanitizedUnicode()
    url = fields.Url()


class FieldGrantorSubschemaV1(DraftEnabledSchema, StrictKeysMixin):
    faculty = SanitizedUnicode(required=False)
    university = SanitizedUnicode(required=False)


class FieldSubSchemaV1(TaxonomySchemaV1):
    aliases = fields.List(SanitizedUnicode(), allow_none=True)
    degree_level = SanitizedUnicode(required=False)
    form_of_study = SanitizedUnicode(required=False)
    grantor = fields.List(Nested(FieldGrantorSubschemaV1()))
    date_of_accreditation_validity = SanitizedUnicode()
    duration = SanitizedUnicode()
    reference_number = SanitizedUnicode()
    type = SanitizedUnicode()


class ProviderSubSchemaV1(TaxonomySchemaV1):
    name = fields.List(Nested(MultilanguageSchemaV1()))
    address = SanitizedUnicode()
    url = fields.Url()
    lib_url = fields.Url()


#########################################################################
#                     Main schema                                       #
#########################################################################
class ThesisMetadataSchemaV1(DraftEnabledSchema, StrictKeysMixin):  # modifikace
    """Schema for the record metadata."""

    schema = fields.String(attribute='$schema', load_from='$schema', dump_to='$schema', required=False)
    id = SanitizedUnicode(required=True)
    language = fields.List(SanitizedUnicode(required=True,
                                            validate=validate_language), required=True)
    identifier = fields.List(Nested(ValueTypeSchemaV1()), required=True)  # TODO: Dodělat validaci na type
    dateAccepted = fields.String() #fields.Date(required=True)
    modified = fields.String() #fields.DateTime(format="%Y-%m-%dT%H:%M:%S")
    title = fields.List(Nested(MultilanguageSchemaV1()), required=True)
    extent = SanitizedUnicode()
    abstract = fields.List(Nested(MultilanguageSchemaV1()))
    rights = fields.Nested(RightsMetadataSchemaV1)
    subject = fields.List(Nested(SubjectMetadataSchemaV1))
    keywords = fields.List(Nested(MultilanguageSchemaV1()))
    creator = fields.List(Nested(CreatorSubSchemaV1), required=True)
    contributor = fields.List(Nested(ContributorSubSchemaV1))
    doctype = Nested((DoctypeSubSchemaV1()), required=True)
    subtitle = fields.List(Nested(MultilanguageSchemaV1()))
    note = fields.List(SanitizedUnicode())
    accessibility = fields.List(Nested(MultilanguageSchemaV1()))
    accessRights = SanitizedUnicode(validate=validate.OneOf(["open", "embargoed", "restricted", "metadata_only"]))
    provider = Nested(ProviderSubSchemaV1)
    defended = fields.Boolean()
    studyField = fields.List(Nested(FieldSubSchemaV1))
    degreeGrantor = fields.List(Nested(DegreeGrantorSubSchemaV1), required=True)

    @pre_load()
    def id_to_str(self, data):
        if "id" in data:
            data["id"] = str(data.get("id"))

    @post_load()
    def subject_or_keyword_required(self, data):
        if "keywords" not in data and "subject" not in data:
            raise ValidationError("Keywords or subjects are required!")
        if len(data.get("keywords", [])) < 3 and len(data.get("subject", [])) < 3:
            raise ValidationError("Number of keywords or subject have to be minimal three!")

class ThesisRecordSchemaV1(DraftEnabledSchema, StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1())
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
