#ce fichier contient toutes les règles du jeu

from model import joueur, vache

prixventelait = 1








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
        