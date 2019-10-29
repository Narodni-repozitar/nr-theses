# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CIS UCT Prague.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from elasticsearch_dsl import Q
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all

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

INVENIO_OAREPO_UI_COLLECTIONS = {
    "theses": {
        "title": {
            "cs-cz": "Vysokoškolské práce",
            "en-us": "Theses"
        },
        "description": {
            "cs-cz": """

""",
            "en-us": """

"""
        },
        "rest": "/api/drafts/theses/",
        "facet_filters": list()
    },
}

INVENIO_RECORD_DRAFT_SCHEMAS = [
    'invenio_nusl_theses/nusl-theses-v1.0.0.json',
]


def degree_grantor_filter(field, path=None):
    def inner(values):
        return Q('nested',
                 path="degreeGrantor.ancestors",
                 query=Q("nested",
                         path="degreeGrantor.ancestors.title",
                         query=Q('terms',
                                 **{field: values}
                                 ))
                 )

    return inner


def nested_terms_filter(prefix, field, field_query=None):
    """Create a term filter.

    :param prefix
    :param field: Field name.
    :param field_query
    :returns: Function that returns the Terms query.
    """

    field = prefix + '.' + field

    def inner(values):
        if field_query:
            query = field_query(field)(values)
        else:
            query = Q('terms', **{field: values})
        return Q('nested', path=prefix, query=query)

    return inner


def year_filter(field):
    """Create a term filter.

    :param field: Field name.
    :returns: Function that returns the Terms query.
    """

    def inner(values):
        queries = []
        for value in values:
            queries.append(
                Q('range', **{
                    field: {
                        "gte": value,
                        "lt": int(value) + 1,
                        "format": "yyyy"
                    }
                })
            )
        return Q('bool', should=queries, minimum_should_match=1)

    return inner


def person_filter(field):
    """Create a term filter.

    :param field: Field name.
    :returns: Function that returns the Terms query.
    """

    def inner(values):
        queries = []
        for value in values:
            queries.append(
                Q('term', **{
                    field: value
                })
            )
        return Q('bool', should=queries, minimum_should_match=1)

    return inner


FILTERS = {
    'yearAccepted': year_filter('dateAccepted'),
    'language': terms_filter('language'),
    'defended': terms_filter('defended'),
    'person': person_filter('person.keyword'),
    'subjectKeywords': terms_filter('subjectKeywords'),
    'accessRights': terms_filter('accessRights'),
    'studyField': nested_terms_filter('studyField.title', 'value.keyword'),
    'university': degree_grantor_filter('degreeGrantor.ancestors.title.value.keyword'),
    'faculty': degree_grantor_filter('degreeGrantor.ancestors.title.value.keyword'),
    'valid': terms_filter("invenio_draft_validation.valid"),
    'marshmallow.field': terms_filter("invenio_draft_validation.errors.marshmallow.field"),
    'marshmallow.message': terms_filter("invenio_draft_validation.errors.marshmallow.message.keyword"),
    'jsonschema.field': terms_filter("invenio_draft_validation.errors.jsonschema.field"),
    'jsonschema.message': terms_filter("invenio_draft_validation.errors.jsonschema.message.keyword")
    # 'stylePeriod.title.value.keyword': terms_filter('stylePeriod.title.value.keyword'),
    # 'itemType.title.value.keyword': terms_filter('itemType.title.value.keyword'),
    # 'parts.material.materialType.title.value.keyword':
    #     nested_terms_filter('parts', 'material.materialType.title.value.keyword'),
    # 'parts.material.fabricationTechnology.title.value.keyword':
    #     nested_terms_filter('parts', 'material.fabricationTechnology.title.value.keyword'),
    # 'parts.material.color.title.value.keyword':
    #     nested_terms_filter('parts', 'material.color.title.value.keyword'),
    # 'parts.restorationMethods.title.value.keyword':
    #     nested_terms_filter('parts', 'restorationMethods.title.value.keyword'),
}

POST_FILTERS = {
    'doctype.slug': terms_filter('doctype.slug'),
}

