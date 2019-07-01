# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CIS UCT Prague.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_records_rest.utils import deny_all, check_elasticsearch
from invenio_search import RecordsSearch

THESES_SEARCH_INDEX = 'invenio_nusl_theses-nusl-theses-v1.0.0'
THESES_PID = 'pid(thesis,record_class="invenio_nusl_theses.api:ThesisRecord")'

THESIS_REST_ENDPOINT = dict(
    pid_type='thesis',
    pid_minter='thesis',
    pid_fetcher='thesis',
    record_class='invenio_nusl_theses.api:ThesisRecord',
    default_endpoint_prefix=True,
    search_class=RecordsSearch,
    search_index=THESES_SEARCH_INDEX,
    search_type=None,
    record_serializers={
        'application/json': ('invenio_nusl_theses.serializers'
                             ':thesis_json_v1_response'),
    },
    search_serializers={
        'application/json': ('invenio_nusl_theses.serializers'
                             ':thesis_json_v1_search'),
    },
    # record_loaders={
    #     'application/json': ('cis_theses_repository.loaders'
    #                          ':json_v1'),
    # },
    # links_factory_imp=access_links_factory(),
    list_route='/record/',
    item_route='/record/<{0}:pid_value>'.format(THESES_PID),
    default_media_type='application/json',
    max_result_window=10000,
    create_permission_factory_imp=deny_all,
    read_permission_factory_imp=check_elasticsearch,
    update_permission_factory_imp=deny_all,
    delete_permission_factory_imp=deny_all,
)

RECORDS_REST_ENDPOINTS = {
    'theses': THESIS_REST_ENDPOINT,
}

RECORDS_REST_FACETS = {
}

RECORDS_REST_SORT_OPTIONS = {
}

RECORDS_REST_DEFAULT_SORT = {
}
