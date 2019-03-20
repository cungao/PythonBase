#创建字典
dic_ = {'name':'gaocun','age':25}
print('原dic:',dic_)
#增
dic_['gender'] = 'man'
print('添加元素',dic_)
#删
del dic_['gender']
print('删除元素',dic_)
print('通过key删除元素',dic_.pop('sex','is null'))
print('删除末尾的元素',dic_.popitem())
dic_.clear()
print('清空字典',dic_)

#改
dic_ = {'name':'gaocun','age':25}
dic_['age'] = 100
print('修改元素',dic_)
#dic的其他函数
print('转为string',str(dic_))
print('通过key获取value',dic_.get('Name','is null'))
print('判断key是否存在','age' in dic_)
print('获取items',dic_.items(),type(dic_.items()))
print('获取所有的key',dic_.keys(),type(dic_.keys()))
print('通过key获取value',dic_.setdefault('sex','nan'),dic_)
print('获取所有的value',dic_.values())

#遍历dic
dic_ = {'name':'gaocun','age':25}
for key,value in dic_.items():
    print(key,'\t:',value)
dic_ = {'name':'gaocun','age':25}
for key in dic_.keys():
    print(key,'\t :',dic_.get(key))

#补充
#通过工厂创建dict list2dict、tuple2dict
list2dict = dict(([1,'a'],[2,'b']))
print('list2dict:',list2dict)
tuple2dict = dict(((1,'a'),(2,'b')))
print('tuple2dict',tuple2dict)
#这样只是将dict的key放入到了list当中
dict2list1 = list({1:'a',2:'b'})
print('dict2list1:',dict2list1)
#通过函数将dict转化为list
def dict2list(dict):
    list =[];
    keys = dict.keys();
    values = dict.values();
    for key,value in zip(keys,values):
        list.append(key);
        list.append(value);
    return list;
print('dict2list2:',dict2list({1:'a',2:'b'}))




