# -*- coding: utf-8 -*-
# @E-mail: lixu8666@gmail.com

import re

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

json_long = dict()
json_long['name'] = re.compile('V\w+\s\w+V').findall(long_text)[0]
json_long['lei'] = re.compile('\w{20}').findall(long_text)[0]
sub_fund = list()
sub_funds = re.compile('([\d{1}\\\.].*[LU\d+\n]*)[\d+]?').findall(long_text)
for sub in sub_funds:
    titles = re.compile('\.([\s\w+]*)').findall(sub.split('\n', 1)[0])
    if len(titles) > 0:
        title = titles[0][1:]
        sub_fund.append({'title': title,'isin': re.compile('LU\d+').findall(sub)})
json_long['sub_fund'] = sub_fund

print(json_long)
