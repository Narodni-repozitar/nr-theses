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
from marshmallow import fields, missing, validate
from invenio_nusl_common.marshmallow import MultilanguageSchemaV1, ValueTypeSchemaV1, Organization


#########################################################################
class CCSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode()  # TODO kontrolovaný slovník
    version = SanitizedUnicode()
    country = SanitizedUnicode  # TODO dvojmístný kód státu ISO 3166-1 alpha-2


class CopyrightShemaV1(StrictKeysMixin):
    pass


class Pracovni(StrictKeysMixin):
    language = fields.List(SanitizedUnicode())  # TODO: trojpísmenný kód
    identifier = Nested(ValueTypeSchemaV1)  # TODO: import
    dateAccepted = fields.Date()
    modified = fields.DateTime()
    title = Nested(MultilanguageSchemaV1, many=True)  # TODO: import, many=True
    extent = SanitizedUnicode()
    abstract = fields.List(Nested(MultilanguageSchemaV1))  # TODO: import


################################################################################

class PersonIdsSchemaV1(StrictKeysMixin):
    """Ids schema."""

    source = SanitizedUnicode()
    value = SanitizedUnicode()


class ContributorSchemaV1(StrictKeysMixin):
    """Contributor schema."""

    ids = fields.Nested(PersonIdsSchemaV1, many=True)
    name = SanitizedUnicode(required=True)
    role = SanitizedUnicode()
    affiliations = fields.List(SanitizedUnicode())
    email = fields.Email()


class ThesisMetadataSchemaV1(StrictKeysMixin):  # modifikace
    """Schema for the record metadata."""

    id = PersistentIdentifier()
    title = SanitizedUnicode(required=True, validate=validate.Length(min=3))
    keywords = fields.List(SanitizedUnicode(), many=True)
    publication_date = DateString()
    contributors = Nested(ContributorSchemaV1, many=True, required=True)


class ThesisRecordSchemaV1(StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
