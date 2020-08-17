#!/bin/bash

while [ true ];
do
	python3 fetch_run_bme280.py
    sleep 1
    python3 fetch_run_lightsensor.py
    # Fetch every X seconds
	sleep 15
done
