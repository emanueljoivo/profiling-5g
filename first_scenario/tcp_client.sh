#/usr/bin/env bash

set -o xtrace

OUTPUT_FILE=tcp_download-mi-5g-pro-16032020.csv

# the test will execute for ten minutes
iperf --client 189.40.186.4 --time 300 --interval 1 --reportstyle C --output "${OUTPUT_FILE}"
