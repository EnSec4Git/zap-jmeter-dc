#!/bin/bash

sleep 40

bash /entrypoint.sh $@

echo "OK" >/tmp/lpwd/done.txt

sleep 30
