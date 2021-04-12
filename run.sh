#!/bin/bash

SCRIPT_DIR=$(dirname $0)

cd ${SCRIPT_DIR}
if [ ! -f ".env" ]; then
  echo "Properties file '.env' does not exists! It has to be created from '.env.template'."
  exit 1
fi

. .env

if [ ! -d "${DATA_DIR}" ]; then
  mkdir -p ${DATA_DIR}
  echo "Created 'data' directory: ${DATA_DIR}."
fi

DB_DIR=${DATA_DIR}/db/
if [ ! -d "${DB_DIR}" ]; then
  mkdir -p ${DB_DIR}
  echo "Created 'db' directory: ${DB_DIR}."
fi

docker-compose rm -s -f || true

docker-compose --project-name weather2db --env-file .env --log-level DEBUG up -d --remove-orphans --build

cd -