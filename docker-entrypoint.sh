#!/bin/bash
set -e

ls -la /opt/
ls -la /opt/lpwd/

#zap.sh -daemon -port 8080 -host 127.0.0.1 -config api.disablekey=true 1>/opt/lpwd/zaplog.txt 2>/opt/lpwd/zaperr.txt &
zap.sh -daemon -port 8080 -host 127.0.0.1 -config api.disablekey=true 1>/dev/null 2>/dev/null &

sleep 10

exec "$@"