#!/bin/sh
set -e
poetry run python -W 'ignore:"@coroutine" decorator is deprecated::asynctest.case' \
	-m pytest --cov-branch --cov=sphinx_ansible_highlighter --cov-report term-missing -vv tests "$@"
