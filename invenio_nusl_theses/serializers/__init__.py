from __future__ import absolute_import, print_function

from invenio_records_rest.serializers.json import JSONSerializer
from invenio_records_rest.serializers.response import record_responsify, \
    search_responsify

from ..marshmallow import ThesisRecordSchemaV1


class ThesisSerializer(JSONSerializer):
    pass


thesis_json_v1 = ThesisSerializer(ThesisRecordSchemaV1, replace_refs=True)
thesis_json_v1_response = record_responsify(thesis_json_v1, 'application/json')
thesis_json_v1_search = search_responsify(thesis_json_v1, 'application/json')

__all__ = (
    'thesis_json_v1',
    'thesis_json_v1_response',
    'thesis_json_v1_search',
)
