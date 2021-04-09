import pytest

from tests.helpers import create_draft_record


@pytest.mark.usefixtures("app", "db", "taxonomy_tree", "base_json", "base_json_dereferenced")
class TestRecord:
    def test_canonical_url(self, app, db, base_json_dereferenced):
        record = create_draft_record(base_json_dereferenced)
        with app.app_context():
            assert record.canonical_url == "http://127.0.0.1:5000/nr/theses/411100"
