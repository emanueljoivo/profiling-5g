#/usr/bin/env bash

set -o xtrace

sudo netperf -H 189.40.186.130 -p 5000 -t TCP_STREAM -- -m 32
