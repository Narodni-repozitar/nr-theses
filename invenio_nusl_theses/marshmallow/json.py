# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function
from invenio_records_rest.schemas.fields.datetime import DateString

from urllib.parse import urlparse

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, validate, ValidationError, pre_load, post_load
from pycountry import languages, countries

from flask_taxonomies.marshmallow import TaxonomySchemaV1
from invenio_nusl_common.marshmallow.json import MultilanguageSchemaV1, ValueTypeSchemaV1, \
    DoctypeSubSchemaV1
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


class PSHSchema:
    modified = fields.DateTime()
    uri = fields.Url()
    altLabel = fields.List(Nested(MultilanguageSchemaV1))


class CZMeshSchema:
    relatedURI = fields.List(Nested(ValueTypeSchemaV1()))
    DateCreated = fields.Date()
    DateRevised = fields.Date()
    DateEstablished = fields.Date()
    TreeNumberList = fields.List(SanitizedUnicode())


class MedvikSchema:
    relatedURI = fields.List(Nested(ValueTypeSchemaV1()))


class SubjectMetadataSchemaV1(ApprovedTaxonomySchema, PSHSchema, MedvikSchema, CZMeshSchema,
                              StrictKeysMixin):
    pass


class RightsMetadataSchemaV1(ApprovedTaxonomySchema):
    icon = fields.Url()
    related = fields.List(Nested(ValueTypeSchemaV1()))


class CreatorSubSchemaV1(DraftEnabledSchema, StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1())


class ContributorSubSchemaV1(DraftEnabledSchema):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1())
    role = Nested(ContributorTaxonomySchema())


class DegreeGrantorSubSchemaV1(TaxonomySchemaV1):
    ICO = SanitizedUnicode(required=False, attribute='ICO', data_key='ICO')
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
    address = SanitizedUnicode()
    url = fields.Url()
    lib_url = fields.Url()


class LanguageSubSchemaV1(TaxonomySchemaV1):
    pass


#########################################################################
#                     Main schema                                       #
#########################################################################
class ThesisMetadataSchemaV1(DraftEnabledSchema, StrictKeysMixin):  # modifikace
    """Schema for the record metadata."""

    schema = fields.String(attribute='$schema', data_key='$schema', required=False)
    id = SanitizedUnicode(required=True)
    language = fields.List(Nested(LanguageSubSchemaV1), required=True,
                           validate=validate.Length(min=1))
    identifier = fields.List(Nested(ValueTypeSchemaV1()),
                             required=True)  # TODO: Dodělat validaci na type
    dateAccepted = DateString(required=True)  # fields.Date(required=True)
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
    accessRights = SanitizedUnicode(
        validate=validate.OneOf(["open", "embargoed", "restricted", "metadata_only"]))
    provider = Nested(ProviderSubSchemaV1)
    defended = fields.Boolean()
    studyField = fields.List(Nested(FieldSubSchemaV1))
    degreeGrantor = fields.List(Nested(DegreeGrantorSubSchemaV1), required=True)

    @pre_load()
    def id_to_str(self, data, **kwargs):
        if "id" in data:
            data["id"] = str(data.get("id"))
        return data

    @post_load()
    def subject_or_keyword_required(self, data, **kwargs):
        if self.context.get("draft"):
            return data
        if "keywords" not in data and "subject" not in data:
            raise ValidationError("Keywords or subjects are required!",
                                  field_names=["subject", "keywords"])
        if len(data.get("keywords", [])) < 3 and len(data.get("subject", [])) < 3:
            raise ValidationError("Number of keywords or subject have to be minimal three!",
                                  field_names=["subject", "keywords"])
        return data

    @post_load()
    def validate_study_field(self, data, **kwargs):
        if self.context.get("draft"):
            return data
        study_fields = data.get("studyField")
        if study_fields is not None:
            for field in study_fields:
                if "$ref" in field:
                    url = urlparse(field["$ref"])
                    path = url.path
                    path_components = path.split("/")
                    last = path_components[-1]
                    if "no_valid_" in last:
                        raise ValidationError(
                            f"Studyfield is not valid.",
                            field_names=["studyField"])
        return data


class ThesisRecordSchemaV1(DraftEnabledSchema, StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1())
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
