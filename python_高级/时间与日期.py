import time
import calendar
import datetime
print('获取当前时间戳：',time.time()) #1544686311.4246957
print('获取当前时间：',type(time.localtime(time.time())),'\n',time.localtime(time.time()))
print('获取格式化时间：',time.asctime(time.localtime(time.time())))
print('获取格式化时间：',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print('获取某年某月日历:','\n',calendar.month(2018,1))
#获取当前日期
current_day = datetime.date.today()
print('获取当前时间：',current_day,type(current_day))
print('获取当前年：',current_day.year)
print('获取当前月：',current_day.month)
print('获取当前日',current_day.day)
#获取明天日期



#datetime 模块
#求两个时间的差值(天、时、分、秒)
import datetime
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print('两个时间的差：',(endtime - starttime).seconds)
#求当前日期
today = datetime.datetime.today()
print("当前时间：",today)
print("当前年：",today.year,starttime.year)
print("当前月：",today.month,starttime.month)
print("当前日：",today.day,starttime.day)
#求昨天日期
day_1 = datetime.datetime.now() - datetime.timedelta(days=1)
print("昨天的日期：",day_1)
#将字符串转化为date对象
str_2_date = datetime.datetime.strptime("2018-01-12","%Y-%m-%d")
print("string to date:",type(str_2_date),str_2_date)
#将字符串转化为date对象
date_2_date = datetime.datetime.strftime(str_2_date,'%Y%m%d')
print("",date_2_date)


