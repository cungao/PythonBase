from people_superclass import *
from people import *
#单继承示例
class student(people,people_super):
    grade = ''
    def __init__(self,name,age,weigth,grade,hobby):
        #调用父类的构函
        people.__init__(self,name,age,weigth)
        people_super.__init__(self,name,age,hobby)
        self.grade = grade
    def toString(self):
        print('name:',self.grade)

st = student('gaocun',22,100,2,'dahuaxiyou')
st.speak()
print('GetName',st.name)
st.toString()