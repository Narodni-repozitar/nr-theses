# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CIS UCT Prague.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_records_rest.utils import deny_all, check_elasticsearch, allow_all
from invenio_search import RecordsSearch

from invenio_nusl_theses.api import ThesisSearch
from invenio_nusl_theses.marshmallow import ThesisRecordSchemaV1, ThesisMetadataSchemaV1
from invenio_nusl_theses.record import PublishedThesisRecord, DraftThesisRecord

THESES_SEARCH_INDEX = 'invenio_nusl_theses-nusl-theses-v1.0.0'
THESES_STAGING_SEARCH_INDEX = 'invenio_nusl_theses-nusl-theses-staging-v1.0.0'
THESES_PID = 'pid(nusl,record_class="invenio_nusl_theses.api:ThesisRecord")'
THESES_STAGING_JSON_SCHEMA = "https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-staging-v1.0.0.json"

DRAFT_ENABLED_RECORDS_REST_ENDPOINTS = {
    'theses': {
        'json_schemas': [
            'invenio_nusl_theses/nusl-theses-v1.0.0.json'
        ],
        'published_pid_type': 'nusl',
        'pid_minter': 'nusl',
        'pid_fetcher': 'nusl',
        'draft_pid_type': 'dnusl',
        'draft_allow_patch': True,

        'record_marshmallow': ThesisRecordSchemaV1,
        'metadata_marshmallow': ThesisMetadataSchemaV1,

        'draft_record_class': DraftThesisRecord,
        'published_record_class': PublishedThesisRecord,

        'publish_permission_factory': allow_all,
        'unpublish_permission_factory': allow_all,
        'edit_permission_factory': allow_all,

        # 'search_class': DebugACLRecordsSearch,
        # 'indexer_class': CommitingRecordIndexer,

    }
}

INVENIO_RECORD_DRAFT_SCHEMAS = [
    'invenio_nusl_theses/nusl-theses-v1.0.0.json',
]

RECORDS_REST_FACETS = {
}

RECORDS_REST_SORT_OPTIONS = {
}

RECORDS_REST_DEFAULT_SORT = {
}
