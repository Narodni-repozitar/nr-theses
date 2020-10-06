from pprint import pprint

import pytest
from nr_theses.record import PublishedThesisRecord

from nr_theses.proxies import nr_theses


@pytest.mark.usefixtures("app", "db", "taxonomy_tree", "base_json", "base_json_dereferenced")
class TestAPI:
    # def test_import_old_nusl_record(self, app, db, taxonomy_tree, base_json,
    #                                 base_json_dereferenced):
    #     nusl_theses.import_old_nusl_record(base_json_dereferenced)

    def test_get_record_by_id(self):
        assert nr_theses.get_record_by_id("dnr", "1") is None

    def test_create_draft_record(self, base_json_dereferenced):
        record = nr_theses.create_draft_record(base_json_dereferenced)
        print(record)
        expected_record = PublishedThesisRecord.get_record(id_=record.id)
        assert record == expected_record

    def test_get_record_by_id_2(self):
        record = nr_theses.get_record_by_id("dnr", '411100')
        assert record is not None

    def test_delete_record(self, db):
        record = nr_theses.get_record_by_id("dnr", '411100')
        nr_theses.delete_draft_record(record)
        db.session.commit()
        record2 = nr_theses.get_record_by_id("dnr", '411100')
        db.session.commit()
        assert record2 == {
            '$schema': 'https://nusl.cz/schemas/nr_theses/nr-theses-v1.0.0.json'
        }
