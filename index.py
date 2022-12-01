gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_data = list(
    "mktId='STK'",
    "trdDd='20210108'",
    "money='1'",
    "csvxls_isNo='false'",
    "name='fileDown'",
    "url='dbms/MDC/STAT/standard/MDCSTAT03901'"
)


import requests
r = requests.post('http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd', json={"key": "value"})
r.status_code
200
r.json()
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx'},
 'json': {'key': 'value'},
 'origin': 'x.x.x.x',
 'url': 'http://httpbin.org/post'}


'locale': 'ko_KR',
'searchType': '1',
'mktId': 'STK',
'trdDd': '20221130',
'idxIndCd': '005',
'strtDd': '20221123',
'endDd': '20221130',
'share': '2',
'money': '3',
'csvxls_isNo': 'false',
'name': 'fileDown',
'url': 'dbms/MDC/STAT/standard/MDCSTAT03801',





import requests
import json
url = "http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}

data = {'locale': 'ko_KR',
'searchType': '1',
'mktId': 'STK',
'trdDd': '20221130',
'idxIndCd': '005',
'strtDd': '20221123',
'endDd': '20221130',
'share': '2',
'money': '3',
'csvxls_isNo': 'false',
'name': 'fileDown',
'url': 'dbms/MDC/STAT/standard/MDCSTAT03801'}


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)


import requests
import json
url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

form_data = {'locale': 'ko_KR',
'searchType': '1',
'mktId': 'STK',
'trdDd': '20221130',
'idxIndCd': '005',
'strtDd': '20221123',
'endDd': '20221130',
'share': '2',
'money': '3',
'csvxls_isNo': 'false',
'name': 'fileDown',
'url': 'dbms/MDC/STAT/standard/MDCSTAT03801'}

server = requests.post(url, data=form_data)

output = server.text

print('The response from the server is: \n', output)



url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
requests.get(url)



down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'


down_sector_KS = requests.post(down_url, query = list(code = otp),
                   add_headers(referer = gen_otp_url)) %>%
  read_html(encoding = 'EUC-KR') %>%
  html_text() %>%
  read_csv()







import requests
import json
gen_otp_url  = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

gen_otp_data = {'locale': 'ko_KR',
'searchType': '1',
'mktId': 'STK',
'trdDd': '20221130',
'idxIndCd': '005',
'strtDd': '20221123',
'endDd': '20221130',
'share': '2',
'money': '3',
'csvxls_isNo': 'false',
'name': 'fileDown',
'url': 'dbms/MDC/STAT/standard/MDCSTAT03801'}
# {'locale' : 'ko_KR',
# 'searchType' : '1',
# 'mktId' : 'STK',
# 'trdDd' : '20221130',
# 'idxIndCd' : '005',
# 'strtDd' : '20221123',
# 'endDd' : '20221130',
# 'share' : '2',
# 'money' : '3',
# 'csvxls_isNo' : 'false',
# 'name' : 'fileDown',
# 'url' : 'dbms/MDC/STAT/standard/MDCSTAT03801'}

otp = requests.post(gen_otp_url, data=gen_otp_data)


down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'

down_sector_KS = requests.post(down_url, data=gen_otp_data, json=gen_otp_url)

# , referer = gen_otp_url, 

import pandas as pd
pd.read_csv()

\\\
import requests
import re

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]



url = 'http://google.com/favicon.ico'
r = requests.get(down_url, allow_redirects=True)
filename = get_filename_from_cd(a.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)




#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#                                        재너럴
gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

gen_otp_data  = {'locale' : 'ko_KR',
'searchType' : '1',
'mktId' : 'STK',
'trdDd' : '20221130',
'idxIndCd' : '005',
'strtDd' : '20221123',
'endDd' : '20221130',
'share' : '2',
'money' : '3',
'csvxls_isNo' : 'false',
'name' : 'fileDown',
'url' : 'dbms/MDC/STAT/standard/MDCSTAT03801'}
requests.post(gen_otp_url, data=gen_otp_data)


gen_otp_url = 'https://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

gen_otp_data = {'bld' : 'dbms/MDC/STAT/standard/MDCSTAT03801',
'locale' : 'ko_KR',
'searchType' : '1',
'mktId' : 'STK',
'trdDd' : '20221130',
'idxIndCd' : '005',
'strtDd' : '20221123',
'endDd' : '20221130',
'share' : '2',
'money' : '3',
'csvxls_isNo' : 'false'}
requests.post(gen_otp_url, data=gen_otp_data)
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd



#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
#ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# 마지막 실행
# 토큰otp 인증을 받아와야, 다운로드 링크에서 csv 파일 다운가능.

# otp 링크
gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

#otp payload
gen_otp_data  = {'locale' : 'ko_KR',
'searchType' : '1',
'mktId' : 'STK',
'trdDd' : '20221130',
'idxIndCd' : '005',
'strtDd' : '20221123',
'endDd' : '20221130',
'share' : '2',
'money' : '3',
'csvxls_isNo' : 'false',
'name' : 'fileDown',
'url' : 'dbms/MDC/STAT/standard/MDCSTAT03801'}
#otp 토큰 받아오기
otp = requests.post(gen_otp_url, data=gen_otp_data)

# 다운받을 링크
csv_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
# 코드에 토큰 넣기
gen_otp_data = { 'code' :  otp.content }
csv = requests.post(csv_url, data=gen_otp_data)
filename = get_filename_from_cd(csv.headers.get('content-disposition'))
open(filename, 'wb').write(csv.content)

