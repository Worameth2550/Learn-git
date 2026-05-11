#inheritance คือ การสืบทอด class ไปให้ยัง class รุ่นลูกต่อไปใช้
# อีกทั้งยังสามารถเพิ่มความสามารถต่างๆในรุ่นลูกที่สืบทอดมาด้วยและก้สืบทออด constructor destructor ได้
class animals:
    def speak(self):
        print("Animals sound")
    def walk(self):
       print('walk...')
    def fly(self):
       print('fly บินล่องไป')

class Dog(animals):
    def speak(self):#แก้ไข้และเพิ่มฟังก์ชั่นอันเก่าให้เป็นของจำเพาะในclassนี้
     super().speak()
     print('howllll')
    def run(self):
       print('runnnnnnn')

class fish(Dog,animals):#การสืบทอด class สามารถสืบทอดได้มากกว่า 1 class 
    def swim(edit):#คำว่า self ที่นิยมใช้ในวงเล็บเป็นเหมือนตัวแปรที่ใช้บอกกับคอมพิวเตอร์ว่าถ้าเรียดใช้คำสั่งตัวแปรที่เราใส่จะเข้ามาแทนที่แล้วทำงานตามที่เราสั่ง
       print('swimmm')

A = Dog()
A.speak()
A.walk()
A.run()
A.fly()
b= animals()
b.speak()
b.fly()
c=fish()
c.speak()
c.swim()
c.run()