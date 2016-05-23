#!/bin/bash

```for port in $(seq 8000 8009)
do
    kill -9 $(lsof -i:${port} | awk '{print $2}' | tail -n 2)
done
lsof -nPi TCP -s TCP:LISTEN | grep 127.0.0.1:80 | grep 4u | sort -k 8