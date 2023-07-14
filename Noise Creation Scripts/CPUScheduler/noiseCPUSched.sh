#!/bin/bash

python3 primeGen.py

sysbench cpu --cpu-max-prime=10000 run &
sysbench cpu --cpu-max-prime=10000 run &
sysbench cpu --cpu-max-prime=10000 run &
sysbench cpu --cpu-max-prime=10000 run &
