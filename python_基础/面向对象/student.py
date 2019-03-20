#创建一个对象
class student:
    """class 的描述"""
    #基本属性
    id = 1
    name ='gaocun'
    count = 0
    __age = 29
    #构造方法
    def __init__(self,id,name,age):
        self.name = name
        self.id = id
        self.__age = age
        student.count += 1
    def toString(self):
        print('name:',self.name,' id:',self.id,'age:',self.__age)
#实例化对象
st1 = student(1,'gaocun',22)
print('student.id',student.id)
print('student.count',student.count)
st1.toString()
st2 = student(2,'dawang',23)