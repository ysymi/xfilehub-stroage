#!/bin/bash

for port in $(seq 8000 8010)
do
    PORT=${port} python3.5 server.py &
done