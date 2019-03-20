#集合set是一个无序不重复的元素序列
set_ = {'a','d','f','a'}
print('原set',set_)
#增
set_.add('t')
print('添加元素',set_)
set_.update('1','2')
print('添加元素',set_)
set_.update([1,2],[5,3])
print('添加元素',set_)
set_.update({'name':'gaoucn'})
print('添加元素',set_)
#删
set_.remove('name')
print('删除元素',set_)
set_.discard('name')
print('删除元素',set_)
set_.pop()
print('删除元素',set_)
#集合的其他方法






