import requests
import re
from datetime import datetime, timedelta

yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")

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


gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

#otp payload
gen_otp_data  = {'locale' : 'ko_KR',
'mktId' : 'STK',
'trdDd' : yesterday,
'money' : '1',
'csvxls_isNo' : 'false',
'name' : 'fileDown',
'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'}
#otp 토큰 받아오기
otp = requests.post(gen_otp_url, data=gen_otp_data)

# 다운받을 링크
csv_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
# 코드에 토큰 넣기
gen_otp_data = { 'code' :  otp.content }
csv = requests.post(csv_url, data=gen_otp_data)
filename = get_filename_from_cd(csv.headers.get('content-disposition'))
open(filename, 'wb').write(csv.content)



