import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com" #设置服务器
mail_port=25 #设置端口
mail_user="17610122090@163.com" #用户名
mail_pass="1qaz2wsx" #口令

# 发动者、接受者
sender = "17610122090@163.com"
receivers = '475550727@qq.com'

#邮件内容
mail_msg = '''
<p>Python 邮件发送...</p>
<p><a href="http://www.baidu111.com">这是一个链接</a></p>
'''

message = MIMEText(mail_msg,'html','utf-8')
message['from'] = sender
message['to'] = receivers

#邮件标题
subject = 'Python Email'
message['Subject'] = Header(subject,'utf-8')

#调用程序
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host,mail_port)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender,receivers,message.as_string())

print('邮件发送成功')





