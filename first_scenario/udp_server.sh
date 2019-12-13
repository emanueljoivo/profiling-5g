#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="$(date +%s)".udp.csv

iperf --server --enhanced --udp | tee "${OUTPUT_FILE}"

mv "${OUTPUT_FILE}" data/
