import pytest

from invenio_nusl_theses.marshmallow.json import ThesisRecordSchemaV1, ThesisMetadataSchemaV1
from marshmallow.exceptions import ValidationError
from datetime import date

json = {
    "language": [
        "CZE"
    ],
    "identifier": [{
        "value": "151515",
        "type": "nusl"
    }],
    "dateAccepted": "2019-05-19"
}


########################################################################
#                           Language                                   #
########################################################################
def test_language_dump_1():
    user_data = dict(json)
    user_data["language"] = ["CZE", "GER"]
    schema = ThesisMetadataSchemaV1(strict=True)
    deser_data = schema.load(user_data).data
    assert user_data == schema.dump(deser_data).data


# def test_language_dump_2():
#     user_data = dict(json)
#     user_data["language"] = "CZE"
#     schema = ThesisMetadataSchemaV1(strict=True)
#     deser_data = schema.load(user_data).data
#     assert user_data != schema.dump(deser_data).data


def test_language_load_1():
    user_data = dict(json)
    user_data["language"] = [
        "CZE", "GER"
    ]

    schema = ThesisMetadataSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == schema.dump(result.data).data


def test_language_load_2():
    user_data = dict(json)
    user_data["language"] = [
        "CZE", "blbost"
    ]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.load(user_data)


def test_language_load_3():
    user_data = dict(json)
    user_data["language"] = "CZE"

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.load(user_data)


########################################################################
#                           Identifier                                 #
########################################################################
def test_identifier_dump_1():
    user_data = dict(json)
    user_data["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]
    schema = ThesisMetadataSchemaV1(strict=True)
    assert user_data == schema.dump(schema.load(user_data).data).data


def test_identifier_load_1():
    user_data = dict(json)
    user_data["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    }]

    schema = ThesisMetadataSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == schema.dump(result.data).data


def test_identifier_load_2():
    user_data = dict(json)
    user_data["identifier"] = [{
        "value": "151515",
        "type": "nusl"
    },
        {
            "value": "15dsfa515",
            "type": "nuslOAI"
        }
    ]

    schema = ThesisMetadataSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == schema.dump(result.data).data


def test_identifier_load_3():
    user_data = dict(json)
    del user_data["identifier"]

    with pytest.raises(ValidationError):
        schema = ThesisMetadataSchemaV1(strict=True)
        result = schema.load(user_data)


########################################################################
#                           dateAccepted                               #
########################################################################
def test_dateaccepted_load_1():
    user_data = dict(json)
    user_data["dateAccepted"] = "2019-05-19"

    schema = ThesisMetadataSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == schema.dump(result.data).data


def test_dateaccepted_load_2(): #TODO vyřešit assertion error
    user_data = dict(json)
    user_data["dateAccepted"] = "20190519"

    schema = ThesisMetadataSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data
