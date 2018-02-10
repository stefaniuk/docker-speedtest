#!/usr/bin/env python

import os
import subprocess
import time
from datetime import datetime as dt
from pytz import timezone as tz

interval = int(os.getenv('SPEEDTEST_INTERVAL'))

def main():
    while True:
        perform_test()
        time.sleep(interval)

def perform_test():
    out, err = subprocess.Popen(['/usr/local/speedtest-cli/speedtest.py', '--simple'], stdout=subprocess.PIPE).communicate()
    lines = []
    for line in out.splitlines():
        lines.append(str(line))
    process_output(lines)

def process_output(lines):
    pg_key,pg_val,pg_unit = lines[0].split(' ')
    dl_key,dl_val,dl_unit = lines[1].split(' ')
    ul_key,ul_val,ul_unit = lines[2].split(' ')
    log_message('INFO', 'ping=' + pg_val + '|download=' + dl_val + '|upload=' + ul_val)

def log_message(level, msg):
    now = dt.now(tz(os.getenv('TZ')))
    datetime = now.strftime('%Y/%m/%d %H:%M:%S.%f')[:-3] + now.strftime('%z')
    print(datetime + '|speedtest|' + level + '|' + msg)

main()
