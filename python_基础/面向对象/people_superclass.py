class people_super():
    #定义基本属性
    name = 'gaocun'
    age = 100
    hobby = 'dahuaxiyou'
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def toString(self):
        print('name:',self.name,'age:',self.age,'hobby:',self.hobby)


