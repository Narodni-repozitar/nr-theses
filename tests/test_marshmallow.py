from datetime import date, datetime

import pytest
import pytz
from marshmallow.exceptions import ValidationError

from invenio_nusl_theses.marshmallow.json import ThesisMetadataSchemaV1
from tests.utils import convert_dates


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
        ]
    }


########################################################################
#                           Language                                   #
########################################################################
def test_language_dump_1(thesis_metadata):
    thesis_metadata["language"] = ["CZE", "GER"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_language_load_1(thesis_metadata):
    thesis_metadata["language"] = [
        "CZE", "GER"
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_language_load_2(thesis_metadata):
    thesis_metadata["language"] = [
        "CZE", "blbost"
    ]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.load(convert_dates(thesis_metadata))


def test_language_load_3(thesis_metadata):
    thesis_metadata["language"] = "CZE"

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.load(convert_dates(thesis_metadata))


########################################################################
#                           Identifier                                 #
########################################################################
def test_identifier_dump_1(thesis_metadata):
    thesis_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_identifier_load_1(thesis_metadata):
    thesis_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_identifier_load_2(thesis_metadata):
    thesis_metadata["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    },
        {
            "value": "15dsfa515",
            "type": "nuslOAI"
        }
    ]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_identifier_load_3(thesis_metadata):
    del thesis_metadata["identifier"]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                           dateAccepted                               #
########################################################################
def test_dateaccepted_dump_1(thesis_metadata):
    thesis_metadata["dateAccepted"] = date(2019, 5, 19)
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_dateaccepted_dump_2(thesis_metadata):
    del thesis_metadata["dateAccepted"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_dateaccepted_dump_3(thesis_metadata):
    thesis_metadata["dateAccepted"] = "blbost"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.dump(thesis_metadata)


def test_dateaccepted_load_1(thesis_metadata):
    thesis_metadata["dateAccepted"] = "2019-05-19"

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


# def test_dateaccepted_load_2(thesis_metadata): #TODO: dořešit
#     thesis_metadata["dateAccepted"] = "20190519"
#
#     schema = ThesisMetadataSchemaV1(strict=True)
#     assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_dateaccepted_load_3(thesis_metadata):
    del thesis_metadata["dateAccepted"]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                           modified                                   #
########################################################################
def test_modified_dump_1(thesis_metadata):
    thesis_metadata["modified"] = "blbost"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.dump(thesis_metadata).data


def test_modified_load_1(thesis_metadata):
    thesis_metadata["modified"] = "2014-12-22T03:12:58.019077+00:00"

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_modified_load_2(thesis_metadata):
    thesis_metadata["modified"] = "2014-12-22"

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_modified_load_3(thesis_metadata):
    del thesis_metadata["modified"]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                              title                                   #
########################################################################
def test_title_dump_1(thesis_metadata):
    thesis_metadata["title"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cze"
         }]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_title_dump_2(thesis_metadata):
    thesis_metadata["title"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cz"
         }]
    # with pytest.raises(ValidationError):
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_title_dump_3(thesis_metadata):
    thesis_metadata["title"] = "blbost"
    with pytest.raises(AssertionError):
        schema = ThesisMetadataSchemaV1(strict=True)
        assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_title_dump_4(thesis_metadata):
    del thesis_metadata["title"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_title_load_1(thesis_metadata):
    thesis_metadata["title"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cze"
         }]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_title_load_2(thesis_metadata):
    thesis_metadata["title"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cz"
         }]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              extent                                  #
