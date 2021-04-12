#!/bin/bash

SCRIPT_DIR=$(dirname $0)

cd ${SCRIPT_DIR}

docker-compose rm -s -f || true

DATA_DIR=${PWD}/data.tests
if [ -d "${DATA_DIR}" ]; then
  rm -rf ${DATA_DIR}
  echo "Removed old 'data' directory: ${DATA_DIR}."
fi
mkdir -p ${DATA_DIR}
echo "Created 'data' directory: ${DATA_DIR}."
DB_DIR=${DATA_DIR}/db/
mkdir -p ${DB_DIR}
echo "Created 'db' directory: ${DB_DIR}."

cp .env.tests .env.tests.work
echo "DATA_DIR=${DATA_DIR}" >> .env.tests.work
. .env.tests.work

docker-compose --project-name weather2db --env-file .env.tests.work --log-level DEBUG up -d --remove-orphans --build

sleep 30

python scripts/tests/db_checks.py
ret=$?

if [ $ret -ne 0 ]; then
  exit 1
fi

rm .env.tests.work

cd -
