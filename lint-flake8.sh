#!/bin/bash
set -e
poetry run flake8 src/ --count --max-complexity=10 --max-line-length=100 --statistics "$@"
