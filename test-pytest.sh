#!/bin/sh
set -e
poetry run python -m pytest --cov-branch --cov=src/ --cov-report term-missing -vv tests "$@"
