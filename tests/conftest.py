# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

import os
import shutil
import tempfile

import pytest
from flask import Flask
from flask_taxonomies import FlaskTaxonomies
from flask_taxonomies.views import blueprint as taxonomies_blueprint
from invenio_app.factory import create_api
from invenio_db import InvenioDB
from invenio_db import db as db_
from invenio_search import InvenioSearch, current_search_client
from sqlalchemy_utils import create_database, database_exists
from invenio_jsonschemas.ext import InvenioJSONSchemas
from invenio_records.ext import InvenioRecords

# @pytest.yield_fixture()
# def app():
#     instance_path = tempfile.mkdtemp()
#     app = Flask('testapp', instance_path=instance_path)
#
#     app.config.update(
#         JSONSCHEMAS_HOST="nusl.cz",
#         SQLALCHEMY_TRACK_MODIFICATIONS=True,
#         SQLALCHEMY_DATABASE_URI=os.environ.get(
#             'SQLALCHEMY_DATABASE_URI',
#             'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="oarepo", pw="oarepo",
#             url="127.0.0.1",
#                                                                   db="oarepo")),
#         SERVER_NAME='localhost',
#     )
#     InvenioJSONSchemas(app)
#     InvenioRecords(app)
#     InvenioDB(app)
#     FlaskTaxonomies(app)
#     with app.app_context():
#         yield app
#
#     shutil.rmtree(instance_path)
from flask_taxonomies_es import FlaskTaxonomiesES

from invenio_nusl_theses import InvenioNUSLTheses


@pytest.yield_fixture()
def app():
    instance_path = tempfile.mkdtemp()
    _app = Flask('testapp', instance_path=instance_path)

    _app.config.update(
        JSONSCHEMAS_HOST="nusl.cz",
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        TAXONOMY_ELASTICSEARCH_INDEX="test_taxonomies_es",
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="oarepo", pw="oarepo",
                                                                  url="127.0.0.1",
                                                                  db="oarepo")),
        SERVER_NAME='localhost',
    )
    InvenioDB(_app)
    InvenioJSONSchemas(_app)
    InvenioRecords(_app)
    InvenioSearch(_app)
    FlaskTaxonomies(_app)
    FlaskTaxonomiesES(_app)
    InvenioNUSLTheses(_app)
    with _app.app_context():
        _app.register_blueprint(taxonomies_blueprint)
        yield _app

    shutil.rmtree(instance_path)
    with _app.app_context():
        if current_search_client.indices.exists(_app.config["TAXONOMY_ELASTICSEARCH_INDEX"]):
            current_search_client.indices.delete(index=_app.config["TAXONOMY_ELASTICSEARCH_INDEX"])


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api


@pytest.fixture
def thesis_metadata():
    return {
        '$schema': 'https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-v1.0.0.json',
        'language': [
            {'$ref': 'https://localhost/api/taxonomies/languages/cze'}
        ],
        "identifier": [
            {
                "value": "151515",
                "type": "nusl"
            }
        ],
        "dateAccepted": "2019-05-19",  # date(2019, 5, 19),
        "title": [
            {
                "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do "
                        "sklonku středověku.",
                "lang": "cze"
            },
            {
                "name": "Historical landscape of the Bohemian-Moravian Highlands. Settlement from "
                        "prehistoric to late medieval times",
                "lang": "eng"
            }
        ],
        "extent": "123s",
        "abstract": [
            {
                "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů "
                        "trestné činnosti zpět do společnosti. V rámci práce je na základě "
                        "odborné literatury a získaných informací cílem seznámit zájemce, "
                        "a to v teoretické části práce, s hlavními termíny a problematikou daného "
                        "tématu. V praktické části je popsán průběh sběru dat až po výsledky "
                        "kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti "
                        "sociální integrace pachatelů trestné činnosti zpět do společnosti je "
                        "objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět "
                        "do společnosti po propuštění z výkonu trestu odnětí svobody. Ve "
                        "vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu "
                        "odnětí svobody při jejich zpětné integraci do společnosti odpovídají "
                        "možnostem, které naše společnost poskytuje.",
                "lang": "cze"
            },
            {
                "name": "The bachelor thesis is focused on the possibility of integrating "
                        "criminals back into society. In the theoretical part are introduced the "
                        "main terms and issues to layman, thanks to the literature and acquired "
                        "information. In the practical part will be described the process of data "
                        "collection up to the results of the research. The main aim of the "
                        "bachelor thesis on 'Possibilities of social integration of criminals "
                        "back into society'is to clarify the integration of the perpetrator of "
                        "criminal activity back into society after release from imprisonment. In "
                        "a secondary goal will be found out whether the needs of released "
                        "prisoners, when they are reintegrated into society, correspond to the "
                        "possibilities provided by our society.",
                "lang": "eng"
            }
        ],
        "rights": [
            {
                "$ref": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/"
            }
        ],
        "subject": [
            {
                "$ref": "https://localhost/api/taxonomies/subjects/nlk20040148348"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/nlk20040147252"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/D002626"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/D002620"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/D004304"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/PSH11857"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subjects/PSH13081"
            }
        ],
        "creator": [
            {
                "name": "Kopecký, Daniel",
                "id": {
                    "value": "21454545",
                    "type": "ORCID"
                }
            },
            {
                "name": "Novák, Jiří",
                "id": {
                    "value": "21448754745",
                    "type": "ORCID"
                }
            }
        ],
        "contributor": [
            {
                "name": "Kopecký, Daniel",
                "id": {
                    "value": "21454545",
                    "type": "ORCID"
                },
                "role": {
                    "$ref": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/"
                }
            },
            {
                "name": "Novák, Jiří",
                "id": {
                    "value": "21448754745",
                    "type": "ORCID"
                },
                "role": {
                    "$ref": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/"
                }
            }
        ],
        "doctype": {
            "$ref": "http://127.0.0.1:5000/api/taxonomies/doctypes/analyzy/"
        },
        "id": "1276327",
        "subtitle": [
            {
                "name": "Alternativní název",
                "lang": "cze"
            }
        ],
        "note": [
            "Poznámka 1",
            "Poznámka 2"
        ],
        "accessibility": [
            {
                "name": "Dostupné kdesi blabla",
                "lang": "cze"
            },
            {
                "name": "Available at blabla",
                "lang": "eng"
            }
        ],
        "accessRights": {
            "$ref": "http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/",
        },
        "provider":
            {
                "$ref": "http://127.0.0.1:5000/api/taxonomies/institutions/60461373/",
            },
        "defended": True,
        "studyField": [
            {
                '$ref': "http://127.0.0.1:5000/api/taxonomies/studyfields/O_ucitelstvi"
                        "-praktickeho-vyucovani/"
            }
        ],
        "degreeGrantor": [
            {
                "$ref": "http://127.0.0.1:5000/api/taxonomies/institutions/60461373/fakulta"
                        "-chemicko-inzenyrska/ustav-chemickeho-inzenyrstvi/"
            }
        ]
    }


@pytest.yield_fixture()
def db(app):
    """Database fixture."""
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    yield db_
