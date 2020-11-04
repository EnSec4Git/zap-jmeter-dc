#!/bin/bash

sleep 20

bash /entrypoint.sh $@

echo "OK" > /tmp/lpwd/done.txt

sleep 30