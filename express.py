# -*- coding: utf-8 -*-  
# ---------------------------------------
#   程序：获取订单详情爬虫
# ---------------------------------------

import json
import requests
import urllib3
import urllib
import xlrd
import re
import time


# Excel中的数据
sheet_one= xlrd.open_workbook('C:/Users/andy/Desktop/python/python_test.xlsx').sheet_by_index(0)


# 访问的URL
url_address='https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury?cb=jQuery110204914333994305038_1509696342371&appid=4001&com=ems&nu='
# 访问头
header = {
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'Accept-Encoding':'gzip, deflate, br',
     'Accept-Language':'zh-CN,zh;q=0.8',
     'Connection':'keep-alive',
     'Cookie':'PSTM=1498888328; BIDUPSID=1589189A5F549E2AB9E43D4B03CF8B7E; BAIDUID=99FEF92766490D6F8C298F8A0749CE95:FG=1; BDUSS=UFmQ244WTRyT0V6VXBocVhFZDBTOHAxc3NMY1A2Rk12LW1xb3Jnc2psQWV3c3haSVFBQUFBJCQAAAAAAAAAAAEAAAA8m6FXvbvNqLSmxa7X-QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB41pVkeNaVZb; MCITY=-365%3A; BDRCVFR[Usf3Hj-5366]=mk3SLVN4HKm; PSINO=3; H_PS_PSSID=1464_21116_24879_20718; BDORZ=FFFB88E999055A3F8A630C64834BD6D0',
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

for item in sheet_one.col_values(3):
   if item !='':
       req = requests.get(url_address +''+ item,headers =header)
       str_data = re.findall(".*\((.*)\).*", str(req.content))[0]
       msg = str_data.encode().decode('unicode_escape')
       try:
           jn = json.loads(msg)
           c = jn['data']['info']['context']
           for i in c:
               print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(i['time'])))+" "+ i['desc'])

       except :
           c =1


