class Etudaint :
    def __init__(self , id , nom , prenom , note):
        self.id =id
        self.nom = nom
        self.prenom = prenom
        self.note =note


    def afficher(self) :
        print("les information de l etudaitnt" ,self.id , self.nom , self.prenom , self.note)
    
    def est_admis(sefl ):
        if sefl.note >= 10 :
            print("admis")
        else :
            print("non admis")

e1 = Etudaint(2, "ahmed" , "brahim" , 12)
e1.afficher()
e1.est_admis()
