#!/bin/bash

SCRIPT_DIR=$(dirname $0)

cd ${SCRIPT_DIR}
. .env

python scripts/collect_data.py

cd -