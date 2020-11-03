#!/usr/bin/env python3

### Created using the OWASP ZAP API documentation:
### https://www.zaproxy.org/docs/api/
### Original Documentation License: Apache 2

import time
import json
import csv
from pprint import pprint
from zapv2 import ZAPv2

# Here the target is defined and an instance of ZAP is created.
SCANURL = 'http://testableapi:8080/'
SWAGGERURL = 'http://localhost:8080/v2/swagger.json'
CTXNAME = 'localtest'
AJAXTO = 5 * 60 # a.k.a. 5 minutes
DONE = '/tmp/lpwd/done.txt'
ENTRYPOINTS = '/tmp/lpwd/entrypoints.txt'
RESULTS = '/tmp/lpwd/results.csv'

time.sleep(10) # Boot up time

zap = ZAPv2()

ctxId = zap.context.new_context(CTXNAME)
print(ctxId)
zap.context.set_context_regexs(CTXNAME, json.dumps([r'^(http(s)?:\/\/testableapi:8080).*$']), '[]')

#zap.urlopen(SCANURL)
#time.sleep(5)

### Spider

scanID = zap.spider.scan(SCANURL, contextname=CTXNAME)
while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

print('Spider has completed!')
# Prints the URLs the spider has crawled
with open(ENTRYPOINTS, 'w') as out:
    out.write('\n'.join(map(str, zap.spider.results(scanID))))

### AJAX Spider

print('Ajax Spider target {}'.format(SCANURL))
scanID = zap.ajaxSpider.scan(SCANURL, contextname=CTXNAME)

timeout = time.time() + AJAXTO
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status: ' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10000)
with open(ENTRYPOINTS, 'a') as out:
    out.write('\n'.join(map(str, ajaxResults)))

### Active Scan

scanID = zap.ascan.scan(SCANURL, contextid=ctxId)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')

### Swagger Import

zap.openapi.import_url(SWAGGERURL)


### Export results


alerts = zap.core.alerts()
csval = list(map(lambda x: (x['risk'], repr(x)), alerts))
with open(RESULTS, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
    csvwriter.writerow(['Risk', 'Description'])
    for entry in csval:
        csvwriter.writerow(entry)

# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(alerts)

with open(DONE, 'w') as f:
    f.write("OK")
