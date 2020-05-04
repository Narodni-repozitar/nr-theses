from copy import deepcopy
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


def test_language_load_3(app, thesis_metadata):
    thesis_metadata["language"] = [{
        "title": [
            {
                "lang": "cze",
                "value": "čeština"
            },
            {
                "lang": "eng",
                "value": "Czech"
            }
        ],
        "approved": True,
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 144576,
        "slug": "cze",
        "taxonomy": "languages",
        "path": "/cze",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/languages/cze/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/languages/cze/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/languages/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/languages/?drilldown=True"
        },
        "level": 1
    }]

    schema = ThesisMetadataSchemaV1()
    expexted_result = deepcopy(thesis_metadata)
    expexted_result["language"] = [{"$ref": "http://127.0.0.1:5000/api/taxonomies/languages/cze/"}]
    assert expexted_result == schema.load(convert_dates(thesis_metadata))


########################################################################
#                           Identifier                                 #
########################################################################
def test_identifier_dump_1(app, dump_metadata):
    dump_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]
    schema = ThesisMetadataSchemaV1()
    pprint(schema.dump(dump_metadata))
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
    dump_metadata["rights"] = [{
        "title": [
            {
                "lang": "cs",
                "value": "verze 1.0 Obecná licence"
            },
            {
                "lang": "en",
                "value": "version 1.0 Generic License"
            }
        ],
        "approved": True,
        # "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 210545,
        "slug": "1.0",
        "taxonomy": "licenses",
        "path": "/CC/1.0",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/?drilldown=True"
        },
        "level": 2,
        # "ancestors": [
        #     {
        #         "title": [
        #             {
        #                 "lang": "cs",
        #                 "value": "Licence Creative Commons"
        #             },
        #             {
        #                 "lang": "en",
        #                 "value": "License Creative Commons"
        #             }
        #         ],
        #         "approved": True,
        #         "level": 1,
        #         "slug": "CC"
        #     }
        # ],
        "descendants_count": 6.0
    }]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_rights_dump_2(dump_metadata):
    dump_metadata["rights"] = ["blbost"]
    schema = ThesisMetadataSchemaV1()
    with pytest.raises(TypeError):
        schema.dump(dump_metadata)


