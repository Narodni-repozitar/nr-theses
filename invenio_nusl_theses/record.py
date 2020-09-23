from flask import url_for
from invenio_records.api import Record
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin

from .constants import THESES_ALLOWED_SCHEMAS, THESES_PREFERRED_SCHEMA
from .marshmallow import ThesisMetadataSchemaV2


class PublishedThesisRecord(SchemaKeepingRecordMixin,
                            MarshmallowValidatedRecordMixin,
                            ReferenceEnabledRecordMixin,
                            Record):
    ALLOWED_SCHEMAS = THESES_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = THESES_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = ThesisMetadataSchemaV2

    # @cached_property
    # def server_name(self):
    #     return current_app.config.get('SERVER_NAME')

    @property
    def canonical_url(self):
        return url_for('invenio_records_rest.theses_item',
                       pid_value=self['control_number'], _external=True)
        # SERVER_NAME = self.server_name
        # url = f"https://{SERVER_NAME}/api/theses/{self.id}"
        # return url
