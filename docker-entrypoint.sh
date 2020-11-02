#!/bin/bash
set -e

zap.sh -daemon -port 8080 -host 127.0.0.1 -config api.disablekey=true 1>/opt/lpwd/zaplog.txt 2>/opt/lpwd/zaperr.txt &

sleep 10

exec "$@"