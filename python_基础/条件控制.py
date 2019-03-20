#举个例子
#接收控制台输入参数
age = int(input('请输入你家狗子的年龄'))
print('')
if age < 0:
    print('数据非法，程序停止')
elif age == 1:
    print('你家狗子年龄为: %d 岁' % (age))
elif age == 2:
    print('你家狗子年龄为: %d 岁' % age)
elif age > 2:
    human = 22 + (age - 2)*5
    print('你家狗子的年龄：',human)

### 退出提示
input('按 enter 键退出')