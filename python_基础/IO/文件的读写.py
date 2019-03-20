import cgi,cgitb
import dao
import socket
import os
#创建FieldStorage实例
form = cgi.FieldStorage()


# 获取参数
username = form.getvalue('username')
password = form.getvalue('password')
telephone = form.getvalue('telephone')
email = form.getvalue('email')
#h获取文件名称
file_obj = form['filename']
# 获取本机主机名
local_name = socket.gethostname()

#文件上传
#设置文件路径
fn = os.path.basename(file_obj.filename)
open('D:/'+fn, 'wb').write(file_obj.file.read())



#将数据写到mysql
dao.load2mysql(username,password,telephone,email)

print("Content-type:text/html")
#设置cookie
print('Set-Cookie: name= %s ;expires= %s' % (local_name,'Fri Oct 29 16:24:40 2018') )
print()                               # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="GBK">')
print('<title>Python http get </title>')
print('</head>')
print('<body>')
print('filename:111',))
print('<br>')
print('fileType:')
print('</body>')
print('</html>')