import sqlalchemy as db
import logging

# Logging config
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
# CONNECT TO DATABASE
engine = db.create_engine('postgresql://oarepo:oarepo@localhost:5432/oarepo')
connection = engine.connect()
# Load tables
metadata = db.MetaData()
metadata.reflect(bind=engine)
table = metadata.tables["records_metadata"]

# Load old data
old_data = engine.execute(
    """SELECT * FROM records_metadata WHERE json -> 'invenio_draft_validation' -> 'errors' -> 'marshmallow' @> '[{"field": "studyField", "message": "Studyfield is not valid."}]'""")

# Fix old data
for record in old_data:
    id_ = record[2]
    json = record[3]

    if "studyField" in json:
        del json["studyField"]

    stmt = table.update().where(table.c.id == str(id_)).values(json=json)
    connection.execute(stmt)
    logging.info(f'Record with id: {id_} was updated')

connection.close()

# one = result.fetchone()[3]
