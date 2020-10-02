# Invenio Nusl Theses

[![Build Status](https://travis-ci.org/Narodni-repozitar/invenio-nusl-theses.svg?branch=master)](https://travis-ci.org/Narodni-repozitar/invenio-nusl-theses)

[![Coverage Status](https://coveralls.io/repos/github/Narodni-repozitar/invenio-nusl-theses/badge.svg?branch=master)](https://coveralls.io/github/Narodni-repozitar/invenio-nusl-theses?branch=master)


Disclaimer: The library is part of the Czech National Repository, and therefore the README is written in Czech.
General libraries extending [Invenio](https://github.com/inveniosoftware) are concentrated under the [Oarepo
 namespace](https://github.com/oarepo).

  ## Instalace

 Nejedná se o samostatně funkční knihovnu, proto potřebuje běžící Invenio a závislosti Oarepo.
 Knihovna se instaluje ze zdroje.

 ```bash
git clone git@github.com:Narodni-repozitar/invenio-nusl-theses.git
cd invenio-nusl-common
pip install poetry
poetry install
```

Pro testování a/nebo samostané fungování knihovny je nutné instalovat tests z extras.

```bash
poetry install --extras tests
```

:warning: Pro instalaci se používá Manažer závilostí **Poetry** více infromací lze naleznout v
[dokumentaci](https://python-poetry.org/docs/)

## Účel

Knihovna rozšiřuje [obecný metadatový model](https://github.com/Narodni-repozitar/invenio-nusl-common)
o pole pro vysokoškolské závěrečné práce. Vysokoškolským pracím je přiřazen endpoint **/api/theses**. Knihovna
poskytuje API pro CRUD operace pod proxy **nusl_these**.

## Použití

Bude dopsáno.
