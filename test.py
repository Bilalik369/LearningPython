
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

# x = int(input("Entrez votre salaire : "))

# if x < 5000:
#     print("Votre impôt est 0%")
# elif x >= 5000 and x < 10000:
#     impot = x * 0.10
#     print("Votre impôt est de", impot, "DH")
# else:  
#     impot = x * 0.20
#     print("Votre impôt est de", impot, "DH")



class Etudaint:
    def __init__(self, code_massare, nom, prenom, adress, notes, semester):

        if len(notes) != 7:
            raise ValueError("La liste doit contenir 7 notes ")

        self.__code_massare = code_massare
        self.__nom = nom
        self.__prenom = prenom
        self.__adress = adress
        self.__notes = notes
        self.__semester = semester

 
    def get_code(self):
        return self.__code_massare

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_adress(self):
        return self.__adress

    def get_notes(self):
        return self.__notes

    def get_semester(self):
        return self.__semester


 

    def set_adress(self, adress):
        self.__adress = adress

    def set_notes(self, notes):
        if len(notes) == 7:
            self.__notes = notes
        else:
            print("Il faut 7 notes ")


 

    def afficher(self):
        print("Code:", self.__code_massare)
        print("Nom:", self.__nom)
        print("Prenom:", self.__prenom)
        print("Adresse:", self.__adress)
        print("Notes:", self.__notes)
        print("Semester:", self.__semester)




    def calcul_moyenne(self):
        return sum(self.__notes) / len(self.__notes)




    def decision(self):
        moyenne = self.calcul_moyenne()

        if moyenne >= 10:
            return "Admis "
        else:
            return "Non Admis "


        
notes=[12 , 14 , 15 , 10 , 12 , 20, 12]
s = Etudaint("A123", "Bilal", "Iken", "Rabat", notes, 1)

s.afficher()
print("Moyenne:", s.calcul_moyenne())
print("Decision:", s.decision())
        

        
