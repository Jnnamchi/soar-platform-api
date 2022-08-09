#!/bin/bash

PROC_NUM="$(getconf _NPROCESSORS_ONLN)"
THREADS=$(($PROC_NUM * 2))

uwsgi --http 0.0.0.0:5000 --master -p "$THREADS" -w  app:app