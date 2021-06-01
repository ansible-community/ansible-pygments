#!/bin/sh
set -e
poetry run python -m pytest --cov-branch --cov=sphinx_ansible_highlighter --cov-report term-missing -vv tests "$@"
