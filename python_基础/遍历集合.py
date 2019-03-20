import sys
#遍历list
list_ = ['a','b','x','d','s']
#创建迭代器
it = iter(list_)
print('迭代器的类型：',type(it))
#for
for ele in it:
    print(ele)
print('===================')
#while
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

