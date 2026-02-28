import tkinter as tk

# créer la fenêtre
fenetre = tk.Tk()
fenetre.title("Formulaire simple")
fenetre.geometry("300x200")

# champ texte (comme <input> en HTML)
entry = tk.Entry(fenetre)
entry.pack()

# label pour afficher le résultat
label_resultat = tk.Label(fenetre, text="")
label_resultat.pack()

# fonction appelée quand on clique
def valider():
    nom = entry.get()  # récupère ce qui est tapé
    label_resultat.config(text="Bonjour " + nom)

# bouton
tk.Button(fenetre, text="Valider", command=valider).pack()

# boucle tkinter
fenetre.mainloop()