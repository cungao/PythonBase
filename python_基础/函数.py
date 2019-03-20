#创建一个函数
def printBean(name,age,sex='man',*vartuple,**vardic):
    print('name:',name)
    print('age:',age)
    print('sex:',sex)
    print('*vartuple:',vartuple)
    print('**vardic:',vardic)
    return
printBean('gaocun',21,1,1,1,1)
printBean(name = 'gaocun',age = 22,a=1,b=2)
#创建一个匿名函数
sum = lambda x,y :x+y
print(sum(1,2))
#全局变量
def count(x,y):
    global count1
    count1 = 100
    print('x*y=',x*y)
count(10,2)
print(count1)




