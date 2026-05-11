#การสร้าง constructor เป็นฟังก์ชั่นที่เมื่อเปิดใช้เมื่อเริ่มกระบวนการทั้งหมด
class Employee:

    def __init__(self,name,salary,department):
        self.name= name
        self.salary= salary
        self.department= department
        
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

    def __del__(self):#การสร้าง destructure เป็นฟังก์ชั่นที่จะทำงานในตอนที่จะจบการทำงาน
        print("Call Destructure")
#การสร้างวัตถุ
obj1 = Employee("กาย",20000,"บัญชี")
obj1.salary=70000
obj1.showdata()
obj2 = Employee('jotaro',50000,'Starplatinum')
obj2.showdata()
obj3 = Employee('dio',50000,'the world')
obj3.showdata() 