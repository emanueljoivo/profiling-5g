#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="$(date +%s)".tcp.csv

sudo netserver -L 189.40.186.130 -4 -p 5000 -D

mkdir -p data/

mv "${OUTPUT_FILE}" data/
