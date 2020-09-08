from flask import current_app

from invenio_records.api import Record
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin
from werkzeug.utils import cached_property


class PublishedThesisRecord(SchemaKeepingRecordMixin,
                            MarshmallowValidatedRecordMixin,
                            ReferenceEnabledRecordMixin,
                            Record):
    ALLOWED_SCHEMAS = OBJECT_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = OBJECT_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = RestorationObjectMetadataSchemaV1

    @cached_property
    def server_name(self):
        return current_app.config.get('SERVER_NAME')

    @property
    def canonical_url(self):
        SERVER_NAME = self.server_name
        url = f"https://{SERVER_NAME}/api/theses/{self.id}"
        return url
