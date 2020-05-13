from flask import current_app
from invenio_jsonschemas import current_jsonschemas

from invenio_records_draft.record import DraftEnabledRecordMixin, MarshmallowValidator
from invenio_records.api import Record
from werkzeug.utils import cached_property


class PublishedThesisRecord(DraftEnabledRecordMixin, Record):
    def validate(self, **kwargs):
        self['$schema'] = current_jsonschemas.path_to_url(
            'invenio_nusl_theses/nusl-theses-v1.0.0.json')
        return super().validate(**kwargs)

    @cached_property
    def server_name(self):
        return current_app.config.get('SERVER_NAME')

    @property
    def canonical_url(self):
        SERVER_NAME = self.server_name
        url = f"https://{SERVER_NAME}/api/theses/{self.id}"
        return url


class DraftThesisRecord(DraftEnabledRecordMixin, Record):
    draft_validator = MarshmallowValidator(
        'invenio_nusl_theses.marshmallow:ThesisMetadataSchemaV1',
        # marshmallow of the published version
        'invenio_nusl_theses/nusl-theses-v1.0.0.json'  # json schema of the published version
    )

    def validate(self, **kwargs):
        self['$schema'] = current_jsonschemas.path_to_url(
            'draft/invenio_nusl_theses/nusl-theses-v1.0.0.json')
        return super().validate(**kwargs)

    @cached_property
    def server_name(self):
        return current_app.config.get('SERVER_NAME')

    @property
    def canonical_url(self):
        SERVER_NAME = self.server_name
        url = f"https://{SERVER_NAME}/api/drafts/theses/{self['id']}"
        return url
