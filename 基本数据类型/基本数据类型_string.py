import  string
#判断字符串是否包换指定字符后者字符串
_in = 'g' in 'gaocun'
not_in = 'ga' not in 'gaocun'
print(_in,not_in)
print('=====================')
#字符串格式化(类似mybatis的占位符)
print("我叫 %s 今年 %d 岁" %('高存',20))
#字符串常用的函数
print('将字符串第一个字符大写：','gaocun'.capitalize())
print('将字符串的长度调为等长','gaocun'.center(20,'#'))
print('返回指定字符在字符串中出现的次数','gaocun'.count('g'))
print('检查字符串是否以指定字符结尾','gaoucn'.endswith('n'))
print('将字符串中对的tab建换位指定空格数','gao\tcun'.expandtabs(tabsize=0))
print('检查字符串中是否包含指定字符返回索引值','gaocun'.find('o'))
print('检查字符串中是否包含指定字符返回索引','gaocun'.index('a'))
print('判读字符串是否是字母和数字','gaoucn@@'.isalnum())
print('判读字符串是否全是数字','123456'.isdigit())
print('判读字符串是否全是字母','gaocun'.isalpha())
print('判断小写','gaocun'.islower())
print('判断大写','gaocun'.isupper())
print('判读字符串是否全是数字','123456'.isnumeric())
print('判读字符串是否全为空格','   '.isspace())
print('判断字符串是否是tatle','Gaoun'.istitle())
print('指定字符串分割符','#'.join(['g','a','o']))
print('获取字符串长度',len('gaocun'))
print('指定字符串长度，不足填补指定字符','gaoun'.ljust(8,'$'))
print('将字符串转为小写','GAOCUN'.lower())
print('截取字符串左边指定字符','@@@gaocun'.lstrip('@@@'))
print('截取字符串右边指定字符','@@@gaocun@@@'.rjust(6,'@'))
print('替换字符串中指定字符','gaocun222'.replace('2','%',1))












