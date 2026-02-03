
print("hello word")

class Person : 
    def __init__(self , name , age ):
        self.name = name
        self.age = age
    def greet(self):
        print("hello , my name is" , self.name , "and my age is " ,self.age)
    

p1 = Person("bilal " , 21)
p1.greet()


class Student :
    def __init__(self , name , grade):
        self.name = name
        self.grade = grade
    def show_inf(self):
        print("my name is ",self.name , "and my grade is " , self.grade)
    def is_passed(self):
        if(self.grade>=10):
            print("is passed")
        else : 
            print("failed") 

p2 =Student("hicahm" , 10)

p2.show_inf()
p2.is_passed()


   