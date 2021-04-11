#!/bin/bash

SCRIPT_DIR=$(dirname $0)
. ${SCRIPT_DIR}/utilities.sh

cd ${SCRIPT_DIR}

if [ ! -d "${DATA_DIR}" ]; then
  mkdir -p ${DATA_DIR}
  echo "Created 'data' directory: ${DATA_DIR}."
fi

DB_DIR=${DATA_DIR}/db/
if [ ! -d "${DB_DIR}" ]; then
  mkdir -p ${DB_DIR}
  echo "Created 'db'directory: ${DB_DIR}."
fi

header "Stopping docker container(s) ..."
docker-compose rm -s -f || true

header "Starting docker container(s) ..."
docker-compose --project-name weather2db --env-file .env --log-level DEBUG up -d --remove-orphans --build
footer "Docker container(s) started."

cd -