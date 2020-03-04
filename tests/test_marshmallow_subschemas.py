import pytest
from marshmallow.exceptions import ValidationError

from invenio_nusl_theses.marshmallow.json import CCMetadataSchemaV1, RightsMetadataSchemaV1
from tests.utils import convert_dates


@pytest.fixture
def cc_metada():
    return {
        "code": "CC BY",
        "version": "3.0",
        "country": "CZ"
    }


@pytest.fixture()
def rights_metadata():
    return {
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


########################################################################
#                           CODE                                       #
########################################################################
def test_code_dump_1(cc_metada):
    cc_metada["code"] = "CC BY"
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_code_dump_2(cc_metada):
    cc_metada["code"] = "blbost"
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_code_dump_3(cc_metada):
    del cc_metada["code"]
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_code_load_1(cc_metada):
    cc_metada["code"] = "CC BY"
    schema = CCMetadataSchemaV1()
    assert cc_metada == schema.load(convert_dates(cc_metada)).data


def test_code_load_2(cc_metada):
    cc_metada["code"] = "blbost"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


def test_code_load_3(cc_metada):
    del cc_metada["code"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


########################################################################
#                           VERSION                                    #
########################################################################
def test_version_dump_1(cc_metada):
    cc_metada["version"] = "3.0"
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_version_dump_2(cc_metada):
    cc_metada["version"] = 3
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) != convert_dates(schema.dump(cc_metada).data)


def test_version_dump_3(cc_metada):
    del cc_metada["version"]
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_version_load_1(cc_metada):
    cc_metada["version"] = "3.0"
    schema = CCMetadataSchemaV1()
    assert cc_metada == schema.load(convert_dates(cc_metada)).data


def test_version_load_2(cc_metada):
    cc_metada["version"] = "3"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


def test_version_load_3(cc_metada):
    del cc_metada["version"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


def test_version_load_4(cc_metada):
    cc_metada["version"] = 3
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


########################################################################
#                           COUNTRY                                    #
########################################################################
def test_country_dump_1(cc_metada):
    cc_metada["country"] = "CZ"
    schema = CCMetadataSchemaV1()
    assert convert_dates(cc_metada) == convert_dates(schema.dump(cc_metada).data)


def test_country_load_1(cc_metada):
    cc_metada["country"] = "CZ"
    schema = CCMetadataSchemaV1()
    assert cc_metada == schema.load(convert_dates(cc_metada)).data


def test_country_load_2(cc_metada):
    cc_metada["country"] = "CZE"
    schema = CCMetadataSchemaV1()
    final_schema = dict(cc_metada)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(cc_metada)).data


def test_country_load_3(cc_metada):
    cc_metada["country"] = "Czechia"
    schema = CCMetadataSchemaV1()
    final_schema = dict(cc_metada)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(cc_metada)).data


def test_country_load_4(cc_metada):
    cc_metada["country"] = "Czech Republic"
    schema = CCMetadataSchemaV1()
    final_schema = dict(cc_metada)
    final_schema["country"] = "CZ"
    assert final_schema == schema.load(convert_dates(cc_metada)).data


def test_country_load_5(cc_metada):
    cc_metada["country"] = "blbost"
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


def test_country_load_6(cc_metada):
    del cc_metada["country"]
    with pytest.raises(ValidationError):
        schema = CCMetadataSchemaV1()
        schema.load(convert_dates(cc_metada))


########################################################################
#                           COPYRIGHT                                  #
########################################################################
def test_copyright_load_1(rights_metadata):
    schema = RightsMetadataSchemaV1()
    assert rights_metadata == schema.load(convert_dates(rights_metadata)).data
