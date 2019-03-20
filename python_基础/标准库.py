import os
import shutil
import glob
import sys
import 面向对象.people
print('获取当前路径：',os.getcwd())
print('切换路径：',os.chdir('d:'))
print('执行系统命令',os.system('java -version'))
print('查看模块结构',dir(面向对象.people))
print('查看模块帮助文档',help(面向对象.people))
print('查看模块文件包位置:',sys.modules['os'])
#print('查看模块文件的版本号：',sys.__version__)
print('copy 文件',shutil.copyfile('date_file/1.java','date_file/2.txt'))
#print('移动重命名文件：',shutil.move('date_file/1.txt','date_file/1.java'))
print('所有文件',glob.glob('*'))
print('获取系统参数',sys.path)

