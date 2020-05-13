import pytest
from invenio_nusl_theses.api import ThesisAPI

from invenio_nusl_theses.proxies import nusl_theses


def test_import_oai_record(app, oai_record):
    print(nusl_theses.import_oai_record(oai_record))


def test_next_draft_id(app, db):
    theses = ThesisAPI(app)
    max = theses.max()
    print(max)


@pytest.fixture()
def oai_record():
    return {
        'contributor': [
            {
                'name': ['Kubíčková, Věra'],
                'role': {
                    '$ref': 'http://127.0.0.1:5000/api/taxonomies/contributor-type/advisor/'
                }
            },
            {
                'name': ['Hronzová, Marie'],
                'role': {
                    '$ref': 'http://127.0.0.1:5000/api/taxonomies/contributor-type/referee/'
                }
            }
        ],
        'creator': [
            {'name': 'Smolková, Lenka'}
        ],
        'identifier': [
            {
                'type': 'originalRecord',
                'value': 'http://hdl.handle.net/20.500.11956/2623'
            },
            {
                'value': 'oai:dspace.cuni.cz:20.500.11956/2623',
                'type': 'originalOAI'
            }
        ],
        'abstract': [
            {
                'value': 'Ze života lidí se stále vytrácí přirozený pohyb. Vymoženosti '
                         'současné společnosti ( televize, počítače...) tyto trendy '
                         'návyku snížené potřeby pohybu jen podporují. &quot;Změnil se '
                         'charakter, zaměření, účel a cíl pohybových aktivit, '
                         'došlo kjejich značné diferenciaci a disproporci mezi aktivními '
                         'a pasivními účastníky. Objevují se nepřiměřené emoce až '
                         'hysterie v souvislosti se sportovními akcemi, uctívání '
                         'silnějších, dravějších, případně i bohatších.&quot; (9) Je '
                         'nezbytné, aby tělesná zdatnost a její význam byla vnímána '
                         'lidmi jako důležitá životní hodnota. Vždyť přiměřeně tělesně '
                         'zdatný člověk, navíc pohybově kultivovaný, se v praktickém '
                         'životě spolu s mravními postoji a vzdělaností přibližuje k '
                         'ideálu všestranně rozvinutého člověka. V lidském životě hraje '
                         'nejvýznamnější období pro účinný tělesný a pohybový rozvoj '
                         'školní věk. Právě v dětském věku je podpůrně pohybový systém '
                         'velmi citlivý na nepřiměřenou strukturu tělesné zátěže a '
                         'nedostatek pohybové aktivity. Nelze přehlédnout, že značný '
                         'počet dětí projevuje nízkou tělesnou zdatnost a také '
                         'nedostatečné zvládnutí pro život důležitých pohybových '
                         'dovedností. Kolisko uvádí (7, str.5), že 20% dětí předškolního '
                         'věku trpí vadným držením těla a v období 11-12 let je tento '
                         'stav téměř trojnásobný.',
                'lang': 'cze'
            }, {
                'value': 'Ze života lidí se stále vytrácí přirozený pohyb. Vymoženosti '
                         'současné společnosti ( televize, počítače...) tyto trendy '
                         'návyku snížené potřeby pohybu jen podporují. &quot;Změnil se '
                         'charakter, zaměření, účel a cíl pohybových aktivit, '
                         'došlo kjejich značné diferenciaci a disproporci mezi aktivními '
                         'a pasivními účastníky. Objevují se nepřiměřené emoce až '
                         'hysterie v souvislosti se sportovními akcemi, uctívání '
                         'silnějších, dravějších, případně i bohatších.&quot; (9) Je '
                         'nezbytné, aby tělesná zdatnost a její význam byla vnímána '
                         'lidmi jako důležitá životní hodnota. Vždyť přiměřeně tělesně '
                         'zdatný člověk, navíc pohybově kultivovaný, se v praktickém '
                         'životě spolu s mravními postoji a vzdělaností přibližuje k '
                         'ideálu všestranně rozvinutého člověka. V lidském životě hraje '
                         'nejvýznamnější období pro účinný tělesný a pohybový rozvoj '
                         'školní věk. Právě v dětském věku je podpůrně pohybový systém '
                         'velmi citlivý na nepřiměřenou strukturu tělesné zátěže a '
                         'nedostatek pohybové aktivity. Nelze přehlédnout, že značný '
                         'počet dětí projevuje nízkou tělesnou zdatnost a také '
                         'nedostatečné zvládnutí pro život důležitých pohybových '
                         'dovedností. Kolisko uvádí (7, str.5), že 20% dětí předškolního '
                         'věku trpí vadným držením těla a v období 11-12 let je tento '
                         'stav téměř trojnásobný.',
                'lang': 'eng'
            }],
        'language': [{'$ref': 'http://127.0.0.1:5000/api/taxonomies/languages/cze/'}], 'title': [{
            'name': 'Zdravotní tělesná výchova na základních školách v Plzni a okolí',
            'lang': 'cze'
        },
            {
                'value': 'Physical Education at Basic Schools in Pilsen and the Surrounding Areas',
                'lang': 'eng'
            }],
        'doctype': {'$ref': 'http://127.0.0.1:5000/api/taxonomies/doctypes/diplomove_prace/'},
        'dateAccepted': '2006-01-17', 'studyField': [{
            '$ref': 'http://127.0.0.1:5000/api/taxonomies/studyfields/O_ucitelstvi-pro-1-stupen'
                    '-zakladni-skoly/'
        }], 'defended': True, 'degreeGrantor': [
            {'$ref': 'http://127.0.0.1:5000/api/taxonomies/institutions/katedra-telesne-vychovy/'}],
        'provider': {'$ref': 'https://localhost:5000/api/taxonomies/institutions/00216208'},
        'accessRights': {'$ref': 'https://localhost:5000/api/taxonomies/accessRights/c_abf2'},
        'accessibility': [{'lang': 'cze', 'value': 'Dostupné v digitálním repozitáři UK.'}, {
            'lang': 'eng', 'value': 'Available in the Charles University Digital Repository.'
        }]
    }
