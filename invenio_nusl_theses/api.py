from invenio_explicit_acls.record import SchemaEnforcingRecord


class ThesisRecord(SchemaEnforcingRecord):
    ALLOWED_SCHEMAS = ('invenio_nusl_theses/nusl-theses-staging-v1.0.0.json',
                       'invenio_nusl_theses/nusl-theses-v1.0.0.json',)
    PREFERRED_SCHEMA = 'invenio_nusl_theses/nusl-theses-staging-v1.0.0.json'
