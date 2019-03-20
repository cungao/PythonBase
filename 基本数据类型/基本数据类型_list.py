#创建list
list_ = [1,2,3,'1','a','b']
#增
print('原列表打印：',list_)
list_.insert(0,'100')
print('指定索引添加元素',list_)
list_.append('888')
print('在list最后追加元素',list_)
#删
del list_[0]
print('指定索引删除元素',list_)
list_.remove('888')
print('指定元素删除元素',list_)
list_.pop()
print('删除最后面的元素',list_)
list_.clear()
print('清空元素 ',list_)
list_ = [1,2,3,'1','a','b']
#改
list_[0] = '999'
print('指定索引改变元素',list_)
#其他list操作
print('判读元素是否在list中','999' in list_)
print('统计某元素出现的次数',list_.count('a'))
list_.reverse()
print('反转列表',list_)
#集合并、交、差
#A、B集合取交集
a=[2,3,4,5]
b=[2,5,8]
#交
tmp = [val for val in a if val in b]
print('a交b：',tmp)
#交2
print('a交b：',list(set(a).intersection(set(b))))
#并
print('a并b',list(set(a).union(set(b))))
#差
print('a差b',list(set(b).difference(set(a))))

