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

from invenio_nusl_theses.api import ThesisAPI
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
        self.init_config(app)
        app.extensions['invenio-nusl-theses'] = ThesisAPI(app)


    def init_config(self, app):
        """Initialize configuration.

        Override configuration variables with the values in this package.
        """
        app.config.setdefault('INVENIO_RECORD_DRAFT_SCHEMAS', []).extend(config.INVENIO_RECORD_DRAFT_SCHEMAS)
        app.config.setdefault('DRAFT_ENABLED_RECORDS_REST_ENDPOINTS', {}).update(
            config.DRAFT_ENABLED_RECORDS_REST_ENDPOINTS)

        app.config.setdefault('RECORDS_REST_FACETS', {}).update(config.RECORDS_REST_FACETS)

        app.config.setdefault('RECORDS_REST_SORT_OPTIONS', {}).update(config.RECORDS_REST_SORT_OPTIONS)

        app.config.setdefault('RECORDS_REST_DEFAULT_SORT', {}).update(config.RECORDS_REST_DEFAULT_SORT)


