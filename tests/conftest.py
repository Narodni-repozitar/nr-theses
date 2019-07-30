# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

from invenio_db import db as db_
import os
import shutil
import tempfile
from datetime import date, datetime

import pytest
import pytz
from flask import Flask
from invenio_app.factory import create_api
from invenio_db import InvenioDB
from invenio_jsonschemas import InvenioJSONSchemas
from invenio_records import InvenioRecords
from sqlalchemy_utils import create_database, database_exists

from flask_taxonomies import FlaskTaxonomies


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
        "dateAccepted": "2019-05-19",
        "modified": "2014-12-22T03:12:58.19077",
        "title": [
            {
                "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
                "lang": "cze"
            },
            {
                "name": "Historical landscape of the Bohemian-Moravian Highlands. Settlement from prehistoric to late medieval times",
                "lang": "eng"
            }
        ],
        "extent": "123s",
        "abstract": [
            {
                "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné činnosti zpět do společnosti. V rámci práce je na základě odborné literatury a získaných informací cílem seznámit zájemce, a to v teoretické části práce, s hlavními termíny a problematikou daného tématu. V praktické části je popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti sociální integrace pachatelů trestné činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti odpovídají možnostem, které naše společnost poskytuje.",
                "lang": "cze"
            },
            {
                "name": "The bachelor thesis is focused on the possibility of integrating criminals back into society. In the theoretical part are introduced the main terms and issues to layman, thanks to the literature and acquired information. In the practical part will be described the process of data collection up to the results of the research. The main aim of the bachelor thesis on 'Possibilities of social integration of criminals back into society'is to clarify the integration of the perpetrator of criminal activity back into society after release from imprisonment. In a secondary goal will be found out whether the needs of released prisoners, when they are reintegrated into society, correspond to the possibilities provided by our society.",
                "lang": "eng"
            }
        ],
        "rights": {
            "CC": {
                "code": "CC BY",
                "version": "3.0",
                "country": "CZ"
            },
            "copyright": [
                {
                    "name": "Dílo je chráněno podle autorského zákona č. 121/2000 Sb.",
                    "lang": "cze"
                }
            ]
        },
        "subject": [
            {
                "name": "koza",
                "lang": "cze"
            },
            {
                "name": "anorganická chemie",
                "lang": "cze",
                "taxonomy": "psh",
                "id": "http://psh.techlib.cz/skos/PSH5740"
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
                "role": "Referee"
            },
            {
                "name": "Novák, Jiří",
                "id": {
                    "value": "21448754745",
                    "type": "ORCID"
                },
                "role": "Referee"
            }
        ],
        "doctype": {
            "NUSL": {"term": "studie",
                     "bterm": "anl_met_mat"}
        },
        "id": 1276327,
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
        "accessRights": "open",
        "provider": {
            "id": {
                "value": "60461373",
                "type": "IČO"},
            "address": "Technická 1905/5, Dejvice, 160 00 Praha",
            "contactPoint": "info@vscht.cz",
            "name": {
                "name": "Vysoká škola chemicko-technologická",
                "lang": "cze"
            },
            "url": "https://www.vscht.cz/",
            "provider": True,
            "isPartOf": ["public_uni", "edu"]
        },
        "defended": True,
        "studyProgramme": {
            "code": "B1407",
            "name": "Chemie"
        },
        "studyField": {
            "code": "2801T015",
            "name": "Technologie organických látek a chemické speciality"
        },
        "degreeGrantor": [
            {
                "university": [
                    {
                        "name": "Vysoká škola chemicko-technologická v Praze",
                        "lang": "cze"
                    }
                ],
                "faculty": [
                    {
                        "name": "Fakulta chemické technologie",
                        "lang": "cze"
                    }
                ],
                "department": [
                    {
                        "name": "UOT",
                        "lang": "cze"
                    }
                ]
            }
        ]
    }


@pytest.yield_fixture()
def app():
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    app.config.update(
        JSONSCHEMAS_HOST="nusl.cz",
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="oarepo", pw="oarepo", url="127.0.0.1",
                                                                  db="oarepo")),
        SERVER_NAME='localhost',
    )
    InvenioJSONSchemas(app)
    InvenioRecords(app)
    InvenioDB(app)
    FlaskTaxonomies(app)
    with app.app_context():
        yield app

    shutil.rmtree(instance_path)


@pytest.yield_fixture()
def db(app):
    """Database fixture."""
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    # db_.create_all()
    yield db_
    # db_.session.remove()
    # db_.drop_all()
