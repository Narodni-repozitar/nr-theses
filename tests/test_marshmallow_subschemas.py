import pytest
from marshmallow.exceptions import ValidationError

from invenio_nusl_theses.marshmallow.json import CCMetadataSchemaV1
from tests.utils import convert_dates


@pytest.fixture
def CC_metadata():
    return {
        "code": "CC BY",
        "version": "3.0",
        "country": "CZ"
    }


########################################################################
#                           CODE                                       #
########################################################################
def test_code_dump_1(CC_metadata):
    CC_metadata["code"] = "CC BY"
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)


def test_code_dump_2(CC_metadata):
    CC_metadata["code"] = "blbost"
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)


def test_code_dump_3(CC_metadata):
    del CC_metadata["code"]
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)


def test_code_load_1(CC_metadata):
    CC_metadata["code"] = "CC BY"
    schema = CCMetadataSchemaV1(strict=True)
    assert CC_metadata == schema.load(convert_dates(CC_metadata)).data


def test_code_load_2(CC_metadata):
    CC_metadata["code"] = "blbost"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))


def test_code_load_3(CC_metadata):
    del CC_metadata["code"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))


########################################################################
#                           VERSION                                    #
########################################################################
def test_version_dump_1(CC_metadata):
    CC_metadata["version"] = "3.0"
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)


def test_version_dump_2(CC_metadata):
    CC_metadata["version"] = 3
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) != convert_dates(schema.dump(CC_metadata).data)


def test_version_dump_3(CC_metadata):
    del CC_metadata["version"]
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)


def test_version_load_1(CC_metadata):
    CC_metadata["version"] = "3.0"
    schema = CCMetadataSchemaV1(strict=True)
    assert CC_metadata == schema.load(convert_dates(CC_metadata)).data


def test_version_load_2(CC_metadata):
    CC_metadata["version"] = "3"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))


def test_version_load_3(CC_metadata):
    del CC_metadata["version"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))


def test_version_load_4(CC_metadata):
    CC_metadata["version"] = 3
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))


########################################################################
#                           COUNTRY                                    #
########################################################################
def test_country_dump_1(CC_metadata):
    CC_metadata["country"] = "CZ"
    schema = CCMetadataSchemaV1(strict=True)
    assert convert_dates(CC_metadata) == convert_dates(schema.dump(CC_metadata).data)

def test_country_load_1(CC_metadata):
    CC_metadata["country"] = "CZ"
    schema = CCMetadataSchemaV1(strict=True)
    assert CC_metadata == schema.load(convert_dates(CC_metadata)).data

def test_country_load_2(CC_metadata):
    CC_metadata["country"] = "CZE"
    schema = CCMetadataSchemaV1(strict=True)
    final_schema = dict(CC_metadata)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(CC_metadata)).data

def test_country_load_3(CC_metadata):
    CC_metadata["country"] = "Czechia"
    schema = CCMetadataSchemaV1(strict=True)
    final_schema = dict(CC_metadata)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(CC_metadata)).data

def test_country_load_4(CC_metadata):
    CC_metadata["country"] = "Czech Republic"
    schema = CCMetadataSchemaV1(strict=True)
    final_schema = dict(CC_metadata)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(CC_metadata)).data

def test_country_load_5(CC_metadata):
    CC_metadata["country"] = "blbost"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))

def test_country_load_5(CC_metadata):
    del CC_metadata["country"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1(strict=True)
        schema.load(convert_dates(CC_metadata))
