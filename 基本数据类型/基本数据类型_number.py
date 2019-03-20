import random
#number --随机数函数
#从序列中随机挑选一个元素出来
list_ = ['高存','大王','妞子','粪池']
tuple_ = ('高存','大王','妞子','粪池')
print("----随机获取序列中的元素---------------------")
for index in range(len(list_)):
    ele = random.choice(list_)
    list_.remove(ele)
    print(ele)
print("----随机获取序列中的元素---------------------")
for index in range(len(tuple_)):
    ele_ = random.choice(tuple_)
    print(ele_)
print('--------在一定范围中随机取数-----------------')
#在一定范围中随机取数
print(random.randrange(0,10))
print('----随机产生一个[0,1)之间的数据---------------')
#随机产生一个[0,1)之间的数据
print(random.random())
print('将序列中的元素顺序随机打乱')
#将序列中的元素顺序随机打乱
list_1 = ['高存','大王','妞子','粪池']
random.shuffle(list_1)
print(list_1)
print('-----产生x，y的数据--------------')
print(random.uniform(2,3))