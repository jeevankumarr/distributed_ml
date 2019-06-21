#!/usr/bin/env bash

# remove all __pycache__ directories
# find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
echo 'Deleting all __pycache__, *.pyc, *.pyo'
python3 -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
python3 -c "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

# run the tests
echo 'Running tests'
pytest -s tests/

# generate a coverage report
echo 'Generating coverage report'
pytest -s --cov=src/roulette --cov-report term-missing tests/
