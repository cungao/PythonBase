import re
#match:判断字符串起始位置
str = 'www.baidu.com'
str1 = '''baidu   
 
www.xinliang.com'''
str2 = 'Cats are smarter than dogs'
print('起始位置匹配：',re.match('www',str).span())
print('不是起始位置匹配：',re.match('com1',str))

print(str1)
#search：扫描整个字符串返回第一个匹配，匹配不到报错
print('起始位置匹配：',re.search('www',str).span())
print('不是起始位置匹配：',re.search('com',str1).span())
searchBean = re.search('(.*) are (.*?) .*',str2)
print(searchBean)
print(searchBean.group(2))

#替换字符串
phone = '2004-959-559 # 这是一个电话号码'
#替换‘#’号,返回替换后的字符串
num = re.sub('\s#(.*)','',phone)
print('num:',num)
num1 = re.sub('\D','',phone)
print(num1)

#匹配整个字符串，返回匹配成功的列表
str_list = re.findall(r'[A-Za-z]+',str2)
print(str_list)

#按照指定字符分割字符串
spli_list = re.split('[^A-Za-z]+',str2)
print(spli_list)