########################################################################
def test_extent_dump_1(thesis_metadata):
    thesis_metadata["extent"] = "123 s."
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_extent_dump_2(thesis_metadata):
    del thesis_metadata["extent"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_extent_dump_3(thesis_metadata):
    thesis_metadata["extent"] = 123
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_extent_load_1(thesis_metadata):
    thesis_metadata["extent"] = "123 s."
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_extent_load_2(thesis_metadata):
    del thesis_metadata["extent"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_extent_load_3(thesis_metadata):
    thesis_metadata["extent"] = 123
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_extent_load_4(thesis_metadata):
    thesis_metadata["extent"] = ["123 s."]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              abstract                                #
########################################################################
def test_abstract_dump_1(thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné činnosti zpět do společnosti. V rámci práce je na základě odborné literatury a získaných informací cílem seznámit zájemce, a to v teoretické části práce, s hlavními termíny a problematikou daného tématu. V praktické části je popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti sociální integrace pachatelů trestné činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_abstract_dump_2(thesis_metadata):
    del thesis_metadata["abstract"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_abstract_dump_3(thesis_metadata):
    thesis_metadata["abstract"] = 123  # jiný datový typ
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_abstract_load_1(thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné činnosti zpět do společnosti. V rámci práce je na základě odborné literatury a získaných informací cílem seznámit zájemce, a to v teoretické části práce, s hlavními termíny a problematikou daného tématu. V praktické části je popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti sociální integrace pachatelů trestné činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cze"
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_2(thesis_metadata):
    del thesis_metadata["abstract"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_3(thesis_metadata):
    thesis_metadata["abstract"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_4(thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné činnosti zpět do společnosti. V rámci práce je na základě odborné literatury a získaných informací cílem seznámit zájemce, a to v teoretické části práce, s hlavními termíny a problematikou daného tématu. V praktické části je popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti sociální integrace pachatelů trestné činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "cs"
        }
    ]
    final_metadata = dict(thesis_metadata)
    final_metadata["abstract"][0]["lang"] = "cze"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_abstract_load_5(thesis_metadata):
    thesis_metadata["abstract"] = [
        {
            "name": "Bakalářská práce je zaměřena na téma možností integrace pachatelů trestné činnosti zpět do společnosti. V rámci práce je na základě odborné literatury a získaných informací cílem seznámit zájemce, a to v teoretické části práce, s hlavními termíny a problematikou daného tématu. V praktické části je popsán průběh sběru dat až po výsledky kvalitativního výzkumu. Hlavním cílem bakalářské práce na téma Možnosti sociální integrace pachatelů trestné činnosti zpět do společnosti je objasnit okolnosti a podmínky integrace pachatele trestné činnosti zpět do společnosti po propuštění z výkonu trestu odnětí svobody. Ve vedlejším cíli je zjišťováno, zda potřeby propuštěných z výkonu trestu odnětí svobody při jejich zpětné integraci do společnosti odpovídají možnostem, které naše společnost poskytuje.",
            "lang": "ces"
        }
    ]
    final_metadata = dict(thesis_metadata)
    final_metadata["abstract"][0]["lang"] = "cze"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              rights                                  #
########################################################################
def test_rights_dump_1(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_rights_dump_2(thesis_metadata):
    thesis_metadata["rights"] = "blbost"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_rights_dump_3(thesis_metadata):
    del thesis_metadata["rights"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_rights_load_1(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_2(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert final_data == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_3(thesis_metadata):
    thesis_metadata["rights"] = {
        "CC": {
            "code": "CC BY",
            "version": "3.0",
            "country": "CZ"
        },
        "copyright": []
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_rights_load_4(thesis_metadata):
    del thesis_metadata["rights"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              subject                                 #
########################################################################
def test_subject_dump_1(thesis_metadata):
    thesis_metadata["subject"] = [
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
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_subject_dump_2(thesis_metadata):
    thesis_metadata["subject"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_subject_dump_3(thesis_metadata):
    del thesis_metadata["subject"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_subject_load_1(thesis_metadata):
    thesis_metadata["subject"] = [
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
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_subject_load_2(thesis_metadata):
    thesis_metadata["subject"] = [
        {
            "name": "koza"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze",
            "taxonomy": "psh",
            "id": "http://psh.techlib.cz/skos/PSH5740"
        }
    ]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_subject_load_3(thesis_metadata):
    thesis_metadata["subject"] = [
        {
            "name": "koza",
            "lang": "cze"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze",
            "taxonomy": "unknown",
            "id": "http://psh.techlib.cz/skos/PSH5740"
        }
    ]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_subject_load_4(thesis_metadata):
    thesis_metadata["subject"] = [
        {
            "name": "koza",
            "lang": "cze"
        },
        {
            "name": "anorganická chemie",
            "lang": "cze",
            "taxonomy": "psh",
            "id": "http://www.bljsdafjhdsahfjdshajkdf.cz/"
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    schema.load(convert_dates(thesis_metadata))
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                             creator                                  #
########################################################################
def test_creator_dump_1(thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            }
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_creator_dump_2(thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel"
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_creator_dump_3(thesis_metadata):
    thesis_metadata["creator"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_creator_dump_4(thesis_metadata):
    del thesis_metadata["creator"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_creator_load_1(thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
                "type": "ORCID"
            }
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_creator_load_2(thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel"
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_creator_load_3(thesis_metadata):
    thesis_metadata["creator"] = [
        {
            "name": "Kopecký, Daniel",
            "id": {
                "value": "21454545",
            }
        }
    ]
    with pytest.raises(ValidationError):  # Chybí typ id
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_creator_load_4(thesis_metadata):
    del thesis_metadata["creator"]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                             contributor                              #
########################################################################
def test_contributor_dump_1(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_contributor_dump_2(thesis_metadata):
    thesis_metadata["contributor"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_contributor_dump_3(thesis_metadata):
    del thesis_metadata["contributor"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_contributor_load_1(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_contributor_load_2(thesis_metadata):
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
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_contributor_load_3(thesis_metadata):
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
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))
