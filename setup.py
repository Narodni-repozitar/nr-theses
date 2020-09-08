# -*- coding: utf-8 -*-


"""NUSL theses data model."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    # 'check-manifest>=0.25',
    # 'coverage>=4.0',
    # 'isort>=4.3.3',
    # 'mock>=2.0.0',
    # 'pydocstyle>=1.0.0',
    # 'pytest-cache>=1.0',
    # 'pytest-invenio>=1.0.2,<1.1.0',
    # 'pytest-mock>=1.6.0',
    # 'pytest-cov>=1.8.0',
    # 'pytest-random-order>=0.5.4',
    # 'pytest-pep8>=1.0.6',
    # 'pytest>=2.8.0',
    # 'selenium>=3.4.3',
    'oarepo>=3.3.0.4, <3.4.0.0',
    'pytest>=6.0.0, <7.0.0'
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    "oarepo-records-draft>=5.0.0a7, <6.0.0",
    "oarepo-validate>=1.2.8, <2.0.0",
    "oarepo-references>=1.8.1 <2.0.0"
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_nusl_theses', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-nusl-theses',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='nusl Invenio theses',
    license='MIT',
    author='Daniel Kopecký',
    author_email='Daniel.Kopecky@techlib.cz',
    url='',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'theses = invenio_nusl_theses:InvenioNUSLTheses',
        ],
        'invenio_base.api_apps': [
            'theses = invenio_nusl_theses:InvenioNUSLTheses',
        ],
        'console_scripts': [
        ],
        'invenio_base.blueprints': [
        ],
        'invenio_config.module': [
        ],
        'invenio_i18n.translations': [
        ],
        'invenio_jsonschemas.schemas': [
            'invenio_nusl_theses = invenio_nusl_theses.jsonschemas'
        ],
        'invenio_search.mappings': [
            'invenio_nusl_theses =invenio_nusl_theses.mappings'
        ],
        'invenio_oarepo_mapping_includes': [
            'invenio_nusl_theses=invenio_nusl_theses.included_mappings'
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Planning',
    ],
)
