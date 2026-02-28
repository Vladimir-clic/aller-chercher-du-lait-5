#ce fichier contient toutes les classes

#initialisation de la classe joueur
class joueur :
    def __init__(self, id, nom, argent, vaches, jour, lait):
        self.id = id
        self.nom = nom
        self.argent = argent
        self.vaches = vaches
        self.jour = jour
        self.lait = lait

#initialisation de la classe vache
class vache :
    def __init__(self, id, nom, prix, lait, nombre):
        self.id = id
        self.nom = nom 
        self.prix = prix
        self.lait = lait
        self.nombre = nombre