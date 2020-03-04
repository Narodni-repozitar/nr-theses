from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import _records_state

from .utils import convert_dates


def test_json(app, thesis_metadata):
    print(app)
    print(current_jsonschemas.list_schemas())
    _records_state.validate(convert_dates(thesis_metadata),
                            "https://nusl.cz/schemas/invenio_nusl_theses/nusl-theses-v1.0.0.json")
