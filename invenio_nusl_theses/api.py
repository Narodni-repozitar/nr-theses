import uuid

from invenio_db import db
from invenio_indexer.api import RecordIndexer
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier
from invenio_search import RecordsSearch
from sqlalchemy.orm.exc import NoResultFound

from invenio_nusl_common.minters import nusl_id_minter
from invenio_nusl_theses.record import DraftThesisRecord
from invenio_pidstore.models import PIDStatus


class ThesisSearch(RecordsSearch):
    pass


class ThesisAPI:

    def __init__(self, app):
        """
        API initialization.

        :param app: invenio application
        """
        self.app = app
        self.indexer = RecordIndexer()

    def validate(self, schema, transformed):
        schema = schema()
        marshmallowed = schema.load(transformed).data
        marshmallowed = schema.dump(marshmallowed).data
        draft_thesis_record = DraftThesisRecord(marshmallowed)
        draft_thesis_record.validate()

        return marshmallowed

    def import_old_nusl_record(self, record):
        # validate json schema and save
        with db.session.begin_nested():
            existing_record = None
            try:
                existing_pid = PersistentIdentifier.get('nusl', record['id'])
                try:
                    existing_record = DraftThesisRecord.get_record(id_=existing_pid.object_uuid)
                except NoResultFound:
                    # check it if has not been deleted and salvage if so
                    existing_record = DraftThesisRecord.get_record(id_=existing_pid.object_uuid, with_deleted=True)
                    existing_record = existing_record.revert(-1)
            except PIDDoesNotExistError:
                pass
            except NoResultFound:
                pass

            if not existing_record:
                id = uuid.uuid4()
                pid = PersistentIdentifier.create(
                    "dnusl",
                    record["id"],
                    pid_provider=None,
                    object_type="rec",
                    object_uuid=id,
                    status=PIDStatus.REGISTERED,
                )
                db_record = DraftThesisRecord.create(record, id_=id)  # Zde dochází i k validaci přes signály z ext
            else:
                # remove everything from the record except of id and pid - keep them
                previous_id = existing_record['id']
                previous_identifier = existing_record['identifier']
                existing_record.clear()
                existing_record['id'] = previous_id
                existing_record['identifier'] = previous_identifier

                for k, v in record.items():
                    existing_record[k] = v
                existing_record.commit()
                db_record = existing_record

        db.session.commit()
        self.indexer.index(db_record)
