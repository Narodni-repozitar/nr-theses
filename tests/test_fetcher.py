from nr_theses.fetchers import nr_theses_id_fetcher
from tests.conftest import TestRecord


def test_nr_id_fetcher(app, db):
    id_field = "control_number"
    data = {
        "title": "Test",
        id_field: "1"
    }
    record = TestRecord.create(data=data)
    fetched_id = nr_theses_id_fetcher(record_uuid=record.id, data=data)
    assert fetched_id.pid_type == "nrthe"
    assert str(fetched_id.pid_value) == str(data[id_field])
