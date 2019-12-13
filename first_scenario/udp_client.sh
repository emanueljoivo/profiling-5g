#!/usr/bin/env bash

set -o xtrace

iperf --client 189.40.186.130 --enhanced \
  --udp --tradeoff --bandwidth 1200M --time 60 --interval 1
