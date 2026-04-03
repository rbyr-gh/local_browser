import customtkinter as ctk
import tkinter as tk

black = "gray90"
white = "gray15"

couleur_Fond2 = ("grey95","grey23")
couleur_Fond = (black,"grey15")
couleur_Widget = ("grey74","grey43")
couleur_Bouton1 = (black,"grey3")
couleur_Bouton2 = ("DarkOrange1","DarkOrange3")
couleur_Bouton3 = ("cornsilk4","DarkGray")
couleur_Surbrillance =("grey74","grey43")
couleur_Bord = (white,black)
couleur_Texte1 = (white,black)
couleur_Texte2 = ("grey26","grey80")


class frame_Calculatrice(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Ecran d'affichage
        entry = ctk.CTkEntry(self, placeholder_text="Entrez votre calcul dans la calculatrice", height=30, font=ctk.CTkFont(size=20))
        entry.grid(row=0, column=0, columnspan=5, padx=(20,20), pady=(20,10), sticky="nsew")

        # Configuration de grille
        for i in range(5):
            self.columnconfigure(i, weight=1)
        for y in range(5):
            self.rowconfigure(y, weight=1)

        # boutons
        buttons = [("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3), ("C", 1, 4), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3), ("←", 2, 4), ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("x", 3, 3), ("=", 3, 4), ("0", 4, 1), (",", 4, 2), ("÷", 4, 3)]
        L_opérateur = ["=","x","÷","+","-"]
        L_autre = ["C",",","←"]
        for (text, row, col) in buttons:
            if text in L_opérateur:
                btn = ctk.CTkButton(self, text=text, fg_color= couleur_Bouton2, corner_radius= 200, command= lambda n= text: recup_valeur_bouton_entree(entry, n), hover_color=couleur_Surbrillance,font=("Arial",40,'bold'))
                btn.grid(row=row, column=col, padx= (10,10), pady=(10,10), sticky="nsew")
            elif text in L_autre:
                btn = ctk.CTkButton(self, text=text, fg_color= couleur_Bouton3, corner_radius= 200, command= lambda n= text: recup_valeur_bouton_entree(entry, n), hover_color=couleur_Surbrillance,font=("Arial",40,'bold'))
                btn.grid(row=row, column=col, padx= (10,10), pady=(10,10), sticky="nsew")
            else :
                btn = ctk.CTkButton(self, text=text, fg_color= couleur_Bouton1, corner_radius= 200,command= lambda n= text: recup_valeur_bouton_entree(entry, n), hover_color=couleur_Surbrillance,font=("Arial",40,'bold'))
                btn.grid(row=row, column=col, padx= (10,10), pady=(10,10), sticky="nsew")


        def recup_valeur_bouton_entree(entree, n):
            valeur_actuelle = entree.get()
            # Bouton reset
            if n == "C":
                entree.delete(0, "end")
            # Supprimer dernier caractère
            elif n == "←":
                entree.delete(0, "end")
                entree.insert(0, valeur_actuelle[:-1])
            # Calcul
            elif n == "=":
                try:
                    expression = valeur_actuelle.replace("x", "*").replace("÷", "/").replace(",",".")
                    resultat = str(eval(expression))
                    resultat = resultat.replace(".",",")
                    entree.delete(0, "end")
                    entree.insert(0, resultat)
                except:
                    entree.delete(0, "end")
                    entree.insert(0, "Erreur")
            # Ajouter caractère
            else:
                entree.insert("end", n)




