# while
x = y = 1
while x <= 9:
    while y <= x:
        print(y,'*',x,'=',x*y,end='  ')
        y += 1
    print('')
    y = 1
    x += 1

print('-------------------------------------')
#for
for x in range(10):
    for y in range(x):
        print(y+1,'*',x,'=',x*(y+1),end='  ')
    print('')

#continue
for index in range(10):
    if index % 2 == 0:
        print('这是个偶数：',index)
    else:
        continue
        print('这是个奇数：',index)

#break
for index in range(10):
    if index % 2 == 0:
        print('这是个偶数：',index)
    else:
        #遇到奇数结束程序
        pass
        break