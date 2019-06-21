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
                "name": "Avallable at blabla",
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
                "language": "cze",
                "university": {
                    "name": "Vysoká škola chemicko-technologická v Praze",
                    "faculties": [
                        {
                            "name": "Fakulta chemické technologie",
                            "departments": [
                                "Ústav organické technologie"
                            ]
                        }
                    ]
                }
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


########################################################################
#                             doctype                                  #
########################################################################
def test_doctype_dump_1(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "studie",
                 "bterm": "anl_met_mat"}
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_doctype_dump_2(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "studie",
                 "bterm": "anl_met_mat"},
        "RIV": {"term": "polop",
                "bterm": "Z"}
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_doctype_dump_3(thesis_metadata):
    del thesis_metadata["doctype"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_doctype_load_1(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "studie",
                 "bterm": "anl_met_mat"}
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_doctype_load_2(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "studie",
                 "bterm": "anl_met_mat"},
        "RIV": {"term": "polop",
                "bterm": "Z"}
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_doctype_load_3(thesis_metadata):
    thesis_metadata["doctype"] = {
        "RIV": {"term": "polop",
                "bterm": "Z"}
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_doctype_load_4(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "studie",
                 "bterm": "vskp"}
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


def test_doctype_load_5(thesis_metadata):
    thesis_metadata["doctype"] = {
        "NUSL": {"term": "bakalarske_prace",
                 "bterm": "vskp"},
        "RIV": {"term": None,
                "bterm": "W"}
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                             id                                       #
########################################################################
def test_id_dump_1(thesis_metadata):
    thesis_metadata["id"] = 2562727272
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_id_dump_2(thesis_metadata):
    del thesis_metadata["id"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.dump(thesis_metadata).data)


def test_id_dump_3(thesis_metadata):
    thesis_metadata["id"] = "2562727272"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != convert_dates(schema.dump(thesis_metadata).data)


def test_id_load_1(thesis_metadata):
    thesis_metadata["id"] = 2562727272
    schema = ThesisMetadataSchemaV1(strict=True)
    assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_id_load_2(thesis_metadata):
    del thesis_metadata["id"]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        assert thesis_metadata == schema.load(convert_dates(thesis_metadata)).data


def test_id_load_3(thesis_metadata):
    thesis_metadata["id"] = "2562727272"
    schema = ThesisMetadataSchemaV1(strict=True)
    final_metadata = dict(thesis_metadata)
    final_metadata["id"] = 2562727272
    assert final_metadata == schema.load(convert_dates(thesis_metadata)).data


########################################################################
#                              subtitle                                #
########################################################################
def test_subtitle_dump_1(thesis_metadata):
    thesis_metadata["subtitle"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cze"
         }]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_subtitle_dump_2(thesis_metadata):
    thesis_metadata["subtitle"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cz"
         }]
    # with pytest.raises(ValidationError):
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_subtitle_dump_3(thesis_metadata):
    thesis_metadata["subtitle"] = "blbost"
    with pytest.raises(AssertionError):
        schema = ThesisMetadataSchemaV1(strict=True)
        assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_subtitle_dump_4(thesis_metadata):
    del thesis_metadata["subtitle"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_subtitle_load_1(thesis_metadata):
    thesis_metadata["subtitle"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cze"
         }]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_subtitle_load_2(thesis_metadata):
    thesis_metadata["subtitle"] = [
        {"name": "Historická krajina Českomoravské vrchoviny. Osídlení od pravěku do sklonku středověku.",
         "lang": "cz"
         }]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        schema.load(convert_dates(thesis_metadata))


########################################################################
#                              note                                    #
########################################################################
def test_note_dump_1(thesis_metadata):
    thesis_metadata["note"] = [
        "Poznámka 1",
        "Poznámka 2"
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_note_dump_2(thesis_metadata):
    del thesis_metadata["note"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_note_dump_3(thesis_metadata):
    thesis_metadata["note"] = {
        "Poznámka 1",
        "Poznámka 2"
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_note_load_1(thesis_metadata):
    thesis_metadata["note"] = [
        "Poznámka 1",
        "Poznámka 2"
    ]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_note_load_2(thesis_metadata):
    del thesis_metadata["note"]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_note_load_3(thesis_metadata):
    thesis_metadata["note"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           accessibility                              #
########################################################################
def test_accessibility_dump_1(thesis_metadata):
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
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_accessibility_dump_2(thesis_metadata):
    del thesis_metadata["accessibility"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_accessibility_dump_3(thesis_metadata):
    thesis_metadata["accessibility"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_accessibility_load_1(thesis_metadata):
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

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessibility_load_2(thesis_metadata):
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
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessibility_load_3(thesis_metadata):
    del thesis_metadata["accessibility"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           accessRights                               #
########################################################################
def test_accessRights_dump_1(thesis_metadata):
    thesis_metadata["accessRights"] = "open"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_accessRights_dump_2(thesis_metadata):
    del thesis_metadata["accessRights"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_accessRights_dump_3(thesis_metadata):
    thesis_metadata["accessRights"] = ["Jiný datový typ"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_accessRights_load_1(thesis_metadata):
    thesis_metadata["accessRights"] = "open"

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_2(thesis_metadata):
    thesis_metadata["accessRights"] = "blbost"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_3(thesis_metadata):
    del thesis_metadata["accessRights"]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_accessRights_load_4(thesis_metadata):
    thesis_metadata["accessRights"] = None
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           Provider                                   #
########################################################################
def test_provider_dump_1(thesis_metadata):
    thesis_metadata["provider"] = {
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
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_provider_dump_2(thesis_metadata):
    thesis_metadata["provider"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_provider_dump_3(thesis_metadata):
    del thesis_metadata["provider"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_provider_load_1(thesis_metadata):
    thesis_metadata["provider"] = {
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
    }

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_provider_load_2(thesis_metadata):
    del thesis_metadata["provider"]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


########################################################################
#                           Defended                                   #
########################################################################
def test_defended_dump_1(thesis_metadata):
    thesis_metadata["defended"] = False
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_defended_dump_2(thesis_metadata):
    thesis_metadata["defended"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


# def test_defended_dump_3(thesis_metadata): #TODO: dořešit
#     del thesis_metadata["defended"]
#     schema = ThesisMetadataSchemaV1(strict=True)
#     assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_defended_load_1(thesis_metadata):
    thesis_metadata["defended"] = False

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_defended_load_2(thesis_metadata):
    del thesis_metadata["defended"]

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_defended_load_3(thesis_metadata):
    thesis_metadata["defended"] = "jiný datový typ"
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


#######################################################################
#                           Study Programme                           #
#######################################################################
def test_studyProgramme_dump_1(thesis_metadata):
    thesis_metadata["studyProgramme"] = {
        "code": "B1407",
        "name": "Chemie"
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_studyProgramme_dump_2(thesis_metadata):
    thesis_metadata["studyProgramme"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_studyProgramme_dump_3(thesis_metadata):
    del thesis_metadata["studyProgramme"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_studyProgramme_load_1(thesis_metadata):
    thesis_metadata["studyProgramme"] = {
        "code": "B1407",
        "name": "Chemie"
    }

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyProgramme_load_2(thesis_metadata):
    thesis_metadata["studyProgramme"] = {
        "code": "blbost",
        "name": "Chemie"
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyProgramme_load_3(thesis_metadata):
    del thesis_metadata["studyProgramme"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyProgramme_load_4(thesis_metadata):
    thesis_metadata["studyProgramme"] = {
        "code": "B1407",
        "name": "Chemie (čtyřletá)"
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)

def test_studyProgramme_load_5(thesis_metadata):
    thesis_metadata["studyProgramme"] = {
        "name": "Chemie"
    }

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)




#######################################################################
#                           Study Field                               #
#######################################################################
def test_studyField_dump_1(thesis_metadata):
    thesis_metadata["studyField"] = {
        "code": "2801T015",
        "name": "Technologie organických látek a chemické speciality"
    }
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_studyField_dump_2(thesis_metadata):
    del thesis_metadata["studyField"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_studyField_dump_3(thesis_metadata):
    thesis_metadata["studyField"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_studyField_load_1(thesis_metadata):
    thesis_metadata["studyField"] = {
        "code": "2801T015",
        "name": "Technologie organických látek a chemické speciality"
    }

    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyField_load_2(thesis_metadata):
    del thesis_metadata["studyField"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyField_load_3(thesis_metadata):
    thesis_metadata["studyField"] = {
        "code": "blbost",
        "name": "Technologie organických látek a chemické speciality"
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyField_load_4(thesis_metadata):
    thesis_metadata["studyField"] = {
        "code": "2801T015",
        "name": "blbost"
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_studyField_load_5(thesis_metadata):
    thesis_metadata["studyField"] = {
        "code": "2801T007",
        "name": "Technologie organických látek a chemické speciality"
    }
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


#######################################################################
#                           Degree grantor                            #
#######################################################################
def test_degreeGrantor_dump_1(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cze",
            "university": {
                "name": "Vysoká škola chemicko-technologická",
                "faculties": [
                    {
                        "name": "Fakulta chemické technologie",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_degreeGrantor_dump_2(thesis_metadata):
    del thesis_metadata["degreeGrantor"]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == schema.dump(thesis_metadata).data


def test_degreeGrantor_dump_3(thesis_metadata):
    thesis_metadata["degreeGrantor"] = "jiný datový typ"
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) != schema.dump(thesis_metadata).data


def test_degreeGrantor_load_1(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cze",
            "university": {
                "name": "Vysoká škola chemicko-technologická v Praze",
                "faculties": [
                    {
                        "name": "Fakulta chemické technologie",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_degreeGrantor_load_2(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cze",
            "university": {
                "name": "Vysoká škola chemicko-technologická",
                "faculties": [
                    {
                        "name": "Fakulta chemické technologie",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_degreeGrantor_load_3(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cze",
            "university": {
                "name": "Vysoká škola chemicko-technologická",
                "faculties": [
                    {
                        "name": "Fakulta chemické technologie",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_degreeGrantor_load_4(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cz",
            "university": {
                "name": "Vysoká škola chemicko-technologická v Praze",
                "faculties": [
                    {
                        "name": "Fakulta chemické technologie",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_degreeGrantor_load_5(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
        {
            "language": "cze",
            "university": {
                "name": "Vysoká škola chemicko-technologická v Praze",
                "faculties": [
                    {
                        "name": "Neexistující fakulta",
                        "departments": [
                            "Ústav organické technologie"
                        ]
                    }
                ]
            }
        }
    ]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)


def test_degreeGrantor_load_6(thesis_metadata):
    del thesis_metadata["degreeGrantor"]
    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        convert_dates(schema.load(convert_dates(thesis_metadata)).data)

def test_degreeGrantor_load_7(thesis_metadata):
    thesis_metadata["degreeGrantor"] = [
            {
                "language": "cze",
                "university": {
                    "name": "Univerzita Karlova",
                    "faculties": [
                        {
                            "name": "Fakulta tělesné výchovy a sportu",
                            "departments": [
                                "Fyzioterapie"
                            ]
                        }
                    ]
                }
            },
            {
                "language": "eng",
                "university": {
                    "name": "Charles University",
                    "faculties": [
                        {
                            "name": "Faculty of Physical Education and Sport",
                            "departments": [
                                None
                            ]
                        }
                    ]
                }
            }
        ]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert convert_dates(thesis_metadata) == convert_dates(schema.load(convert_dates(thesis_metadata)).data)
