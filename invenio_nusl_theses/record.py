from invenio_jsonschemas import current_jsonschemas

from invenio_records_draft.record import DraftEnabledRecordMixin, MarshmallowValidator
from invenio_records.api import Record


class PublishedRecord(DraftEnabledRecordMixin, Record):
    def validate(self, **kwargs):
        self['$schema'] = current_jsonschemas.path_to_url('invenio_nusl_theses/nusl-theses-v1.0.0.json')
        return super().validate(**kwargs)


class DraftRecord(DraftEnabledRecordMixin, Record):

    draft_validator = MarshmallowValidator(
        'invenio_nusl_theses.marshmallow:ThesisMetadataSchemaV1',  # marshmallow of the published version
        'invenio_nusl_theses/nusl-theses-v1.0.0.json'  # json schema of the published version
    )

    def validate(self, **kwargs):
        self['$schema'] = current_jsonschemas.path_to_url('draft/nusl-theses-v1.0.0.json')
        return super().validate(**kwargs)
