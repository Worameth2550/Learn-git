#Encapsulation คือ การห่อหุ้มข้อมูลเพื่อจำักดการเข้าถึง
class Employee:

    def __init__(self,name,salary,department):
        #public attribute คือ มาตราการความปลอดภัยน้อยที่สุดแก้ไขง่ายเข้าถึงง่าย
        self.name= name
        self. _salary= salary#protector attribute ติดตัวป้องกันเป็นตัว _ อยู่
        self.department= department
    #public method
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self. _salary))#protector attribute ติดตัวป้องกันเป็นตัว _ อยู่
        print("ตำแหน่ง = {}".format(self.department))

    def __del__(self):#การสร้าง destructure เป็นฟังก์ชั่นที่จะทำงานในตอนที่จะจบการทำงาน
        print("Call Destructure")
#การสร้างวัตถุ
obj1 = Employee("กาย",20000,"บัญชี")
obj1._salary=70000 #ใช้เครื่องหมาย _ เพื่อเปิดใช้งานการแก้ไขตรงแสดงผลถ้าไม่ใส่จะรันได้แต่ข้อมูลที่ใส่ไว้จะไม่แก้ไข
obj1.showdata()
obj2 = Employee('jotaro',50000,'Starplatinum')
obj2.showdata()
obj3 = Employee('dio',50000,'the world')
obj3.showdata() 

#แต่หากเป็น private จะใช้เครื่องหมาย __ ซึ่งจะมีการเปิดใช้งานแบบเดียวกันกับ protector แต่แก้ไขจากภายนอกไม่ได้