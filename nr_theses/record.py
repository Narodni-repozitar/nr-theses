from invenio_records.api import Record
from nr_common.record import CanonicalUrlMixin
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin

from .constants import THESES_ALLOWED_SCHEMAS, THESES_PREFERRED_SCHEMA
from .marshmallow import ThesisMetadataSchemaV2


class PublishedThesisRecord(SchemaKeepingRecordMixin,
                            MarshmallowValidatedRecordMixin,
                            ReferenceEnabledRecordMixin,
                            CanonicalUrlMixin,
                            Record):
    ALLOWED_SCHEMAS = THESES_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = THESES_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = ThesisMetadataSchemaV2

    @property
    def canonical_url(self):
        url = self.get_canonical_url('invenio_records_rest.theses_item',
                                     pid_value=self['control_number'], _external=True)
        return url
