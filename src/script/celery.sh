#!/bin/bash

PROC_NUM="$(getconf _NPROCESSORS_ONLN)"
celery -A scheduler.celery worker -l info -c "$PROC_NUM" --beat -E
