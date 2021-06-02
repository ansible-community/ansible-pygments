#!/bin/bash
set -e
poetry run pylint --rcfile .pylintrc.automated src/ansible_pygments/ "$@"
