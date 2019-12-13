#/usr/bin/env bash

set -o xtrace

# the test will execute for ten minutes
iperf --client 189.40.186.130 --time 600 --interval 1