def test_rights_dump_3(dump_metadata):
    del dump_metadata["rights"]
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_rights_load_1(app, thesis_metadata):
    thesis_metadata["rights"] = [
        {
            "title": [
                {
                    "lang": "cs",
                    "value": "verze 1.0 Obecná licence"
                },
                {
                    "lang": "en",
                    "value": "version 1.0 Generic License"
                }
            ],
            "approved": True,
            "date_of_serialization": "2020-04-16 07:39:53.491593",
            "id": 210545,
            "slug": "1.0",
            "taxonomy": "licenses",
            "path": "/CC/1.0",
            "links": {
                "self": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/",
                "tree": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/?drilldown=True",
                "parent": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/",
                "parent_tree": "http://127.0.0.1:5000/api/taxonomies/licenses/CC/?drilldown=True"
            },
            "level": 2,
            "ancestors": [
                {
                    "title": [
                        {
                            "lang": "cs",
                            "value": "Licence Creative Commons"
                        },
                        {
                            "lang": "en",
                            "value": "License Creative Commons"
                        }
                    ],
                    "approved": True,
                    "level": 1,
                    "slug": "CC"
                }
            ],
            "descendants_count": 6.0
        }
    ]
    schema = ThesisMetadataSchemaV1()
    expected_metadata = deepcopy(thesis_metadata)
    expected_metadata["rights"] = [
        {'$ref': 'http://127.0.0.1:5000/api/taxonomies/licenses/CC/1.0/'}]
    assert expected_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_2(app, thesis_metadata):
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
            "role": {
                "title": [
                    {
                        "lang": "cze",
                        "value": "oponent"
                    },
                    {
                        "lang": "eng",
                        "value": "referee"
                    }
                ],
                "approved": True,
                "marcCode": "opn",
                # "date_of_serialization": "2020-04-16 07:39:53.491593",
                "id": 171348,
                "slug": "referee",
                "taxonomy": "contributor-type",
                "path": "/referee",
                "links": {
                    "self": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/",
                    "tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee"
                            "/?drilldown=True",
                    "parent": "http://127.0.0.1:5000/api/taxonomies/contributor-type/",
                    "parent_tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type"
                                   "/?drilldown=True"
                },
                "level": 1
            }
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
            "role": {
                "title": [
                    {
                        "lang": "cze",
                        "value": "oponent"
                    },
                    {
                        "lang": "eng",
                        "value": "referee"
                    }
                ],
                "approved": True,
                "marcCode": "opn",
                "date_of_serialization": "2020-04-16 07:39:53.491593",
                "id": 171348,
                "slug": "referee",
                "taxonomy": "contributor-type",
                "path": "/referee",
                "links": {
                    "self": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/",
                    "tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type/referee"
                            "/?drilldown=True",
                    "parent": "http://127.0.0.1:5000/api/taxonomies/contributor-type/",
                    "parent_tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type"
                                   "/?drilldown=True"
                },
                "level": 1
            }
        }
    ]
    expected_result = deepcopy(thesis_metadata)
    expected_result["contributor"][0]["role"] = {
        '$ref': 'http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/'
    }
    schema = ThesisMetadataSchemaV1()
    assert expected_result == schema.load(convert_dates(thesis_metadata)).data


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
def test_doc_type_dump_1(app, dump_metadata):
    dump_metadata["doctype"] = {
        "title": [
            {
                "lang": "cze",
                "value": "Diplomové práce"
            },
            {
                "lang": "eng",
                "value": "Master’s theses "
            }
        ],
        "approved": True,
        # "date_of_serialization": "2020-04-16 07:39:53.491593", # TODO: vyřešit format data
        "id": 180356,
        "slug": "diplomove_prace",
        "taxonomy": "doctypes",
        "path": "/nusl/vskp/diplomove_prace",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/diplomove_prace/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/diplomove_prace"
                    "/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/?drilldown=True"
        },
        "level": 3,
        # "ancestors": [
        #     {
        #         "title": [
        #             {
        #                 "lang": "cze",
        #                 "value": "Typologie Národního uložiště šedé literatury"
        #             },
        #             {
        #                 "lang": "eng",
        #                 "value": "Typology of National Repository of Grey Literature"
        #             }
        #         ],
        #         "approved": true,
        #         "level": 1,
        #         "slug": "nusl"
        #     },
        #     {
        #         "title": [
        #             {
        #                 "lang": "cze",
        #                 "value": "Vysokoškolské kvalifikační práce"
        #             },
        #             {
        #                 "lang": "eng",
        #                 "value": "Academic theses (ETDs)"
        #             }
        #         ],
        #         "approved": true,
        #         "level": 2,
        #         "slug": "vskp"
        #     }
        # ]
    }
    schema = ThesisMetadataSchemaV1()
    assert convert_dates(dump_metadata) == convert_dates(schema.dump(dump_metadata).data)


