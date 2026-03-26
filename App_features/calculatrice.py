import customtkinter as ctk
import tkinter as tk


def calculatrice(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    # Ecran d'affichage
    entry = ctk.CTkEntry(frame, placeholder_text="Entrez votre calcul dans la calculatrice", height=30, font=ctk.CTkFont(size=20))
    entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    # Configuration de grille
    for i in range(5):
        frame.columnconfigure(i, weight=1)
    for y in range(5):
        frame.rowconfigure(y, weight=1)

    # boutons
    buttons = [("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3), ("C", 1, 4), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3), ("<-", 2, 4), ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("x", 3, 3), ("=", 3, 4), ("0", 4, 1), ("÷", 4, 3)]

    for (text, row, col) in buttons:
        btn = ctk.CTkButton(frame, text=text, command= lambda n= text: recup_valeur_bouton_entree(entry, n))
        btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    def recup_valeur_bouton_entree(entree, n):
        valeur_actuelle = entree.get()
        # Bouton reset
        if n == "C":
            entree.delete(0, "end")
        # Supprimer dernier caractère
        elif n == "<-":
            entree.delete(0, "end")
            entree.insert(0, valeur_actuelle[:-1])
        # Calcul
        elif n == "=":
            try:
                expression = valeur_actuelle.replace("x", "*").replace("÷", "/")
                resultat = str(eval(expression))
                entree.delete(0, "end")
                entree.insert(0, resultat)
            except:
                entree.delete(0, "end")
                entree.insert(0, "Erreur")
        # Ajouter caractère
        else:
            entree.insert("end", n)




