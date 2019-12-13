#/usr/bin/env bash

set -o xtrace

iperf --client 189.40.186.130 --time 60 --interval 1
