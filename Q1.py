# -*- coding: utf-8 -*-
# @E-mail: leicunkuan@gmail.com

import pandas as pd
import requests
import re
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
r = requests.get(url=url).text
res = re.findall(',{"confirmed"(.*?)]}', r)
df = pd.DataFrame([], columns=['confirmed', 'died', 'crued', 'curConfirm', 'area'])

for idx, item in enumerate(res):
    new_str = 'confirmed' + item
    # print(new_str)
    tmp = re.findall('confirmed:"(.*?)","died":"(.*?)","crued":"(.*?)",.*?"curConfirm":"(.*?)",.*?"area":"(.*?)","subList":.*?' ,new_str)
    df.loc[idx, 'confirmed'] = tmp[0][0]
    df.loc[idx, 'died'] = tmp[0][1]
    df.loc[idx, 'crued'] = tmp[0][2]
    df.loc[idx, 'curConfirm'] = tmp[0][3]
    df.loc[idx, 'area'] = tmp[0][4].split(',')[0].replace('"', '').encode('utf-8').decode("unicode_escape")

df.to_csv('test.csv', encoding='gbk', index=False)
