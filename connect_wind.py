# -*- coding: utf-8 -*-
"""
# Author: lixiang
# Created Time : Tue 24 Mar 2020 08:02:48 PM CST
# File Name: test.py
# Description:
"""
from bq import *

sql = '''
SELECT TRADE_DAYS FROM WINDDF.ASHARECALENDAR
WHERE S_INFO_EXCHMARKET = 'SSE' AND
TRADE_DAYS BETWEEN 20190101 AND 20191231
ORDER BY TRADE_DAYS ASC
'''
dates = get_data_sql(sql,to_csv=True,csv_name='output.csv')
print(dates.head())

