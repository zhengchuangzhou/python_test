import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

name = []
email = []

with open('test.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        name.append(row[0])
        email.append(row[1])



# 发送方邮箱: csv文件中的某个邮箱
from_addr = email[0]
# 发送方邮箱授权码: xxx
password = 'xxx'

# 接收方邮箱: csv文件中的某个邮箱
to_addr = email[1]

smtp_server = 'smtp.qq.com'

msg = MIMEText('send by python','plain','utf-8')

msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python homework')

server=smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
