from invenio_db import db
from invenio_explicit_acls.record import SchemaEnforcingRecord
from invenio_indexer.api import RecordIndexer
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier
from invenio_search import RecordsSearch
from sqlalchemy.orm.exc import NoResultFound
from invenio_records.api import _records_state


class ThesisRecord(SchemaEnforcingRecord):
    STAGING_SCHEMA = 'invenio_nusl_theses/nusl-theses-staging-v1.0.0.json'
    PUBLISHED_SCHEMA = 'invenio_nusl_theses/nusl-theses-v1.0.0.json'
    ALLOWED_SCHEMAS = (STAGING_SCHEMA,
                       PUBLISHED_SCHEMA,)
    PREFERRED_SCHEMA = STAGING_SCHEMA


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

    def validate(self, schema, transformed, json_schema):
        marshmallowed = schema.load(transformed).data
        marshmallowed = schema.dump(marshmallowed).data
        _records_state.validate(marshmallowed,
                                json_schema)

        return marshmallowed

    def import_record(self, record):
        # validate json schema and save
        with db.session.begin_nested():
            existing_record = None
            try:
                existing_pid = PersistentIdentifier.get('nusl', record['id'])
                try:
                    existing_record = ThesisRecord.get_record(id_=existing_pid.object_uuid)
                except NoResultFound:
                    # check it if has not been deleted and salvage if so
                    existing_record = ThesisRecord.get_record(id_=existing_pid.object_uuid, with_deleted=True)
                    existing_record = existing_record.revert(-1)
            except PIDDoesNotExistError:
                pass
            except NoResultFound:
                pass

            if not existing_record:
                db_record = ThesisRecord.create(record)  # Zde dochází i k validaci přes signály z ext
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
