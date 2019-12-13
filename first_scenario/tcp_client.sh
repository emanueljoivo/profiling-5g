#/usr/bin/env bash

set -o xtrace

iperf --client 189.40.186.130 --tradeoff --time 60 --interval 1
