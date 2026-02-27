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



prixventelait = 1


#création des vaches
vache1 = vache(1,"Vache normale", 3, 1, 0)
vache2 = vache(2,"Vache qualitative", 7, 2, 0)
vache3 = vache(3,"Vache d'élite", 32, 4, 0)

listevache = [vache1, vache2, vache3]
listejoueur = []

#joueur temporaire pour tester les sauvegardes
#j1 = joueur(4, "joueur 4", 15, [], 58, 4)
#listejoueur.append(j1)
#j2 = joueur(5, "joueur 5", 47, [], 1, 0)
#listejoueur.append(j2)

#ajout des vaches aux joueurs
#for j in listejoueur : 
    #for v in listevache :
        #j.vaches.append(v)




#début du jeu
class game : 
    def menu ():
        print("vous êtes entrés dans le menu")
        menu1 = int
        # while menu1 !=1 :
        menu1 = input("Bienvenue dans Vache à lait, le nouveau jeu à la mode \n" \
            " ------------MENU-------------- \n" \
            "Entrez un chiffre pour choisi une option \n" \
            "1) Nouvelle partie \n" \
            "2) Continue (pas encore paramétré)\n"
            "3) Options\n")

        menu1 = int(menu1)
        print(f"vous avez choisi {menu1}")

        if menu1 == 1 : 
                partie.debutjeu()
        elif menu1 == 2 :
                continuepartie.reprisejeu()
        elif menu1 == 3 :
                partie.options()
        else : 
                print("non, je ne crois pas")
                return 0
    
class continuepartie :
    def reprisejeu() : 
        
        print("Liste des sauvegardes : \n"
        "------------------------------------")

        if len(listejoueur) == 0 :
            print("Erreur, aucune sauvegarde enregistrée, veuillez créer un nouveau profil")
            print("------------------------------------ \n")
            partie.debutjeu()

        else : 
            for i in listejoueur :
                print(f"{i.id}) {i.nom} | {i.argent} Lacteuros | {i.lait} Litre de lait | {i.jour} jours")
            print("------------------------------------ \n")
            charger = int(input("Choisissez la sauvegarde à charger : \n"))
            for i in listejoueur : 
                print(f"on lance la boucle avec {i.nom}")
                if i.id == charger :
                    partie.bouclepartie(i)
            print("ID invalide.")
            continuepartie.reprisejeu()



class partie :

    def debutjeu() :
        print("------------Création de personnage---------------\n")
        print("partie lancée")

        


        # Génération automatique de l'id
        if len(listejoueur) == 0:
            nouvel_id = 1
        else:
            nouvel_id = max(j.id for j in listejoueur) + 1

        #création du joueur
        nomdujoueur = input("Comment t'appelles tu ?\n")
        print(nomdujoueur)
        
        joueur1 = joueur(nouvel_id, nomdujoueur, 3, [], 1, 0)
        listejoueur.append(joueur1)

        print(f"Profil créé avec l'id {joueur1.id}")





        
        joueur1.vaches.append(vache1)
        joueur1.vaches.append(vache2)
        joueur1.vaches.append(vache3)

        partie.bouclepartie(joueur1)



    def bouclepartie(j) :
        print(f"----------JOUR {j.jour}----------\n\n"
                    f"-Joueur : {j.nom}\n"
                    f"-Lacteuros : {j.argent}\n"
                    f"-Litre de lait : {j.lait}L\n"
                    f"")
        #while not j.argent > 100:
        #for i in range(10) : 
        #a = 1
        #if a == 1 : 
        while True : 



            optionjour1 = input(f"Que voulez vous faire aujourd'hui {j.nom} ?\n \n"
                    "1) Acheter une vache\n"
                    "2) Vendre du lait\n"
                    "3) Se recoucher\n"
                    "4) Voir le troupeau\n"
                    "5) Menu \n")
            
            optionjour = int(optionjour1)

            if optionjour == 1 :
                partie.achetervache(j)
            elif optionjour == 2 :
                partie.vendredulait(j)
            elif optionjour == 3 :
                partie.serecoucher(j)
            elif optionjour == 4 :
                partie.troupeau(j)
            elif optionjour == 5 :
                partie.options()
            else : 
                pass

        print("BRAVO ! Vous avez gagné le jeux, en espérant vous revoir bientôt !")



    def achetervache(j) :
        print(f"\n\n {j.nom} part à la ferme acheter une vache \n")
        for k in j.vaches :
            print(f"{k.id}) {k.nom} : prix : {k.prix}, production : {k.lait} ")

        reponsestr = input("\nQuelle vache souhaites-tu acheter ? \n")
        reponseint = int(reponsestr)

        for k in j.vaches :
            if reponseint == k.id :

                if j.argent >= k.prix :
                    #print(f"{j.nom} à {j.argent} lacteuros, c'est suffisant pour acheter {k.nom} à {k.prix} lacteuros")
                    #print(j.vaches)
                    k.nombre = k.nombre + 1
                    #print(j.vaches)
                    j.argent = j.argent - k.prix
                    #print(f"Après la transaction, {j.nom} à {j.argent} lacteuros")
                    print(f"Vous avez acheté une {k.nom}")
                    

                elif j.argent < k.prix :

                    print(f"Désolé {j.nom}, vous n'avez que {j.argent}, c'est trop peu pour achete une {k.nom} qui coute {k.prix}")
                    #faire revenir à l'achat de la vache (pour refaire)



    def vendredulait(j) : 
        print(f"\n\n {j.nom} part au marché pour vendre du lait, il a {j.lait} \n")
        if j.lait == 0 :
            print("Mince, il semble que tu n'ai pas d'argent... si triste")

        else :
            j.argent = (j.lait * prixventelait) + j.argent
            print(f"Félicitation, vous avez gagné {j.lait * prixventelait} lacteuros")
            j.lait = 0




    def serecoucher(j) : 
        j.jour = j.jour + 1
        for k in j.vaches :
            j.lait = j.lait + (k.lait * k.nombre)

        partie.bouclepartie(j)
            


    def troupeau(j) : 
        print(f"----------BIENVENUE DANS VOTRE TROUPEAU----------\n")
        for i in j.vaches :
            if i.nombre > 0 :
                print(f"{i.nom} × {i.nombre} ")
        print(f"\n ------------------------------------------------\n")



    def options() : 
        print(f"-----------OPTIONS-----------")
        optionchoisi = input(f"Liste options \n \n"
                    "1) Revenir au menu\n")
        if optionchoisi == 1 :
            print('entrée dans le menu')
            #game.menu()
        print("fin des options")
        game.menu()
            
                    

game.menu()
