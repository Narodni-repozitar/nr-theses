from pprint import pprint

import pytest
from marshmallow.exceptions import ValidationError

from invenio_nusl_theses.marshmallow.json import ThesisMetadataSchemaV1
from tests.utils import convert_dates


@pytest.fixture
def dump_metadata():
    return {
        '$schema': 'https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-v1.0.0.json',
        "language": [
            {'$ref': 'https://localhost/api/taxonomies/languages/cze'}
        ],
        "identifier": [{
            "value": "151515",
            "type": "nusl"
        }],
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
                "$ref": "https://localhost/api/taxonomies/subject/nlk20040148348"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/nlk20040147252"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/D002626"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/D002620"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/D004304"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph120179"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph114722"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph135174"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph116084"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph121510"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph114295"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/ph116680"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/PSH11857"
            },
            {
                "$ref": "https://localhost/api/taxonomies/subject/PSH13081"
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
            "links": {
                "self": "https://127.0.0.1:5000/api/taxonomies/doctype/vskp/diplomove_prace/",
                "tree": "https://127.0.0.1:5000/api/taxonomies/doctype/vskp/diplomove_prace"
                        "/?drilldown=True"
            },
            "title": [
                {
                    "lang": "cze",
                    "value": "Diplomové práce"
                }
            ],
            "path": "/vskp/diplomove_prace",
            "slug": "diplomove_prace"
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
                "name": "Avallable at blabla",
                "lang": "eng"
            }
        ],
        "accessRights": "open",
        "provider":
            {
                "$ref": "https://127.0.0.1:5000/api/taxonomies/provider/edu/public_uni/vscht/",
            },
        "defended": True,
        "studyField": [
            {
                "aliases": None,
                "date_of_accreditation_validity": "31.05.2016",
                "degree_level": "Bakalářský",
                "duration": "3",
                "form_of_study": "P",
                "grantor": [
                    {
                        "faculty": "Divadelní fakulta",
                        "university": "Akademie múzických umění v Praze"
                    }
                ],
                # "id": 64520,
                "links": {
                    "parent": "https://127.0.0.1:5000/api/taxonomies/studyfields/B8212/",
                    "parent_tree": "https://127.0.0.1:5000/api/taxonomies/studyfields/B8212"
                                   "/?drilldown=True",
                    "self": "https://127.0.0.1:5000/api/taxonomies/studyfields/B8212/8203R082/",
                    "tree": "https://127.0.0.1:5000/api/taxonomies/studyfields/B8212/8203R082"
                            "/?drilldown=True"
                },
                "path": "/B8212/8203R082",
                "reference_number": "11137/2010",
                "slug": "8203R082",
                "title": [
                    {
                        "lang": "cze",
                        "value": "Herectví alternativního divadla"
                    }
                ],
                "type": "obor"
            }
        ],
        "degreeGrantor": [
            {
                "ICO": "00216208",
                "RID": "11000",
                "address": "Ovocný trh 5  Staré Město  Praha 1, 116 36",
                "data_box": "piyj9b4",
                "deputy": "prof. MUDr. Tomáš Zima, DrSc., MBA",
                # "descendants_count": 1046.0,
                "form": "veřejná",
                # "id": 45248,
                "links": {
                    "parent": "https://127.0.0.1:5000/api/taxonomies/universities/",
                    "parent_tree": "https://127.0.0.1:5000/api/taxonomies/universities/?drilldown"
                                   "=True",
                    "self": "https://127.0.0.1:5000/api/taxonomies/universities/00216208/",
                    "tree": "https://127.0.0.1:5000/api/taxonomies/universities/00216208"
                            "/?drilldown=True"
                },
                "path": "/00216208",
                "region": "Praha",
                "slug": "00216208",
                "term_of_office_from": "2018-02-01",
                "term_of_office_until": "2022-01-31",
                "title": [
                    {
                        "lang": "cze",
                        "value": "Univerzita Karlova"
                    }
                ],
                "type": "univerzitní",
                "url": "https://www.cuni.cz"
            }
        ]
    }


