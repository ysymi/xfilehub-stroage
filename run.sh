#!/bin/bash
echo
for port in $(seq 8000 8009)
do
    PORT=${port} python3.5 server.py &
done