#!/usr/bin/env python3

import json
import csv

import sys

csv.field_size_limit(134217728)

with open('./zapdata/results.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',', quotechar='"')
    columns = None
    significant_vulns = 0
    total_vulns = 0
    for row in csvreader:
        if not columns:
            columns = row
            continue
        if row[0] == 'High' or row[0] == 'Critical':
            significant_vulns += 1
        total_vulns += 1
    print('High or above vulnerabilities: ', significant_vulns)
    print('Total vulnerabilities: ', total_vulns)

with open("./jmeterdata/PetApi/statistics.json", "r") as json_file:
    jdata = json.load(json_file)
    totd = jdata["Total"]
    total = totd["sampleCount"]
    errors = totd["errorCount"]
    tot_err_rate = errors / total
    print("Total JMeter error rate: ", tot_err_rate)

#### Do something with this data:
# Arbitrary test criteria
if significant_vulns > 2: 
    sys.exit(1)

if tot_err_rate > 0.9:
    sys.exit(1)