########################################################################
#                           Language                                   #
########################################################################
def test_language_load_1(app, thesis_metadata):
    thesis_metadata["language"] = None

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


def test_language_load_2(app, thesis_metadata):
    thesis_metadata["language"] = []

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


# def test_language_load_3(app, thesis_metadata):
#     thesis_metadata["language"] = "CZE"
#
#     with pytest.raises(ValidationError):
#         schema = ThesisMetadataSchemaV1()
#         result = schema.load(convert_dates(thesis_metadata))


########################################################################
#                           Identifier                                 #
########################################################################
def test_identifier_dump_1(app, dump_metadata):
    dump_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_identifier_load_1(app, thesis_metadata):
    thesis_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]

    schema = ThesisMetadataSchemaV1()
    # assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data
    schema_load = schema.load(thesis_metadata)
    assert thesis_metadata == schema_load


def test_identifier_load_2(app, thesis_metadata):
    thesis_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    },
        {
            "value": "15dsfa515",
            "type": "nuslOAI"
        }
    ]

    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_identifier_load_3(app, thesis_metadata):
    del thesis_metadata["identifier"]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                           dateAccepted                               #
########################################################################
def test_dateaccepted_dump_1(app, dump_metadata):
    dump_metadata["dateAccepted"] = "2019-05-19"  # date(2019, 5, 19)
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_dateaccepted_dump_2(app, dump_metadata):
    del dump_metadata["dateAccepted"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_dateaccepted_dump_3(app, dump_metadata):
    dump_metadata["dateAccepted"] = "blbost"
    schema = ThesisMetadataSchemaV1()
    assert dump_metadata != schema.dump(dump_metadata)


def test_dateaccepted_load_1(app, thesis_metadata):
    thesis_metadata["dateAccepted"] = "2019-05-19"

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_dateaccepted_load_2(app, thesis_metadata):
    thesis_metadata["dateAccepted"] = "20190519"

    schema = ThesisMetadataSchemaV1()
    with pytest.raises(ValidationError):
        schema.load(convert_dates(thesis_metadata))


def test_dateaccepted_load_3(app, thesis_metadata):
    del thesis_metadata["dateAccepted"]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              title                                   #
########################################################################
def test_title_dump_1(app, dump_metadata):
    dump_metadata["title"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cze"
        }]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_title_dump_2(app, dump_metadata):
    dump_metadata["title"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cz"
        }]
    # with pytest.raises(ValidationError):
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_title_dump_3(app, dump_metadata):
    dump_metadata["title"] = "blbost"
    with pytest.raises(AssertionError):
        schema = ThesisMetadataSchemaV1()
        assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_title_dump_4(app, dump_metadata):
    del dump_metadata["title"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_title_load_1(app, thesis_metadata):
    thesis_metadata["title"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cze"
        }]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_title_load_2(app, thesis_metadata):
    thesis_metadata["title"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cz"
        }]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              extent                                  #
