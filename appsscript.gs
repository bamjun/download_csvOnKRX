//GOOGLE Apps Script

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
