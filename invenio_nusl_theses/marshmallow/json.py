# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

import csv
import functools
import os

from invenio_nusl_common.marshmallow_utils import marshmallow_remove_required
from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, validate, ValidationError, pre_load, post_load
from pycountry import languages, countries

from invenio_nusl_common.marshmallow import MultilanguageSchemaV1, ValueTypeSchemaV1
from invenio_nusl_common.marshmallow.json import DoctypeSubSchemaV1
from invenio_nusl_theses.marshmallow.data.fields_dict import FIELDS


########################################################################
#                 IMPORT VALIDATION DATA                               #
########################################################################


@functools.lru_cache()
def import_csv(file: str, start: int, end: int):
    path = os.path.dirname(__file__)
    path += f"/data/{file}"
    file = open(path, "r")
    reader = csv.reader(file)
    columns = []
    for col in range(start, end):
        columns.append([])
    for r in reader:
        i = 0
        for col in range(start, end):
            columns[i].append(r[col])
            i += 1
    file.close()
    return columns


########################################################################
#                 VALIDATION MODELS                                    #
########################################################################
def validate_language(language):
    language = language.lower()
    alpha3 = languages.get(alpha_3=language)
    bib = languages.get(bibliographic=language)
    if alpha3 is None and bib is None:
        raise ValidationError('The language code is not part of ISO-639 codes.')


def validate_country(country):
    country = country.upper()
    alpha2 = countries.get(alpha_2=country)
    if alpha2 is None:
        raise ValidationError('The country code is not part of ISO-3166 codes.')


def validate_programme_code(code):
    if code not in import_csv("programme.csv", 0, 2)[0]:
        raise ValidationError('The study programme code is not valid')


def validate_field_code(code):
    if code not in import_csv("field.csv", 0, 2)[0]:
        raise ValidationError('The study field code is not valid')


def validate_programme_name(name):
    if name not in import_csv("programme.csv", 0, 2)[1]:
        raise ValidationError('The study programme name is not valid')


def validate_field_name(name):
    if name not in import_csv("field.csv", 0, 2)[1]:
        if not os.path.exists('/tmp/import-nusl-theses'):
            os.makedirs('/tmp/import-nusl-theses')
        with open("/tmp/import-nusl-theses/wrong_fields.txt", "a") as fp:
            fp.write(f"{name}\n")
        raise ValidationError('The study field name is not valid')


#########################################################################
#                      Sub-schemas                                      #
#########################################################################
class CCMetadataSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(required=True, validate=validate.OneOf(["CC BY",
                                                                    "CC BY-NC",
                                                                    "CC BY-SA",
                                                                    "CC BY-ND",
                                                                    "CC BY-NC-SA",
                                                                    "CC BY-NC-ND"]))
    version = SanitizedUnicode(required=True, validate=validate.Regexp(r"\d.\d"))
    country = SanitizedUnicode(required=True, validate=validate_country)

    @pre_load
    def country_code(self, data):
        if "country" in data:
            country = data["country"]
            if countries.get(alpha_3=country.upper()):
                country = countries.get(alpha_3=country.upper())
            elif countries.get(alpha_2=country.upper()):
                country = countries.get(alpha_2=country.upper())
            elif countries.get(name=country):
                country = countries.get(name=country)
            elif countries.get(official_name=country):
                country = countries.get(official_name=country)
            else:
                country = None
            if country is not None:
                data["country"] = country.alpha_2
        return data


class RightsMetadataSchemaV1(StrictKeysMixin):
    CC = fields.Nested(CCMetadataSchemaV1)
    copyright = fields.List(Nested(MultilanguageSchemaV1))


