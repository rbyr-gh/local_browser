from random import *
from customtkinter import *

def simon():
    fenetre = CTk()
    fenetre.title("simon")
    fenetre.geometry("500x600")

    menu = CTkFrame(fenetre)
    menu.place(x=0, y=0, relwidth=1, relheight=1)

    niveau = 1
    labelSimon = CTkLabel(menu, width=400, height=50, text = f"NIVEAU {niveau}" )
    labelSimon.place(x=50, y=30)

    sequence = []
    reponse_joueur = []
    couleurs = ["green", "red", "yellow", "blue"]

    def ajouter_couleur():
      sequence.append(choice(couleurs))

    def perdu():
      labelSimon.configure(text="PERDU !")

    def passer_niveau():
        nonlocal niveau
        niveau += 1
        labelSimon.configure(text=f"NIVEAU {niveau}")
        reponse_joueur.clear()
        ajouter_couleur()
        fenetre.after(500, jouer_sequence)

    def verifier():
        if reponse_joueur == sequence[:len(reponse_joueur)]:
            if len(reponse_joueur) == len(sequence):
                passer_niveau()
        else:
            perdu()

    def clic(couleur):
         reponse_joueur.append(couleur)
         verifier()


    def jouer_sequence():
        for couleur in sequence:
            if couleur == "green":
                clignote(bouton_vert, "green")
            elif couleur == "red":
                clignote(bouton_rouge, "red")
            elif couleur == "yellow":
                clignote(bouton_jaune, "yellow")
            elif couleur == "blue":
                clignote(bouton_bleu, "blue")


    def clignote(bouton,couleur):       
        bouton.configure(fg_color="white")
        fenetre.update()
        fenetre.after(300)
        bouton.configure(fg_color=couleur)
        fenetre.update()
        fenetre.after(300)

    bouton_vert = CTkButton(menu, command=lambda: clic("green"), fg_color="green")
    bouton_rouge = CTkButton(menu, command=lambda: clic("red"), fg_color="red")
    bouton_jaune = CTkButton(menu, command=lambda: clic("yellow"), fg_color="yellow")
    bouton_bleu = CTkButton(menu, command=lambda: clic("blue"), fg_color="blue")




        


    
    fenetre.mainloop()


simon()