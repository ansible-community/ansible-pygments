#!/bin/bash
set -e
poetry run pylint src/ "$@"
