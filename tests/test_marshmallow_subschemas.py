from pprint import pprint
from urllib.parse import urlparse

import pytest
from marshmallow.exceptions import ValidationError

from invenio_nusl_theses.marshmallow.json import ApprovedTaxonomySchema, RightsMetadataSchemaV1, \
    ContributorTaxonomySchema, AccessRightsSubSchema, InstitutionsSubClass


#########################################################################
#                             SUBJECT                                   #
#########################################################################
def test_psh_1():
    pass


#########################################################################
#                             RIGHTS                                    #
#########################################################################
def test_rights(app, right_fix):
    schema = RightsMetadataSchemaV1()
    result = schema.load(right_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(right_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                             CONTRIBUTOR                               #
#########################################################################
def test_contributor(app, contributor_fix):
    schema = ContributorTaxonomySchema()
    result = schema.load(contributor_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(contributor_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                             STUDY FIELD                               #
#########################################################################
def test_study_field(app, studyfield_fix):
    schema = ContributorTaxonomySchema()
    result = schema.load(studyfield_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(studyfield_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                             LANGUAGE                                  #
#########################################################################
def test_language(app, language_fix):
    schema = ContributorTaxonomySchema()
    result = schema.load(language_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(language_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                             ACCESS RIGHTS                             #
#########################################################################
def test_accessrigts(app, access_fix):
    schema = AccessRightsSubSchema()
    result = schema.load(access_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(access_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                             INSTITUTION                              #
#########################################################################
def test_institution(app, institution_fix):
    schema = InstitutionsSubClass()
    result = schema.load(institution_fix)
    url = urlparse(result["$ref"])
    expected_url = urlparse(institution_fix["links"]["self"])
    assert url.path == expected_url.path


#########################################################################
#                       APPROVED                                        #
#########################################################################
def test_approved_1():
    schema = ApprovedTaxonomySchema()
    meta_data = {
        "approved": True
    }
    result = schema.load(meta_data)
    pprint(result)


def test_approved_2():
    schema = ApprovedTaxonomySchema()
    meta_data = {
        "approved": False
    }
    with pytest.raises(ValidationError):
        schema.load(meta_data)


def test_approved_3():
    schema = ApprovedTaxonomySchema()
    meta_data = {
        "title": [
            {
                "value": "bla",
                "lang": "cze"
            }
        ]
    }
    result = schema.load(meta_data)
    pprint(result)


#########################################################################
#                             FIXTURES                                  #
#########################################################################
@pytest.fixture()
def psh_fix():
    return


@pytest.fixture()
def right_fix():
    return {
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


@pytest.fixture()
def contributor_fix():
    return {
        "title": [
            {
                "lang": "cze",
                "value": "manažer dat"
            },
            {
                "lang": "eng",
                "value": "data manager"
            }
        ],
        "approved": True,
        "marcCode": "dtm",
        "dataCiteCode": "DataManager",
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 171336,
        "slug": "data-manager",
        "taxonomy": "contributor-type",
        "path": "/data-manager",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/contributor-type/data-manager/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type/data-manager"
                    "/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/contributor-type/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/contributor-type/?drilldown=True"
        },
        "level": 1
    }


@pytest.fixture()
def language_fix():
    return {
        "title": [
            {
                "lang": "cze",
                "value": "Učitelství praktického vyučování"
            }
        ],
        "approved": True,
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 172326,
        "slug": "O_ucitelstvi-praktickeho-vyucovani",
        "taxonomy": "studyfields",
        "path": "/P_specializace-v-pedagogice/O_ucitelstvi-praktickeho-vyucovani",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/studyfields/P_specializace-v-pedagogice"
                    "/O_ucitelstvi-praktickeho-vyucovani/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/studyfields/P_specializace-v-pedagogice"
                    "/O_ucitelstvi-praktickeho-vyucovani/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/studyfields/P_specializace-v"
                      "-pedagogice/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/studyfields/P_specializace-v"
                           "-pedagogice/?drilldown=True"
        },
        "level": 2,
        "ancestors": [
            {
                "title": [
                    {
                        "lang": "cze",
                        "value": "Specializace v pedagogice"
                    }
                ],
                "approved": True,
                "level": 1,
                "slug": "P_specializace-v-pedagogice"
            }
        ]
    }


@pytest.fixture()
def language_fix():
    return {
        "title": [
            {
                "lang": "cze",
                "value": "bulharština"
            },
            {
                "lang": "eng",
                "value": "Bulgarian"
            }
        ],
        "approved": True,
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 144574,
        "slug": "bul",
        "taxonomy": "languages",
        "path": "/bul",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/languages/bul/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/languages/bul/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/languages/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/languages/?drilldown=True"
        },
        "level": 1
    }


@pytest.fixture()
def institution_fix():
    return {
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
                "uri": "http://purl.org/coar/access_right/c_14cb",
                "type": "coar"
            },
            {
                "uri": "http://purl.org/eprint/accessRights/ClosedAccess",
                "type": "eprint"
            },
            {
                "uri": "",
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


@pytest.fixture()
def institution_fix():
    return {
        "ico": "00020702",
        "url": "http://www.vulhm.cz/",
        "title": [
            {
                "lang": "cs",
                "value": "Výzkumný ústav lesního hospodářství a myslivosti"
            },
            {
                "lang": "en",
                "value": "Forestry and Game Management Research Institute"
            }
        ],
        "aliases": [
            "VÚLHM"
        ],
        "approved": True,
        "provider": True,
        "date_of_serialization": "2020-04-16 07:39:53.491593",
        "id": 243442,
        "slug": "00020702",
        "taxonomy": "institutions",
        "path": "/00020702",
        "links": {
            "self": "http://127.0.0.1:5000/api/taxonomies/institutions/00020702/",
            "tree": "http://127.0.0.1:5000/api/taxonomies/institutions/00020702/?drilldown=True",
            "parent": "http://127.0.0.1:5000/api/taxonomies/institutions/",
            "parent_tree": "http://127.0.0.1:5000/api/taxonomies/institutions/?drilldown=True"
        },
        "level": 1
    }
