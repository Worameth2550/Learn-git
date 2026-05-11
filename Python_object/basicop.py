#การสร้าง class
class Employee:
    #สร้างmethod
    def detail(self,name,salary,department):#เรียกตรงนี้ว่าการสร้างMethod คือันเดียวกับการสร้าง function แค่คนละชื่อ
        self.name= name
        self.salary= salary
        self.department= department
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))
#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("กาย",50000,"บัญชี")
obj1.salary=70000
obj2 = Employee()
obj2.detail("jotaro",50000,"โปรแกรมเมอร์")
obj3=Employee() 
obj3.detail("nut",100000,"ผู้จัดการ")

obj1.showdata()
obj2.showdata()
obj3.showdata()

print(isinstance(obj1,Employee))#ฟังก์ชั่นเสริมใช้ตรวจสอบว่าเป็นคลาสที่เลือกไหม
print(dir(obj1))#ใช้ตรวจดูว่ามีattributeอะไรบ้าง
print(obj1.__class__)#ใช้ดูชนิดจริงของclass

