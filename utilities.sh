#!/bin/bash

set -eou pipefail

SCRIPT_DIR=$(dirname $0)

NO_FORMAT='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'

. .env

is_mac_os() { $([[ "$(uname -s)" = "Darwin" ]]) ;}

die() {
    fail "***** ERROR: $1" 1>&2

    if [[ -n "${2}" ]]; then
        exit_code=${2}
    else
        exit_code=1
    fi
    exit ${exit_code}
}

warn() {
    echo "**** WARNING: $*" 1>&2
    exit 0
}

function defaultString {
  if [ -z "${1}" ]; then
    echo "$2"
  else
    echo "$1"
  fi
}

function header {
  echo ""
  echo "****************************************"
  echo ${1}
  echo "----------------------------------------"
}

function footer {
  echo "----------------------------------------"
  echo ${1}
  echo "****************************************"
}

function fail {
  MESSAGE=$(defaultString "$1" "FAIL")
  echo -e "${RED}${MESSAGE}${NO_FORMAT}"
}

function pass {
  MESSAGE=$(defaultString "$1" "PASS")
  echo -e "${GREEN}${MESSAGE}${NO_FORMAT}"
}

if is_mac_os ; then
  echo "MacOS"
  SED_APP_I="sed -i ''"
else
  SED_APP_I="sed -i"
fi