def test_doc_type_1(app, thesis_metadata):
    thesis_metadata["doctype"] = {
        "title": [
            {
                "lang": "cze",
                "value": "Diplomové práce"
            },
            {
                "lang": "eng",
                "value": "Master’s theses "
            }
        ],
        "approved": True,
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 180356,
        "slug": "diplomove_prace",
        "taxonomy": "doctypes",
        "path": "/nusl/vskp/diplomove_prace",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/diplomove_prace/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/diplomove_prace"
                    "/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/?drilldown=True"
        },
        "level": 3,
        "ancestors": [
            {
                "title": [
                    {
                        "lang": "cze",
                        "value": "Typologie Národního uložiště šedé literatury"
                    },
                    {
                        "lang": "eng",
                        "value": "Typology of National Repository of Grey Literature"
                    }
                ],
                "approved": True,
                "level": 1,
                "slug": "nusl"
            },
            {
                "title": [
                    {
                        "lang": "cze",
                        "value": "Vysokoškolské kvalifikační práce"
                    },
                    {
                        "lang": "eng",
                        "value": "Academic theses (ETDs)"
                    }
                ],
                "approved": True,
                "level": 2,
                "slug": "vskp"
            }
        ]
    }
    schema = ThesisMetadataSchemaV1()
    expected_result = deepcopy(thesis_metadata)
    expected_result["doctype"] = {
        "$ref": "http://127.0.0.1:5000/api/taxonomies/doctypes/nusl/vskp/diplomove_prace/"
    }
    assert expected_result == schema.load(convert_dates(thesis_metadata)).data


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
    dump_metadata["accessRights"] = {
        "title": [
            {
                "lang": "cze",
                "value": "pouze metadata"
            },
            {
                "lang": "eng",
                "value": "metadata only access"
            }
        ],
        "approved": True,
        "relatedURI": [
            {
                "value": "http://purl.org/coar/access_right/c_14cb",
                "type": "coar"
            },
            {
                "value": "http://purl.org/eprint/accessRights/ClosedAccess",
                "type": "eprint"
            },
            {
                "value": "",
                "type": "vocabs"
            }
        ],
        # "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 171277,
        "slug": "c_14cb",
        "taxonomy": "accessRights",
        "path": "/c_14cb",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/accessRights/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/accessRights/?drilldown=True"
        },
        "level": 1
    }
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
    thesis_metadata["accessRights"] = {
        "title": [
            {
                "lang": "cze",
                "value": "pouze metadata"
            },
            {
                "lang": "eng",
                "value": "metadata only access"
            }
        ],
        "approved": True,
        "relatedURI": [
            {
                "value": "http://purl.org/coar/access_right/c_14cb",
                "type": "coar"
            },
            {
                "value": "http://purl.org/eprint/accessRights/ClosedAccess",
                "type": "eprint"
            },
            {
                "value": "",
                "type": "vocabs"
            }
        ],
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 171277,
        "slug": "c_14cb",
        "taxonomy": "accessRights",
        "path": "/c_14cb",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/accessRights/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/accessRights/?drilldown=True"
        },
        "level": 1
    }
    schema = ThesisMetadataSchemaV1()
    expected_result = deepcopy(thesis_metadata)
    expected_result["accessRights"] = {
        '$ref': 'http://127.0.0.1:5000/api/taxonomies/accessRights/c_14cb/'
    }
    assert convert_dates(expected_result) == convert_dates(
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


def test_provider_2(app, thesis_metadata):
    thesis_metadata["provider"] = {
        "ico": "60461373",
        "url": "www.vscht.cz",
        "title": [
            {
                "lang": "cs",
                "value": "Vysoká škola chemicko-technologická v Praze"
            },
            {
                "lang": "en",
                "value": "University of Chemistry and Technology, Prague"
            }
        ],
        "aliases": [
            "VŠCHT"
        ],
        "approved": True,
        "provider": True,
        "relatedID": {
            "type": "rid",
            "value": "22000"
        },
        "date_of_serialization": "2020-04-17 06:49:26.591265",
        "id": 244838,
        "slug": "60461373",
        "taxonomy": "institutions",
        "path": "/60461373",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/institutions/60461373/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/institutions/60461373/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/institutions/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/institutions/?drilldown=True"
        },
        "level": 1,
        "descendants_count": 42.0
    }
    schema = ThesisMetadataSchemaV1()
    expected_result = deepcopy(thesis_metadata)
    expected_result["provider"] = {
        "$ref": "http://127.0.0.1:5000/api/taxonomies/institutions/60461373/"
    }
    assert convert_dates(expected_result) == convert_dates(
        schema.load(convert_dates(thesis_metadata)).data)


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
