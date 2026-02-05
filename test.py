
# print("hello word")

# class Person : 
#     def __init__(self , name , age ):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("hello , my name is" , self.name , "and my age is " ,self.age)
    

# p1 = Person("bilal " , 21)
# p1.greet()


# class Student :
#     def __init__(self , name , grade):
#         self.name = name
#         self.grade = grade
#     def show_inf(self):
#         print("my name is ",self.name , "and my grade is " , self.grade)
#     def is_passed(self):
#         if(self.grade>=10):
#             print("is passed")
#         else : 
#             print("failed") 

# p2 =Student("hicahm" , 10)

# p2.show_inf()
# p2.is_passed()

# class Banck : 
#     def __init__(self, name , balnce):
#         self.sum = 0
#         self.name = name
#         self.balnce = balnce
#     def show(self) :
#         print("hey M.", self.name)
#         print("Bilance", self.balnce)
#     def desposit(self , anmout):
#         self.balnce+=anmout
#         print("Desposite" , anmout,"DH")
#     def nks(self , anmout) :
#         if anmout <= self.balnce :
#             self.balnce -= anmout
#             print("Withdraw:", anmout, "DH")

#         else :
#             print("not enough money")


# acc = Banck("bilal" , 200)
# acc.desposit(122)   
# acc.nks(100)
# acc.show()

x = int(input("Entrez votre salaire : "))

if x < 5000:
    print("Votre impôt est 0%")
elif x >= 5000 and x < 10000:
    impot = x * 0.10
    print("Votre impôt est de", impot, "DH")
else:  
    impot = x * 0.20
    print("Votre impôt est de", impot, "DH")
