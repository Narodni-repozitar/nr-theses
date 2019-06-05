# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

import shutil
import tempfile
from datetime import date, datetime

import pytest
import pytz
from flask import Flask
from invenio_app.factory import create_api
from invenio_jsonschemas import InvenioJSONSchemas
from invenio_records import InvenioRecords


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api


@pytest.fixture
def thesis_metadata():
    return {
        "language": [
            "CZE"
        ],
        "identifier": [{
            "value": "151515",
            "type": "nusl"
        }],
        "dateAccepted": date(2019, 5, 19),
        "modified": datetime(2014, 12, 22, 3, 12, 58, 19077, tzinfo=pytz.utc),
        "title": [
            {
                "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
                "lang": "cze"
            },
            {
                "name": "Historical landscape of the Bohemian-Moravian Highlands. Settlement from prehistoric to late medieval times",
                "lang": "eng"
            }
        ]
    }


@pytest.yield_fixture()
def app():
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    app.config.update(
        JSONSCHEMAS_HOST="nusl.cz"
    )
    InvenioJSONSchemas(app)
    InvenioRecords(app)
    with app.app_context():
        yield app

    shutil.rmtree(instance_path)
