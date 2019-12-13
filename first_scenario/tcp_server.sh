#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="$(date +%s)".tcp.csv

iperf --server --enhanced --interval 0.5 | tee "${OUTPUT_FILE}"

mkdir -p data/

mv "${OUTPUT_FILE}" data/
