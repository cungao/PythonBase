import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
mail_host="smtp.163.com" #设置服务器
mail_port=25 #设置端口
mail_user="17610122090@163.com" #用户名
mail_pass="1qaz2wsx" #口令

# 发动者、接受者
sender = "17610122090@163.com"
receivers = 'cun.gao@baifendian.com'

#邮件内容-带附件
message = MIMEMultipart()
message['from'] = sender
message['to'] = receivers
subject = 'Python SMTP Test Email'
message['Subject'] = Header(subject,'utf-8')

#邮件正文内容
mail_content = MIMEText('这里填写邮件的正文内容','plain','utf-8')
message.attach(mail_content)

#构造附件 01.txt
txt_01 = MIMEText(open('Mysql_Pymsql.py','rb').read(),'base64','uft-8')
txt_01["Content-Type"] = 'application/octet-stream'
#这是附件文件的名称
txt_01["Content-Disposition"] = 'attachment; filename="python_01.txt"'
message.attach(txt_01)

#调用程序
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host,mail_port)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender,receivers,message.as_string())

print('邮件发送成功')





