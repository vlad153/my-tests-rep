#!/usr/bin/env sh

. "$(dirname $0)"/read_env_file.sh $1

poetry run uvicorn src.main:app --host ${HOST} --port ${PORT} --reload