RECORDS_REST_FACETS = {
    'draft-invenio_nusl_theses-nusl-theses-v1.0.0': {
        'aggs': {  # agregace
            'yearAccepted': {
                "date_histogram": {
                    "field": "dateAccepted",
                    "interval": "1y",
                    "format": "yyyy",
                    "min_doc_count": 1,
                    "order": {
                        "_key": "desc"
                    }

                }
            },
            'language': {
                'terms': {
                    'field': 'language'
                }
            },
            'defended': {
                'terms': {
                    'field': 'defended'
                }
            },
            'doctype.slug': {
                'terms': {
                    'field': 'doctype.slug'
                }
            },
            'person': {
                'terms': {
                    'field': 'person.keyword'
                }
            },
            'subjectKeywords': {
                'terms': {
                    'field': 'subjectKeywords',
                    'size': 100
                }
            },
            'accessRights': {
                'terms': {
                    'field': 'accessRights'
                }
            },
            "studyField": {
                "nested": {
                    "path": "studyField.title"
                },
                "aggs": {
                    "studyField": {
                        "terms": {
                            "field": "studyField.title.value.keyword",
                            "size": 100
                        }
                    }
                }
            },
            "degreeGrantor": {
                "nested": {
                    "path": "degreeGrantor.ancestors"
                },
                "aggs": {
                    "degreeGrantor": {
                        "filters": {
                            "filters": {
                                "faculty": {
                                    "term": {
                                        "degreeGrantor.ancestors.level": 2
                                    }
                                },
                                "university": {
                                    "term": {
                                        "degreeGrantor.ancestors.level": 1
                                    }
                                }
                            }
                        },
                        "aggs": {
                            "title": {
                                "nested": {
                                    "path": "degreeGrantor.ancestors.title"
                                },
                                "aggs": {
                                    "degreeGrantor": {
                                        "terms": {
                                            "field": "degreeGrantor.ancestors.title.value.keyword",
                                            "size": 100
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "valid": {
                'terms': {
                    'field': "invenio_draft_validation.valid"
                }
            },
            "marshmallow.field": {
                "terms": {
                    "field": "invenio_draft_validation.errors.marshmallow.field"
                }
            },
            "marshmallow.message": {
                "terms": {
                    "field": "invenio_draft_validation.errors.marshmallow.message.keyword"
                }
            },
            "jsonschema.field": {
                "terms": {
                    "field": "invenio_draft_validation.errors.jsonschema.field"
                }
            },
            "jsonschema.message": {
                "terms": {
                    "field": "invenio_draft_validation.errors.jsonschema.message.keyword"
                }
            }
            # 'degreeGrantor': {
            #     'nested': {
            #         'path': "degreeGrantor"
            #     },
            #     "aggs": {
            #         "degreeGrantor.title.value": {
            #             "terms": {
            #                 "field": "degreeGrantor.title.value"
            #             }
            #         }
            #     }
            # }

            # 'restorationRequestor.title.value.keyword': {
            #     'terms': {
            #       'field': 'restorationRequestor.title.value.keyword',
            #       'size': 100,
            #       "order": {"_term": "asc"}}},
            # 'stylePeriod.title.value.keyword': {
            #     'terms': {
            #       'field': 'stylePeriod.title.value.keyword',
            #       'size': 100,
            #       "order": {"_term": "desc"}}},
            # 'itemType.title.value.keyword': {
            #     'terms': {
            #       'field': 'itemType.title.value.keyword',
            #       'size': 100,
            #       "order": {"_term": "desc"}}},
            # 'parts': {  # if nested
            #     "nested": {
            #         "path": "parts"
            #     },
            #     "aggs": {
            #         "parts.materialType.title.value.keyword": {
            #             'terms': {
            #               'field': 'parts.materialType.title.value.keyword',
            #               'size': 100,
            #               "order": {"_term": "desc"}}
            #         },
            #         "parts.fabricationTechnology.title.value.keyword": {
            #             'terms':
            #               {
            #                   'field': 'parts.fabricationTechnology.title.value.keyword',
            #                   'size': 100,
            #                   "order": {"_term": "desc"}
            #               }
            #         },
            #         "parts.color.title.value.keyword": {
            #             'terms': {'field': 'parts.color.title.value.keyword', 'size': 100,
            #                       "order": {"_term": "desc"}}
            #         },
            #         "parts.restorationMethods.title.value.keyword": {
            #             'terms': {'field': 'parts.restorationMethods.title.value.keyword', 'size': 100,
            #                       "order": {"_term": "desc"}}
            #         }
            #     }
            # },
        },
        'filters': FILTERS,
        'post_filters': POST_FILTERS
    }
}

RECORDS_REST_SORT_OPTIONS = {
}

RECORDS_REST_DEFAULT_SORT = {
}
