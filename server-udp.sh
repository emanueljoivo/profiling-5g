#!/usr/bin/env bash

set -o errexit

NOW=$(date | awk -F ' ' '{print $4}')

iperf --server --enhanced --udp | tee udp."${NOW}".out
