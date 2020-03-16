#!/usr/bin/env bash

set -o xtrace

OUTPUT_FILE="tcp_download-mi-5g-pro-16032020.csv"

iperf --server -r --interval 1 --reportstyle c | tee "${OUTPUT_FILE}"

mkdir -p data/

mv "${OUTPUT_FILE}" data/
