#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="$(date +%s)".tcp.csv

iperf --server --enhanced | tee "${OUTPUT_FILE}"

mv "${OUTPUT_FILE}" data/
