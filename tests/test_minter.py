from invenio_pidstore.models import PersistentIdentifier

from nr_theses.minters import nr_theses_id_minter
from tests.conftest import TestRecord


def test_nr_id_minter(app, db):
    data = {
        "title": "Test",
        "resourceType": [
            {
                "is_ancestor": False,
                "links": {
                    "self": "https://example.com/taxonomies/parent/bachelor-theses"
                }
            }
        ]
    }
    record = TestRecord.create(data=data)
    minted_id = nr_theses_id_minter(record_uuid=record.id, data=data)
    db.session.commit()
    pids = PersistentIdentifier.query.all()
    assert data["control_number"] == "1"
    assert pids[0].pid_value == "1"
    assert pids[0].pid_type == "nrthe"
