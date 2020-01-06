#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="tcp_upload_5gpro.csv"

iperf --server --interval 1 --reportstyle c | tee "${OUTPUT_FILE}"

mkdir -p data/

mv "${OUTPUT_FILE}" data/
