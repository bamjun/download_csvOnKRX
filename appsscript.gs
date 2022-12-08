//GOOGLE Apps Script

function myFunction() {
  const gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

  let now = new Date();   
  let yesterday = new Date(now.setDate(now.getDate()-1))
  let year = yesterday.getFullYear()
  let month = yesterday.getMonth() + 1
  let date = yesterday.getDate()
  let yesterdayDate = String(year) + String(month).padStart(2, "0") + String(date).padStart(2, "0")

  // #otp payload
  const gen_otp_data  = {'locale' : 'ko_KR',
  'mktId' : 'STK',
  'trdDd' : yesterdayDate,
  'money' : '1',
  'csvxls_isNo' : 'false',
  'name' : 'fileDown',
  'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'};
  const options = {
      'method' : 'post',
      'payload' : gen_otp_data};
  const otp = UrlFetchApp.fetch(gen_otp_url, options);

  Logger.log(otp.getContentText())

  const csv_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'

  // #csv payload
  const gen_csv_data = {'code' : otp.getContentText() };
  const csv_options = {
      'method' : 'post',
      'muteHttpExceptions': true,
      'payload' : gen_csv_data};
  const csv = UrlFetchApp.fetch(csv_url, csv_options);

  Logger.log(csv.getContentText("cp949"))
  // DriveApp.createFile('1', csv.getContentText("cp949"), MimeType.CSV);


}

function myFunction() {
  var gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

  // #otp payload
  var gen_otp_data  = {'locale' : 'ko_KR',
  'mktId' : 'STK',
  'trdDd' : '20221205',
  'money' : '1',
  'csvxls_isNo' : 'false',
  'name' : 'fileDown',
  'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'};
  var options = {
      'method' : 'post',
      'payload' : gen_otp_data};
  var otp = UrlFetchApp.fetch(gen_otp_url, options);

  Logger.log(otp.getContentText())

  var csv_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
  var gen_csv_data = {'code' : otp.getContentText() };
  var csv_options = {
      'method' : 'post',
      'muteHttpExceptions': true,
      'payload' : gen_csv_data};
  var csv = UrlFetchApp.fetch(csv_url, csv_options);

  Logger.log(csv.getContentText("cp949"))
  DriveApp.createFile('1', csv.getContentText("cp949"), MimeType.CSV);

}
function myFunction() {
  let now = new Date();   
  let yesterday = new Date(now.setDate(now.getDate()-1))
  let year = yesterday.getFullYear()
  let month = yesterday.getMonth() + 1
  let date = yesterday.getDate()
  let yesterdayDate = String(year) + String(month).padStart(2, "0") + String(date).padStart(2, "0")

  const gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'

  // #otp payload
  const gen_otp_data  = {
    'locale' : 'ko_KR',
    'mktId' : 'STK',
    'trdDd' : yesterdayDate,
    'money' : '1',
    'csvxls_isNo' : 'false',
    'name' : 'fileDown',
    'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'};

  // #otp options
  const options = {
    'method' : 'post',
    'payload' : gen_otp_data};
  const otp = UrlFetchApp.fetch(gen_otp_url, options);

  Logger.log(otp.getContentText())

  const csv_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'

  // #csv payload
  const gen_csv_data = {'code' : otp.getContentText() };

  // #csv options
  const csv_options = {
    'method' : 'post',
    'muteHttpExceptions': true,
    'payload' : gen_csv_data};
  const csv = UrlFetchApp.fetch(csv_url, csv_options);

  Logger.log(csv.getContentText("cp949"))
  // DriveApp.createFile('1', csv.getContentText("cp949"), MimeType.CSV);


}

// 코스피
  // const gen_otp_data  = {
  //   'locale' : 'ko_KR',
  //   'mktId' : 'STK',
  //   'trdDd' : yesterdayDate,
  //   'money' : '1',
  //   'csvxls_isNo' : 'false',
  //   'name' : 'fileDown',
  //   'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'};

// 코스닥
  // const gen_otp_data  = {
  //   'locale' : 'ko_KR',
  //   'mktId' : 'KSQ',
  //   'segTpCd': 'ALL',
  //   'trdDd' : yesterdayDate,
  //   'money' : '1',
  //   'csvxls_isNo' : 'false',
  //   'name' : 'fileDown',
  //   'url' : 'dbms/MDC/STAT/standard/MDCSTAT03901'};

