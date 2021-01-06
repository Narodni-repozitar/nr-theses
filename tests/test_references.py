import uuid

from oarepo_references.models import RecordReference

from nr_theses.record import PublishedThesisRecord


def test_save_references(app, db, taxonomy_tree, base_json):
    record_uuid = uuid.uuid4()
    record = PublishedThesisRecord.create(base_json, id_=record_uuid)

    db.session.commit()
    references = RecordReference.query.all()
    assert len(references) != 0
