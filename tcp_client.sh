#/usr/bin/env bash

set -o errexit

iperf --client 189.40.186.130 --tradeoff --time 60 --interval 1

