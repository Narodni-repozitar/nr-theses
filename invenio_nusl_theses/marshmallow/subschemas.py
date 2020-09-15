from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow.fields import List


class StudyFieldMixin(StrictKeysMixin):
    AKVO = SanitizedUnicode
    aliases = List(SanitizedUnicode())
