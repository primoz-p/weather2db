#!/bin/bash

SCRIPT_DIR=$(dirname $0)

cd ${SCRIPT_DIR}/
. .env

python scripts/tests/tests.py

cd -