class SubjectMetadataSchemaV1(StrictKeysMixin):
    name = fields.List(Nested(MultilanguageSchemaV1))
    taxonomy = SanitizedUnicode(validate=validate.OneOf(["czenas",
                                                         "mesh",
                                                         "czmesh",
                                                         "eurovoc",
                                                         "psh",
                                                         "ctt",
                                                         "pedag",
                                                         "agroterm",
                                                         "agrovoc",
                                                         "mednas",
                                                         "phffuk",
                                                         "ph",
                                                         "lcsh"]))
    id = SanitizedUnicode()  # TODO: Dodělat MEDNAS: http://www.medvik.cz/link/nlk20040148348; http://www.medvik.cz/link/ + id z nušl

    @pre_load()
    def lower_taxonomy(self, data):
        if "taxonomy" in data:
            taxonomy = data["taxonomy"]
            data["taxonomy"] = taxonomy.lower()
            return data


class CreatorSubSchemaV1(StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    id = Nested(ValueTypeSchemaV1)


class ContributorSubSchemaV1(CreatorSubSchemaV1):
    role = SanitizedUnicode(required=True)


class ProgrammeSubSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(validate=validate_programme_code)
    name = SanitizedUnicode(validate=validate_programme_name)



    @pre_load()
    def standardize_name(self, data):
        STUDY_PROGRAMME = {
            'Zootechnics': "Zootechnika",
            'Hudebního umění': 'Hudební umění',
            'Biochemistry': "Biochemie",
            'Biology': "Biologie",
            "Applied Informatics": "Aplikovaná informatika",
            'Economics and Management': "Ekonomika a management",
            'Teorie filmové a multimediální tvorby': 'Teorie a praxe audiovizuální tvorby',
            'Botany': 'Botanika',
            'Physiology and Immunology': 'Fyziologie a imunologie',
            'Molecular and Cell Biology': "Molekulární a buněčná biologie",
            "Finance a účetnictví": "Finance a účetnictví"
        }

        if "name" in data:
            data["name"] = STUDY_PROGRAMME.get(data["name"], data["name"])

    @post_load()
    def validate_code_name_fit(self, data):  # TODO: Dát do jednoho společného kódu
        if data.get("code") and data.get("name"):
            codes_names = import_csv("programme.csv", 0, 2)
            programme_code = data["code"]
            programme_name = data["name"]
            code_index = codes_names[0].index(programme_code)
            if codes_names[1][code_index] != programme_name:
                raise ValidationError("The code does not match the program name.")


class FieldSubSchemaV1(StrictKeysMixin):
    code = SanitizedUnicode(validate=validate_field_code)
    name = SanitizedUnicode(validate=validate_field_name)

    @pre_load()
    def standardize_name(self, data):
        if "name" in data:
            data["name"] = FIELDS.get(data["name"], data["name"])

    @post_load()
    def validate_code_name_fit(self, data):  # TODO: Dát do jednoho společného kódu
        if ("name" in data) and ("code" not in data):
            codes_names = import_csv("field.csv", 0, 2)
            index = codes_names[1].index(data["name"])
            code = codes_names[0][index]
            data["code"] = code
            return data

        if data.get("code") and data.get("name"):
            codes_names = import_csv("field.csv", 0, 2)
            programme_code = data["code"]
            programme_name = data["name"]
            code_index = codes_names[0].index(programme_code)
            if codes_names[1][code_index] != programme_name:
                raise ValidationError("The code does not match the field name.")


class FacultySubSchemaV1(StrictKeysMixin):
    name = fields.List(Nested(MultilanguageSchemaV1))
    departments = fields.List(Nested(MultilanguageSchemaV1), allow_none=True)


class UniversitySubSchemaV1(StrictKeysMixin):
    name = fields.List(Nested(MultilanguageSchemaV1))
    faculties = fields.List(Nested(FacultySubSchemaV1))

    @pre_load()
    def standardize_name(self, data):
        FACULTIES = {
            "Filmová a televizní fakulta AMU": "Filmová a televizní fakulta",
            "Divadelní fakulta AMU": "Divadelní fakulta",
            "Hudební a taneční fakulta AMU": "Hudební a taneční fakulta",
            "Hudební fakulta AMU": "Hudební fakulta",
            "Stavební fakulta": "Fakulta stavební"
        }
        if "faculties" in data:
            faculties = []
            for faculty in data["faculties"]:
                names = []
                for fac_name in faculty["name"]:
                    fac_name["name"] = FACULTIES.get(fac_name["name"], fac_name["name"])
                    names.append(fac_name)
                faculty["name"] = names
                faculties.append(faculty)
            data["faculties"] = faculties
        return data


class DegreeGrantorSubSchemaV1(StrictKeysMixin):
    university = Nested(UniversitySubSchemaV1, required=True)

    @pre_load()
    def standardize_name(self, data):
        UNIVERSITIES = {
            "Mendelova univerzita": "Mendelova univerzita v Brně",
            "Mendelova zemědělská a lesnická univerzita": "Mendelova univerzita v Brně",
            "Vysoká škola zemědělská v Brně": "Mendelova univerzita v Brně",
            "Vysoká škola zemědělská a lesnická v Brně": "Mendelova univerzita v Brně",
            "Mendelova univerzita (Brno)": "Mendelova univerzita v Brně"
        }
        names = []
        for uni_name in data["university"]["name"]:
            uni_name["name"] = UNIVERSITIES.get(uni_name["name"], uni_name["name"])
            names.append(uni_name)
        data["university"]["name"] = names
        return data

    @post_load()
    def validate_university_name(self, data):
        for uni_name in data["university"]["name"]:
            if uni_name["lang"] == "cze":
                imported_data = import_csv("universities.csv", 0, 1)[0]
                universities = [university.lower() for university in imported_data]
                name = uni_name["name"].lower()
                if name not in universities:
                    raise ValidationError("The University name is not valid")

    @post_load()
    def validate_faculty_name(self, data):
        if "faculties" in data["university"]:
            for faculty in data["university"]["faculties"]:
                for fac_name in faculty["name"]:
                    if fac_name["lang"] == "cze":
                        imported_data = import_csv("faculties.csv", 0, 1)[0]
                        if fac_name["name"] not in imported_data:
                            raise ValidationError("The Faculty name is not valid")


#########################################################################
#                     Main schema                                       #
#########################################################################
class ThesisMetadataSchemaV1(StrictKeysMixin):  # modifikace
    """Schema for the record metadata."""

    id = fields.Integer(required=True)
    language = fields.List(SanitizedUnicode(required=True,
                                            validate=validate_language), required=True)
    identifier = fields.List(Nested(ValueTypeSchemaV1), required=True)  # TODO: Dodělat validaci na type
    dateAccepted = fields.Date(required=True)
    modified = fields.DateTime()
    title = fields.List(Nested(MultilanguageSchemaV1), required=True)
    extent = SanitizedUnicode()
    abstract = fields.List(Nested(MultilanguageSchemaV1))
    rights = fields.Nested(RightsMetadataSchemaV1)
    subject = fields.List(Nested(SubjectMetadataSchemaV1))  # TODO: udělat required
    creator = fields.List(Nested(CreatorSubSchemaV1), required=True)
    contributor = fields.List(Nested(ContributorSubSchemaV1))
    doctype = Nested((DoctypeSubSchemaV1), required=True)
    subtitle = fields.List(Nested(MultilanguageSchemaV1))
    note = fields.List(SanitizedUnicode())
    accessibility = fields.List(Nested(MultilanguageSchemaV1))
    accessRights = SanitizedUnicode(validate=validate.OneOf(["open", "embargoed", "restricted", "metadata_only"]))
    provider = SanitizedUnicode()  # TODO: dodělat validaci na providera viz csv v NUSL_schemas
    defended = fields.Boolean()
    studyProgramme = Nested(ProgrammeSubSchemaV1)
    studyField = Nested(FieldSubSchemaV1)
    degreeGrantor = fields.List(Nested(DegreeGrantorSubSchemaV1), required=True)


class ThesisRecordSchemaV1(StrictKeysMixin):  # get - zobrazit
    """Record schema."""

    metadata = fields.Nested(ThesisMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()


ThesisMetadataStagingSchemaV1 = marshmallow_remove_required(ThesisMetadataSchemaV1)
ThesisRecordStagingSchemaV1 = marshmallow_remove_required(ThesisRecordSchemaV1)
