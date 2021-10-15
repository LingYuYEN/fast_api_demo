import smtplib  # 傳送郵件
from email.mime.text import MIMEText  # 專門傳送正文
from email.mime.multipart import MIMEMultipart  # 傳送多個部分
from email.mime.application import MIMEApplication  # 傳送附件
from datetime import datetime
import time
import schedule
import json
import os


def send_mail():
    demo_info = '測試發送 mail json 附件'

    jsonfile_name = "./jsonfile.json"
    members_jsonfile = "./members.json"

    # dict_list = []
    # if os.path.exists(jsonfile_name):
    #     with open(jsonfile_name, 'r') as jsonfile:
    #         dict_list = json.load(jsonfile)
    #         print(dict_list)
    # else:
    #     with open(jsonfile_name, 'w') as jsonfile:
    #         dict_list.append(demo_info)
    #         json_object_list = json.dumps(dict_list, indent=4)
    #         jsonfile.write(json_object_list)

    def mail_schedule(demo_str):
        content = MIMEMultipart()  # 建立MIMEMultipart物件
        content["subject"] = "Python use Gmail 寄件測試"  # 郵件標題
        content["from"] = "yuxp0130@gmail.com"  # 寄件者
        content["to"] = "yuxp0130@seed.net.tw"  # 收件者
        content.attach(MIMEText(demo_str))  # 郵件內容

        # 構建郵件附件
        # file = file           #獲取檔案路徑
        part_attach1 = MIMEApplication(open(jsonfile_name, 'r').read())  # 開啟附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=jsonfile_name)  # 為附件命名
        content.attach(part_attach1)  # 新增附件

        # part_attach2 = MIMEApplication(open(members_jsonfile, 'rb').read())  # 開啟附件
        # part_attach2.add_header('Content-Disposition', 'attachment', filename=members_jsonfile)  # 為附件命名
        # content.attach(part_attach2)  # 新增附件

        host_server = "smtp.gmail.com"
        host_port = "587"
        host_send_account = "yuxp0130@gmail.com"
        host_send_pwd = "rvdb gluy kjbq nboo"

        # host_server = "authsmtp.seed.net.tw"
        # host_port = "25"
        # host_send_account = "yuxp0130@seed.net.tw"
        # host_send_pwd = "09260130"

        with smtplib.SMTP(host=host_server, port=host_port) as smtp:  # 設定SMTP伺服器
            try:
                smtp.ehlo()  # 驗證SMTP伺服器
                smtp.starttls()  # 建立加密傳輸
                smtp.login(host_send_account, host_send_pwd)  # 登入寄件者gmail
                # smtp.login()
                smtp.send_message(content)  # 寄送郵件
                print("Complete!")
            except Exception as e:
                print("Error message: ", e)

    def seconds_schedule():
        print(datetime.now())

    mail_schedule(demo_info)
    # 每隔5秒執行一次job1
    # schedule.every(5).seconds.do(seconds_schedule())
    # schedule.every(5).seconds.do(job_func=seconds_schedule)
    # 排程每天指定時間執行
    schedule.every().day.at('12:59').do(mail_schedule, demo_info)

    while True:
        schedule.run_pending()
        time.sleep(1)
