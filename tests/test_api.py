from pprint import pprint

import pytest
from invenio_nusl_theses.record import PublishedThesisRecord

from invenio_nusl_theses.proxies import nusl_theses


@pytest.mark.usefixtures("app", "db", "taxonomy_tree", "base_json", "base_json_dereferenced")
class TestAPI:
    # def test_import_old_nusl_record(self, app, db, taxonomy_tree, base_json,
    #                                 base_json_dereferenced):
    #     nusl_theses.import_old_nusl_record(base_json_dereferenced)

    def test_get_record_by_id(self):
        assert nusl_theses.get_record_by_id("dnusl", "1") is None

    def test_create_draft_record(self, base_json_dereferenced):
        record = nusl_theses.create_draft_record(base_json_dereferenced)
        print(record)
        expected_record = PublishedThesisRecord.get_record(id_=record.id)
        assert record == expected_record

    def test_get_record_by_id_2(self):
        record = nusl_theses.get_record_by_id("dnusl", '411100')
        assert record is not None

    def test_delete_record(self, db):
        record = nusl_theses.get_record_by_id("dnusl", '411100')
        nusl_theses.delete_draft_record(record)
        db.session.commit()
        record2 = nusl_theses.get_record_by_id("dnusl", '411100')
        db.session.commit()
        assert record2 == {
            '$schema': 'https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-v1.0.0.json'
        }
