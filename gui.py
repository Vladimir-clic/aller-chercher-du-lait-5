#interface tkinter

#imports
import tkinter as tk
from model import joueur
from gamelogic import achetervache, vendredulait, serecoucher, troupeau

class GameGUI():
    def __init__(self):
        self.joueur = joueur(1, "Alex", 10, troupeau, 1, 0)

        #définition de la fenêtre
        #super().__init__()
        self.fenetre = tk.Tk()
        self.fenetre.title("Vache à Lait 🐄")
        self.fenetre.geometry("400x400")

        self.label_info = tk.Label(self.fenetre)
        self.label_info.pack()



        # conteneur principal
        container = tk.Frame(self.fenetre)
        container.pack(fill="both", expand=True)

        # dictionnaire pour stocker les pages
        self.frames = {}

        # création des pages
        for Page in (Menu, Newgame, Continue):
            frame = Page(container, self)
            self.frames[Page] = frame
            self.frames[Page].grid(row=0, column=0, sticky="nsew")

        # afficher la première page
        self.show_frame(Menu)
        self.fenetre.mainloop()


    def show_frame(self, page):
        #frame = self.frames[page]
        self.frames[page].tkraise()


# =========================
# PAGE 1 : MENU
# =========================

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="MENU", font=("Arial", 20)).pack(pady=20)

        tk.Button(
            self,
            text="Nouvelle partie",
            command=lambda: controller.show_frame(Newgame)
        ).pack()

        tk.Button(
            self,
            text="Continue",
            command=lambda: controller.show_frame(Continue)
        ).pack()

        tk.Button(
            self,
            text="Options",
            command=lambda: controller.show_frame(Options)
        ).pack()


# =========================
# PAGE 2 : NEW GAME
# =========================

class Newgame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Nouvelle partie", font=("Arial", 20)).pack(pady=20)

        # champ texte (comme <input> en HTML)
        entry = tk.Entry(self)
        entry.pack()

        # label pour afficher le résultat
        label_resultat = tk.Label(self, text="")
        label_resultat.pack()



# fonction appelée quand on clique
        def valider():
            nom = entry.get()  # récupère ce qui est tapé
            label_resultat.config(text="Bonjour " + nom)

        # bouton
        tk.Button(self, text="Valider", command=valider).pack()

        tk.Button(
            self,
            text="Retour",
            command=lambda: controller.show_frame(Menu)
        ).pack()



# =========================
# PAGE 3 : CONTINUE
# =========================

class Continue(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Continue", font=("Arial", 20)).pack(pady=20)

        tk.Button(
            self,
            text="Choisir sa sauvegarde",
            command=lambda: controller.show_frame(Menu)
        ).pack()

# =========================
# PAGE 4 : OPTIONS
# =========================

class Options(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Options", font=("Arial", 20)).pack(pady=20)





        #création des boutons
        tk.Button(self.fenetre, text="Dormir", command=self.action_dormir).pack()
        tk.Button(self.fenetre, text="Vendre lait", command=self.action_vendre).pack()

        self.mettre_a_jour()
        self.fenetre.mainloop()

    def mettre_a_jour(self):
        texte = f"Jour: {self.joueur.jour}\nArgent: {self.joueur.argent}\nLait: {self.joueur.lait}"
        self.label_info.config(text=texte)

    def action_dormir(self):
        serecoucher(self.joueur)
        self.mettre_a_jour()

    def action_vendre(self):
        vendredulait(self.joueur)
        self.mettre_a_jour()