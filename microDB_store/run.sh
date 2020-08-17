#!/bin/bash

while [ true ];
do
	python3 fetch_run_bme280.py
    sleep 1
    python3 fetch_run_lightsensor.py
    # Fetch every 10 seconds
	sleep 10
done
