#Setter Getter คือ การดึงข้อมูลและแก้ไขในส่วนที่ใส่encapsulation
class Employee:

    def __init__(self,name,salary,department):
        
        self.__name= name
        self. __salary= salary
        self.__department= department

    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self. __salary))
        print("ตำแหน่ง = {}".format(self.__department))

    def __del__(self):
        print("Call Destructure")

#setter method (setname)
    def setname(self,newname):
        self.__name = newname

    #getter method (getname)
    def getname(self):
        return self.__name

obj1 = Employee("กาย",20000,"บัญชี")
obj1.setname("jotaro")#setter method
obj1.__salary=70000 
obj1.__department="star platinum"
obj1.showdata()
print(obj1.getname())#getter method