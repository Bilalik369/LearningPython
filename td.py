class Etudaint:
    def __init__(self , id , nom , prenom , note):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.__note = note  

    def afficher(self):
        print("Les informations de l'etudiant :", 
              self.id, self.nom, self.prenom, self.__note)
    
    def est_admis(self):
        if self.__note >= 10:
            print("Admis")
        else:
            print("Non admis")

    def getNote(self):
        return self.__note
    
    def setNote(self , val):
        if 0 <= val <= 20:
            self.__note = val
        else:
            print("Note invalide")


e1 = Etudaint(2, "ahmed", "brahim", 12)

e1.afficher()
e1.est_admis()

e1.setNote(18)
print("Nouvelle note :", e1.getNote())