########################################################################
def test_extent_dump_1(app, dump_metadata):
    dump_metadata["extent"] = "123 s."
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_extent_dump_2(app, dump_metadata):
    del dump_metadata["extent"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_extent_dump_3(app, dump_metadata):
    dump_metadata["extent"] = 123
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_extent_load_1(app, thesis_metadata):
    thesis_metadata["extent"] = "123 s."
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_extent_load_2(app, thesis_metadata):
    del thesis_metadata["extent"]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_extent_load_3(app, thesis_metadata):
    thesis_metadata["extent"] = 123
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


def test_extent_load_4(app, thesis_metadata):
    thesis_metadata["extent"] = ["123 s."]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              abstract                                #
########################################################################
def test_abstract_dump_1(dump_metadata):
    dump_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné "
                    "činnosti zpět do společnosti. V rámci práce je na základě odborné literatury "
                    "a získaných informací cílem seznámit zájemce, a to v teoretické části práce, "
                    "s hlavními termíny a problematikou daného tématu. V praktické části je "
                    "popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem "
                    "bakalářské práce na téma Možnosti sociální integrace pachatelů trestné "
                    "činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace "
                    "pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu "
                    "odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z "
                    "výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti "
                    "odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_abstract_dump_2(dump_metadata):
    del dump_metadata["abstract"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_abstract_dump_3(dump_metadata):
    dump_metadata["abstract"] = 123  # jiný datový typ
    schema = ThesisMetadataSchemaV1()
    # TODO: Zkontrolovat TypeError, nemělo by být: TypeError: 'int' object is not iterable,
    #  zkontrolovat message
    with pytest.raises(TypeError):
        schema.dump(dump_metadata)


def test_abstract_load_1(app, thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné "
                    "činnosti zpět do společnosti. V rámci práce je na základě odborné literatury "
                    "a získaných informací cílem seznámit zájemce, a to v teoretické části práce, "
                    "s hlavními termíny a problematikou daného tématu. V praktické části je "
                    "popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem "
                    "bakalářské práce na téma Možnosti sociální integrace pachatelů trestné "
                    "činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace "
                    "pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu "
                    "odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z "
                    "výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti "
                    "odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_2(app, thesis_metadata):
    del thesis_metadata["abstract"]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_3(app, thesis_metadata):
    thesis_metadata["abstract"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_4(app, thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné "
                    "činnosti zpět do společnosti. V rámci práce je na základě odborné literatury "
                    "a získaných informací cílem seznámit zájemce, a to v teoretické části práce, "
                    "s hlavními termíny a problematikou daného tématu. V praktické části je "
                    "popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem "
                    "bakalářské práce na téma Možnosti sociální integrace pachatelů trestné "
                    "činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace "
                    "pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu "
                    "odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z "
                    "výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti "
                    "odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cs"
        }
    ]
    final_metadata = dict(thesis_metadata)
    final_metadata["abstract"][0]["lang"] = "cze"
    schema = ThesisMetadataSchemaV1()
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_5(app, thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné "
                    "činnosti zpět do společnosti. V rámci práce je na základě odborné literatury "
                    "a získaných informací cílem seznámit zájemce, a to v teoretické části práce, "
                    "s hlavními termíny a problematikou daného tématu. V praktické části je "
                    "popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem "
                    "bakalářské práce na téma Možnosti sociální integrace pachatelů trestné "
                    "činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace "
                    "pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu "
                    "odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z "
                    "výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti "
                    "odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "ces"
        }
    ]
    final_metadata = dict(thesis_metadata)
    final_metadata["abstract"][0]["lang"] = "cze"
    schema = ThesisMetadataSchemaV1()
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              rights                                  #
########################################################################
def test_rights_dump_1(dump_metadata):
    dump_metadata["rights"] = {
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
    }
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_rights_dump_2(dump_metadata):
    dump_metadata["rights"] = "blbost"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_rights_dump_3(dump_metadata):
    del dump_metadata["rights"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_rights_load_1(app, thesis_metadata):
    thesis_metadata["rights"] = {
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
    }
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_2(app, thesis_metadata):
    thesis_metadata["rights"] = {
        "CC": {
            "code": "CC BY",
            "version": "3.0",
            "country": "CZ"
        },
        "copyright": [
            {
                "name": "Dílo je chráněno podle autorského zákona č. 121/2000 Sb.",
                "lang": "ces"
            }
        ]
    }
    final_data = dict(thesis_metadata)
    final_data["rights"]["copyright"][0]["lang"] = "cze"
    schema = ThesisMetadataSchemaV1()
    assert final_data == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_3(app, thesis_metadata):
    thesis_metadata["rights"] = {
        "CC": {
            "code": "CC BY",
            "version": "3.0",
            "country": "CZ"
        },
        "copyright": []
    }
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_4(app, thesis_metadata):
    del thesis_metadata["rights"]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              subject                                 #
########################################################################
def test_keywords_dump_1(dump_metadata):
    dump_metadata["keywords"] = [
        {
            "name": "koza",
            "lang": "cze"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_keywords_dump_2(dump_metadata):
    dump_metadata["keywords"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_keywords_load_1(app, thesis_metadata):
    thesis_metadata["keywords"] = [
        {
            "name": "koza",
            "lang": "cze"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_keywords_load_2(app, thesis_metadata):
    thesis_metadata["keywords"] = [
        {
            "name": "koza",
        },
        {
            "name": "anorganická chemie",
            "lang": "cze"
        }
    ]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


def test_keywords_load_3(app, thesis_metadata):
    thesis_metadata["keywords"] = [
        {
            "name": "koza",
            "lang": "cze"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    schema.load(convert_dates(thesis_metadata))
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                             creator                                  #
########################################################################
def test_creator_dump_1(dump_metadata):
    dump_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            }
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_creator_dump_2(dump_metadata):
    dump_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_creator_dump_3(dump_metadata):
    dump_metadata["creator"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_creator_dump_4(dump_metadata):
    del dump_metadata["creator"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_creator_load_1(app, thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            }
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_creator_load_2(app, thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_creator_load_3(app, thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
            }
        }
    ]
    with pytest.raises(ValidationError):  # Chybí typ id
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


def test_creator_load_4(app, thesis_metadata):
    del thesis_metadata["creator"]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                             contributor                              #
########################################################################
def test_contributor_dump_1(dump_metadata):
    dump_metadata["contributor"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            },
            "role": "referee"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_contributor_dump_2(dump_metadata):
    dump_metadata["contributor"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_contributor_dump_3(dump_metadata):
    del dump_metadata["contributor"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_contributor_load_1(app, thesis_metadata):
    thesis_metadata["contributor"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            },
            "role": "referee"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_contributor_load_2(app, thesis_metadata):
    thesis_metadata["contributor"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            }
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


def test_contributor_load_3(app, thesis_metadata):
    thesis_metadata["contributor"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            },
            "role": ["array, špatný datový typ"]
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                             doctype                                  #
########################################################################
# def test_doctype_dump_1(dump_metadata):
#     dump_metadata["doctype"] = {
#         "taxonomy": "NUSL",
#         "value": [
#             "vskp", "bakalarske_prace"
#         ]
#     }
#     schema = ThesisMetadataSchemaV1()
#     assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)
#
#
# def test_doctype_dump_2(dump_metadata):
#     dump_metadata["doctype"] = {
#         "taxonomy": "NUSL",
#         "value": [
#             "studie", "anl_met_mat"
#         ]
#     }
#     schema = ThesisMetadataSchemaV1()
#     assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)
#
#
# def test_doctype_dump_3(dump_metadata):
#     del dump_metadata["doctype"]
#     schema = ThesisMetadataSchemaV1()
#     assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)
#
#
# def test_doctype_load_1(thesis_metadata):
#     thesis_metadata["doctype"] = {
#         "taxonomy": "NUSL",
#         "value": [
#             "vskp", "bakalarske_prace"
#         ]
#     }
#     schema = ThesisMetadataSchemaV1()
#     assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data
#
#
# def test_doctype_load_2(thesis_metadata):
#     thesis_metadata["doctype"] = {
#         "taxonomy": "RIV",
#         "value": [
#             "polop", "Z"
#         ]
#     }
#     with pytest.raises(ValidationError):
#         schema = ThesisMetadataSchemaV1()
#         schema.load(convert_dates(thesis_metadata)).data
#
#
# # def test_doctype_load_3(thesis_metadata):
# #     thesis_metadata["doctype"] = {
# #         "RIV": {"term": "polop",
# #                 "bterm": "Z"}
# #     }
# #     with pytest.raises(ValidationError):
# #         schema = ThesisMetadataSchemaV1()
# #         schema.load(convert_dates(thesis_metadata))
#
#
# def test_doctype_load_4(app, thesis_metadata):
#     thesis_metadata["doctype"] = {
#         "taxonomy": "NUSL",
#         "value": ["vskp", "studie"]
#     }
#     with pytest.raises(ValidationError):
#         schema = ThesisMetadataSchemaV1()
#         schema.load(convert_dates(thesis_metadata))
#
#
# def test_doctype_load_5(app, thesis_metadata):
#     thesis_metadata["doctype"] = {
#         "taxonomy": "NUSL",
#         "value": [None, "studie"]
#     }
#
#     with pytest.raises(ValidationError):
#         schema = ThesisMetadataSchemaV1()
#         schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                             id                                       #
########################################################################
def test_id_dump_1(dump_metadata):
    dump_metadata["id"] = "2562727272"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_id_dump_2(dump_metadata):
    del dump_metadata["id"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_id_dump_3(dump_metadata):
    dump_metadata["id"] = 2562727272
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != convert_dates(schema.dump(dump_metadata).data)


def test_id_load_1(app, thesis_metadata):
    thesis_metadata["id"] = "2562727272"
    schema = ThesisMetadataSchemaV1()
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_id_load_2(app, thesis_metadata):
    del thesis_metadata["id"]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_id_load_3(app, thesis_metadata):
    thesis_metadata["id"] = 2562727272
    schema = ThesisMetadataSchemaV1()
    final_metadata = dict(thesis_metadata)
    final_metadata["id"] = "2562727272"
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              subtitle                                #
########################################################################
def test_subtitle_dump_1(dump_metadata):
    dump_metadata["subtitle"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cze"
        }]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_subtitle_dump_2(dump_metadata):
    dump_metadata["subtitle"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cz"
        }]
    # with pytest.raises(ValidationError):
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_subtitle_dump_3(dump_metadata):
    dump_metadata["subtitle"] = "blbost"
    with pytest.raises(AssertionError):
        schema = ThesisMetadataSchemaV1()
        assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_subtitle_dump_4(dump_metadata):
    del dump_metadata["subtitle"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_subtitle_load_1(app, thesis_metadata):
    thesis_metadata["subtitle"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cze"
        }]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_subtitle_load_2(app, thesis_metadata):
    thesis_metadata["subtitle"] = [
        {
            "name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku "
                    "středověku.",
            "lang": "cz"
        }]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              note                                    #
########################################################################
def test_note_dump_1(dump_metadata):
    dump_metadata["note"] = [
        "Poznámka 1",
        "Poznámka 2"
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_note_dump_2(dump_metadata):
    del dump_metadata["note"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_note_dump_3(dump_metadata):
    dump_metadata["note"] = {
        "Poznámka 1",
        "Poznámka 2"
    }
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != schema.dump(dump_metadata).data


def test_note_load_1(app, thesis_metadata):
    thesis_metadata["note"] = [
        "Poznámka 1",
        "Poznámka 2"
    ]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_note_load_2(app, thesis_metadata):
    del thesis_metadata["note"]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_note_load_3(app, thesis_metadata):
    thesis_metadata["note"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           accessibility                              #
########################################################################
def test_accessibility_dump_1(dump_metadata):
    dump_metadata["accessibility"] = [
        {
            "name": "Dostupné kdesi blabla",
            "lang": "cz"
        },
        {
            "name": "Avallable at blabla",
            "lang": "en"
        }
    ]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_accessibility_dump_2(dump_metadata):
    del dump_metadata["accessibility"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_accessibility_dump_3(dump_metadata):
    dump_metadata["accessibility"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != schema.dump(dump_metadata).data


def test_accessibility_load_1(app, thesis_metadata):
    thesis_metadata["accessibility"] = [
        {
            "name": "Dostupné kdesi blabla",
            "lang": "cze"
        },
        {
            "name": "Avallable at blabla",
            "lang": "eng"
        }
    ]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_accessibility_load_2(app, thesis_metadata):
    thesis_metadata["accessibility"] = [
        {
            "name": "Dostupné kdesi blabla",
            "lang": "cz"
        },
        {
            "name": "Avallable at blabla",
            "lang": "en"
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessibility_load_3(app, thesis_metadata):
    del thesis_metadata["accessibility"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           accessRights                               #
########################################################################
def test_accessRights_dump_1(dump_metadata):
    dump_metadata["accessRights"] = "open"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_accessRights_dump_2(dump_metadata):
    del dump_metadata["accessRights"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_accessRights_dump_3(dump_metadata):
    dump_metadata["accessRights"] = ["Jiný datový typ"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != schema.dump(dump_metadata).data


def test_accessRights_load_1(app, thesis_metadata):
    thesis_metadata["accessRights"] = "open"

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_2(app, thesis_metadata):
    thesis_metadata["accessRights"] = "blbost"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_3(app, thesis_metadata):
    del thesis_metadata["accessRights"]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_4(app, thesis_metadata):
    thesis_metadata["accessRights"] = None
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           Provider                                   #
########################################################################
def test_provider_1(app, thesis_metadata):
    thesis_metadata["provider"] = None

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        schema.load(convert_dates(thesis_metadata))

# TODO: neměl by projít prázdný dict
def test_provider_2(app, thesis_metadata):
    thesis_metadata["provider"] = {}

    schema = ThesisMetadataSchemaV1()
    schema.load(convert_dates(thesis_metadata))
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)
    pprint(convert_dates(
        schema.load(convert_dates(thesis_metadata)).data))



########################################################################
#                           Defended                                   #
########################################################################
def test_defended_dump_1(dump_metadata):
    dump_metadata["defended"] = False
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == schema.dump(dump_metadata).data


def test_defended_dump_2(dump_metadata):
    dump_metadata["defended"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) != schema.dump(dump_metadata).data


# def test_defended_dump_3(thesis_metadata): #TODO: dořešit
#     del thesis_metadata["defended"]
#     schema = ThesisMetadataSchemaV1()
#     assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_defended_load_1(app, thesis_metadata):
    thesis_metadata["defended"] = False

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_defended_load_2(app, thesis_metadata):
    del thesis_metadata["defended"]

    schema = ThesisMetadataSchemaV1()
    assert convert_dates(thesis_metadata) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


def test_defended_load_3(app, thesis_metadata):
    thesis_metadata["defended"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1()
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


#######################################################################
#                           Study Field                               #
#######################################################################
def test_studyfield_load_1(app, thesis_metadata):
    thesis_metadata["studyField"] = [
        {
            "$ref": "https://localhost/api/taxonomies/studyfields/no_valid_fcc50779-a5d7-4359"
                    "-b9f8-2660d0e738f1"
        }
    ]

    schema = ThesisMetadataSchemaV1()
    with pytest.raises(ValidationError):
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


#######################################################################
#                           Degree grantor                            #
#######################################################################


#######################################################################
#                           Subject - Keywords                        #
#######################################################################
def test_subject_keywords_load_1(app, thesis_metadata):
    del thesis_metadata["subject"]
    schema = ThesisMetadataSchemaV1()

    with pytest.raises(ValidationError):
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_subject_keywords_load_2(app, thesis_metadata):
    del thesis_metadata["subject"]
    thesis_metadata["keywords"] = [
        {
            "name": "něco1",
            "lang": "cze"
        },
        {
            "name": "něco2",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1()

    with pytest.raises(ValidationError):
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_subject_keywords_load_3(app, thesis_metadata):
    thesis_metadata["subject"] = [
        {
            "$ref": "https://localhost/api/taxonomies/subject/nlk20040148348"
        },
        {
            "$ref": "https://localhost/api/taxonomies/subject/nlk20040147252"
        }
    ]
    schema = ThesisMetadataSchemaV1()

    with pytest.raises(ValidationError):
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)
