# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CIS UCT Prague.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Flask extension for CIS theses repository."""

from __future__ import absolute_import, print_function

import re

from flask import Blueprint
from invenio_explicit_acls.utils import convert_relative_schema_to_absolute
import jsonschema
from marshmallow import ValidationError

from invenio_nusl_theses.api import ThesisAPI, ThesisRecord
from invenio_nusl_theses.marshmallow import ThesisMetadataSchemaV1
from invenio_nusl_theses.proxies import nusl_theses
from . import config

import logging

log = logging.getLogger('nusl-theses')


class InvenioNUSLTheses(object):
    """CIS theses repository extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        from invenio_records.signals import before_record_update, before_record_insert
        self.init_config(app)
        app.extensions['invenio-nusl-theses'] = ThesisAPI(app)
        before_record_update.connect(validate_thesis)
        before_record_insert.connect(validate_thesis)

    def init_config(self, app):
        """Initialize configuration.

        Override configuration variables with the values in this package.
        """

        app.config.setdefault('RECORDS_REST_ENDPOINTS', {}).update(getattr(config, 'RECORDS_REST_ENDPOINTS'))

        app.config.setdefault('RECORDS_REST_FACETS', {}).update(config.RECORDS_REST_FACETS)

        app.config.setdefault('RECORDS_REST_SORT_OPTIONS', {}).update(config.RECORDS_REST_SORT_OPTIONS)

        app.config.setdefault('RECORDS_REST_DEFAULT_SORT', {}).update(config.RECORDS_REST_DEFAULT_SORT)


def validate_thesis(*args, record=None, **kwargs):
    if not isinstance(record, ThesisRecord):
        return
    schema = record._convert_and_get_schema(record)
    if schema != convert_relative_schema_to_absolute(ThesisRecord.STAGING_SCHEMA):
        return
    marshmallow_schema = ThesisMetadataSchemaV1(strict=True)
    try:
        nusl_theses.validate(marshmallow_schema, record,
                             "https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-v1.0.0.json")
        record["validations"] = {
            "valid": True
        }

    except ValidationError as e:
        record["validations"] = {
            "valid": False,
            "extra": {
                "reason": "ValidationError",
                "message": str(e)
            }
        }

    except ValueError as e:
        record["validations"] = {
            "valid": False,
            "extra": {
                "reason": "ValueError",
                "message": str(e)
            }
        }

    # TODO: odchytnout tady dalsi exceptions ktere mohou vylitnout (json schema?) a vytvorit k nim spravne validations
    except jsonschema.ValidationError as e:
        record["validations"] = {
            "valid": False,
            "extra": {
                "reason": "JSON-schema validation",
                "message": re.sub(r'[\W_]+', ' ', e.message).strip()
            }
        }

    except Exception as e:
        log.exception('Unhandled exception in import. Please add exception handler for %s', type(e))
        record["validations"] = {
            "valid": False,
            "extra": {
                "reason": "Unhandled exception in validation",
                "message": str(e)
            }
        }
