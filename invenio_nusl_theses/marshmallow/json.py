# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""
import arrow
from invenio_records_rest.schemas.fields.datetime import DateString
from marshmallow import fields, validates, ValidationError
# from __future__ import absolute_import, print_function
#
# from invenio_records_rest.schemas import Nested, StrictKeysMixin
# from invenio_records_rest.schemas.fields import SanitizedUnicode
# from invenio_records_rest.schemas.fields.datetime import DateString
# from marshmallow import fields, validate, ValidationError, pre_load, post_load
# from oarepo_invenio_model.marshmallow import InvenioRecordMetadataSchemaV1Mixin
# from pycountry import languages, countries
#
# from invenio_nusl_common.marshmallow.json import MultilanguageSchemaV1, ValueTypeSchemaV1, \
#     DoctypeSubSchemaV1, ApprovedTaxonomySchema
#
#
# ########################################################################
# #                 VALIDATION MODELS                                    #
# ########################################################################
# def validate_language(language):
#     language = language.lower()
#     alpha3 = languages.get(alpha_3=language)
#     bib = languages.get(bibliographic=language)
#     if alpha3 is None and bib is None:
#         raise ValidationError('The language code is not part of ISO-639 codes.')
#
#
# def validate_country(country):
#     country = country.upper()
#     alpha2 = countries.get(alpha_2=country)
#     if alpha2 is None:
#         raise ValidationError('The country code is not part of ISO-3166 codes.')
#
#
# #########################################################################
# #                      Sub-schemas                                      #
# #########################################################################
#
#
# class PSHSchema:
#     modified = fields.DateTime()
#     uri = fields.Url()
#     altLabel = fields.List(Nested(MultilanguageSchemaV1))
#
#
# class CZMeshSchema:
#     relatedURI = fields.List(Nested(ValueTypeSchemaV1()))
#     DateCreated = fields.Date()
#     DateRevised = fields.Date()
#     DateEstablished = fields.Date()
#     TreeNumberList = fields.List(SanitizedUnicode())
#
#
# class MedvikSchema:
#     relatedURI = fields.List(Nested(ValueTypeSchemaV1()))
#
#
# class SubjectMetadataSchemaV1(ApprovedTaxonomySchema, PSHSchema, MedvikSchema, CZMeshSchema,
#                               StrictKeysMixin):
#     pass
#
#
# class RightsMetadataSchemaV1(ApprovedTaxonomySchema):
#     icon = fields.Url()
#     related = fields.List(Nested(ValueTypeSchemaV1()))
#
#
# class ContributorTaxonomySchema(ApprovedTaxonomySchema):
#     dataCiteCode = SanitizedUnicode()
#     marcCode = SanitizedUnicode()
#
#
# class ContributorSubSchemaV1(StrictKeysMixin):
#     name = SanitizedUnicode(required=True)
#     id = Nested(ValueTypeSchemaV1())
#     role = Nested(ContributorTaxonomySchema(), required=True)
#
#
# class FieldSubSchemaV1(ApprovedTaxonomySchema):
#     pass
#
#
# class LanguageSubSchemaV1(ApprovedTaxonomySchema):
#     pass
#
#
# class AccessRightsSubSchema(ApprovedTaxonomySchema):
#     relatedURI = fields.List(Nested(ValueTypeSchemaV1()))
#
#
# class InstitutionsSubClass(ApprovedTaxonomySchema):
#     relatedID = fields.List(Nested(ValueTypeSchemaV1()))
#     aliases = fields.List(SanitizedUnicode())
#     ico = SanitizedUnicode()
#     url = fields.Url()
#     provider = fields.Boolean(missing=False)
#     formerNames = fields.List(SanitizedUnicode())
#
#
# #########################################################################
# #                     Main schema                                       #
# #########################################################################
# class ThesisMetadataSchemaV1(InvenioRecordMetadataSchemaV1Mixin, StrictKeysMixin):  # modifikace
#     """Schema for the record metadata."""
#
#     language = fields.List(Nested(LanguageSubSchemaV1), required=True,
#                            validate=validate.Length(min=1))
#     identifier = fields.List(Nested(ValueTypeSchemaV1()),
#                              required=True)  # TODO: Dodělat validaci na type
#     dateAccepted = DateString(required=True)  # fields.Date(required=True)
#     title = fields.List(Nested(MultilanguageSchemaV1()), required=True)
#     extent = SanitizedUnicode()
#     abstract = fields.List(Nested(MultilanguageSchemaV1()))
#     rights = fields.List(Nested(RightsMetadataSchemaV1))
#     subject = fields.List(Nested(SubjectMetadataSchemaV1))
#     keywords = fields.List(Nested(MultilanguageSchemaV1()))
#     creator = fields.List(Nested(CreatorSubSchemaV1), required=True)
#     contributor = fields.List(Nested(ContributorSubSchemaV1))
#     doctype = Nested((DoctypeSubSchemaV1()), required=True)
#     subtitle = fields.List(Nested(MultilanguageSchemaV1()))
#     note = fields.List(SanitizedUnicode())
#     accessibility = fields.List(Nested(MultilanguageSchemaV1()))
#     accessRights = Nested(AccessRightsSubSchema())
#     provider = Nested(InstitutionsSubClass())
#     defended = fields.Boolean()
#     studyField = fields.List(Nested(FieldSubSchemaV1))
#     degreeGrantor = fields.List(Nested(InstitutionsSubClass()), required=True)
#
#     @pre_load()
#     def id_to_str(self, data, **kwargs):
#         if "id" in data:
#             data["id"] = str(data.get("id"))
#         return data
#
#     @post_load()
#     def subject_or_keyword_required(self, data, **kwargs):
#         if self.context.get("draft"):
#             return data
#         if "keywords" not in data and "subject" not in data:
#             raise ValidationError("Keywords or subjects are required!",
#                                   field_names=["subject", "keywords"])
#         if len(data.get("keywords", [])) < 3 and len(data.get("subject", [])) < 3:
#             raise ValidationError("Number of keywords or subject have to be minimal three!",
#                                   field_names=["subject", "keywords"])
#         return data
from oarepo_taxonomies.marshmallow import TaxonomyField

from invenio_nusl_common.marshmallow.json import CommonMetadataSchemaV2
from invenio_nusl_common.marshmallow.subschemas import TitledMixin, InstitutionsMixin
from invenio_nusl_theses.marshmallow.subschemas import StudyFieldMixin


class ThesisMetadataSchemaV2(CommonMetadataSchemaV2):
    dateDefended = DateString(required=True)
    defended = fields.Boolean(required=True)
    degreeGrantor = TaxonomyField(mixins=[TitledMixin, InstitutionsMixin], required=True)
    studyField = TaxonomyField(name="studyField", mixins=[TitledMixin, StudyFieldMixin],
                               required=True)

    @validates("dateDefended")
    def validate_date_range(self, value):
        date = arrow.get(value)
        min = arrow.get("1700-01-01")
        current_date = arrow.get()
        if date > current_date:
            raise ValidationError("Date cannot be in the future")
        if date < min:
            raise ValidationError("Records older than from 1700 is not supported")
