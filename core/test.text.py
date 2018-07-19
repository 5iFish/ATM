# Author:ZT
import time
import os
BASE_LOGGER = os.path.dirname(os.getcwd())+'\\logs'
os.chdir(BASE_LOGGER)
with open('transactions.log', 'r', encoding='utf-8') as f:
    for line in f:
        loglist = line.strip().split('\t')
        _year = int(time.strftime('%Y', time.strptime(loglist[2], '%Y-%m-%d %H:%M:%S')))
        print(_year)