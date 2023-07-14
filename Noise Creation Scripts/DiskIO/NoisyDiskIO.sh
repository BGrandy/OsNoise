#!/bin/bash

# Run 3 recursive grep commands on a directory to make the system I/O busy
grep -r "testInTrace.txt" /home/ &
grep -r "testPublic.txt" /home/ &
grep -r "test3.txt" /home/ &

# Run the Python script to read 10 files concurrently
python3 read10FilesConcurrently.py
