import uuid

import flask
from flask import current_app
from flask_principal import Identity, identity_changed
from invenio_access import authenticated_user
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier, PIDStatus
from invenio_records import Record
from sqlalchemy.orm.exc import NoResultFound

from nr_theses.record import PublishedThesisRecord


def set_identity(u):
    """Sets identity in flask.g to the user."""
    identity = Identity(u.id)
    identity.provides.add(authenticated_user)
    identity_changed.send(current_app._get_current_object(), identity=identity)
    assert flask.g.identity.id == u.id


def login(http_client, user):
    """Calls test login endpoint to log user."""
    resp = http_client.get(f'/test/login/{user.id}')
    assert resp.status_code == 200


def create_draft_record(record: dict, pid_type=None, pid_value=None):
    if not pid_type:
        pid_type = "dnr"
    if not pid_value:
        pid_value = record["control_number"]
    id_ = uuid.uuid4()
    pid = PersistentIdentifier.create(
        pid_type,
        pid_value,
        pid_provider=None,
        object_type="rec",
        object_uuid=id_,
        status=PIDStatus.REGISTERED,
    )
    db_record = PublishedThesisRecord.create(record, id_=id_)
    return db_record


def delete_draft_record(record: Record):
    record.delete()


def get_record_by_id(pid_type, pid_value):
    try:
        existing_pid = PersistentIdentifier.get(pid_type, pid_value)
        try:
            existing_record = PublishedThesisRecord.get_record(id_=existing_pid.object_uuid)
        except NoResultFound:
            # check it if has not been deleted and salvage if so
            existing_record = PublishedThesisRecord.get_record(id_=existing_pid.object_uuid,
                                                               with_deleted=True)
            existing_record = existing_record.revert(-1)
    except PIDDoesNotExistError:
        return
    except NoResultFound:  # pragma: no cover
        return
    return existing_record
