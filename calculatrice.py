from math import *
from customtkinter import *

def calculatrice():
    fenetre = CTk()
    fenetre.title("calculatrice")
    fenetre.geometry("500x600")

    menu = CTkFrame(fenetre)
    menu.place(x=0, y=0, relwidth=1, relheight=1)


    # écran
    ecran = CTkEntry(menu, width=400, height=50)
    ecran.place(x=50, y=30)

    # fonctions pour le calcul
    def cliquer(valeur):
        ecran.insert("end", str(valeur))

    def calculer():
        try:
            resultat = eval(ecran.get())
            ecran.delete(0, "end")
            ecran.insert(0, str(resultat))
        except:
            ecran.delete(0, "end")
            ecran.insert(0, "Erreur")

    def effacer():
        ecran.delete(0, "end")

    # fonctions pour chaque bouton
    def bouton_0(): cliquer("0")
    def bouton_1(): cliquer("1")
    def bouton_2(): cliquer("2")
    def bouton_3(): cliquer("3")
    def bouton_4(): cliquer("4")
    def bouton_5(): cliquer("5")
    def bouton_6(): cliquer("6")
    def bouton_7(): cliquer("7")
    def bouton_8(): cliquer("8")
    def bouton_9(): cliquer("9")
    def bouton_plus(): cliquer("+")
    def bouton_moins(): cliquer("-")
    def bouton_mult(): cliquer("*")
    def bouton_div(): cliquer("/")
    def bouton_point(): cliquer(".")

    # création des boutons
    CTkButton(menu, text="7", width=70, height=60, command=bouton_7).place(x=50, y=120)
    CTkButton(menu, text="8", width=70, height=60, command=bouton_8).place(x=150, y=120)
    CTkButton(menu, text="9", width=70, height=60, command=bouton_9).place(x=250, y=120)
    CTkButton(menu, text="/", width=70, height=60, command=bouton_div).place(x=350, y=120)

    CTkButton(menu, text="4", width=70, height=60, command=bouton_4).place(x=50, y=200)
    CTkButton(menu, text="5", width=70, height=60, command=bouton_5).place(x=150, y=200)
    CTkButton(menu, text="6", width=70, height=60, command=bouton_6).place(x=250, y=200)
    CTkButton(menu, text="*", width=70, height=60, command=bouton_mult).place(x=350, y=200)

    CTkButton(menu, text="1", width=70, height=60, command=bouton_1).place(x=50, y=280)
    CTkButton(menu, text="2", width=70, height=60, command=bouton_2).place(x=150, y=280)
    CTkButton(menu, text="3", width=70, height=60, command=bouton_3).place(x=250, y=280)
    CTkButton(menu, text="-", width=70, height=60, command=bouton_moins).place(x=350, y=280)

    CTkButton(menu, text="0", width=70, height=60, command=bouton_0).place(x=50, y=360)
    CTkButton(menu, text=".", width=70, height=60, command=bouton_point).place(x=150, y=360)
    CTkButton(menu, text="=", width=70, height=60, command=calculer).place(x=250, y=360)
    CTkButton(menu, text="+", width=70, height=60, command=bouton_plus).place(x=350, y=360)

    # bouton effacer
    CTkButton(menu, text="C", width=300, height=50, command=effacer).place(x=100, y=460)

    fenetre.mainloop()

calculatrice()