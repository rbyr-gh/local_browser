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

# Création d'un nouveau widget

class BoutonNote(ctk.CTkFrame):
    def __init__(self, parent, nom, on_delete=None, on_click=None):
        super().__init__(parent, fg_color="transparent")

        # Bouton principal 
        self.btn = ctk.CTkButton(self, text=nom, height=35, anchor="w",fg_color="transparent", text_color="DeepPink3",border_width=3, border_color="DeepPink3",hover_color=("gray85", "gray25"),command=on_click)
        self.btn.pack(side="left", fill="x", expand=True, pady=2)

        # Bouton supprimer
        self.btn_delete = ctk.CTkButton(self, text="✕", width=30, height=35,fg_color="transparent", text_color="DeepPink3",hover_color=("gray85", "gray25"),command=lambda: self.supprimer(on_delete))
        self.btn_delete.pack(side="right", pady=2)

    def supprimer(self, on_delete):
        if on_delete:
            on_delete()       # callback personnalisé (ex: retirer de la liste)
        self.destroy() 

# Class de fonctionnement l'app Notes

class frame_Note(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  

        frame_menu_note = ctk.CTkFrame(self, width=250)
        frame_menu_note.grid(row=0, column=0, sticky="ns")
        frame_menu_note.grid_rowconfigure(1, weight=1) 
        frame_menu_note.grid_columnconfigure(0, weight=1)
        frame_menu_note.grid_columnconfigure(1, weight=1)
        frame_menu_note.grid_propagate(False)  

        frame_notes = ctk.CTkFrame(self, fg_color="DeepPink3")
        frame_notes.grid(row=0, column=1, sticky="nsew")
        frame_notes.grid_rowconfigure(0, weight=1)
        frame_notes.grid_columnconfigure(0, weight=1)

        textbox = ctk.CTkTextbox(frame_notes)
        textbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        titre = ctk.CTkLabel(frame_menu_note, text="MES NOTES", text_color="DeepPink3", font=ctk.CTkFont(size=20))
        titre.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,10), sticky="n")

        notes = ["Note 1", "Note 2", "Note 3"]  # à récupérer avec le fichier notes.txt'

        def charger_note(nom):
            textbox.delete("1.0", "end")
            textbox.insert("1.0", f"Contenu de {nom}")
        scrollable = ctk.CTkScrollableFrame(frame_menu_note, width=180)
        scrollable.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  

        for nom in notes:
            def on_delete(n=nom):
                notes.remove(n)
            bouton = BoutonNote(scrollable, nom=nom, on_delete=on_delete, on_click=lambda n=nom: charger_note(n))
            bouton.pack(fill="x", padx=5, pady=2)

        btn_create_notes = ctk.CTkButton(frame_menu_note, text="+", text_color="DeepPink3", border_width=3, border_color="DeepPink3", fg_color="transparent", hover_color=("gray85", "gray25"), command=lambda : create_notes(parent, scrollable, notes))
        btn_create_notes.grid(row=2, column=0, padx=5, pady=10)

        btn_autre_notes = ctk.CTkButton(frame_menu_note, text="à voir", text_color="DeepPink3", border_width=3, border_color="DeepPink3", fg_color="transparent", hover_color=("gray85", "gray25"))
        btn_autre_notes.grid(row=2, column=1, padx=5, pady=10)

        def create_notes(parent,scrollable,L):
            fenetre_create_note = ctk.CTkToplevel()
            largeur, hauteur = 300, 150

            # Récupère la position et taille de la fenêtre principale
            x_parent = parent.winfo_x()
            y_parent = parent.winfo_y()
            w_parent = parent.winfo_width()
            h_parent = parent.winfo_height()

            # Calcule le centre
            x = x_parent + (w_parent // 2) - (largeur // 2)
            y = y_parent + (h_parent // 2) - (hauteur // 2)

            fenetre_create_note.geometry(f"{largeur}x{hauteur}+{x}+{y}")
            fenetre_create_note.title("Création d'une nouvelle note")
            fenetre_create_note.grab_set()  

            entry = ctk.CTkEntry(fenetre_create_note, placeholder_text="Nom de la note...")
            entry.pack(padx=20, pady=20)

            def valider(L):
                nom = entry.get()
                if nom.strip():
                    L.append(nom)
                    def on_delete(n=nom):
                        L.remove(n)
                    bouton = BoutonNote(scrollable, nom=nom, on_delete=on_delete, on_click=lambda n=nom: charger_note(n))
                    bouton.pack(fill="x", padx=5, pady=2)
                    fenetre_create_note.destroy() 

            btn = ctk.CTkButton(fenetre_create_note, text="Valider", text_color="DeepPink3", border_width=3, border_color="DeepPink3", fg_color="transparent", hover_color=("gray85", "gray25"), command=lambda :valider(L))
            btn.pack(pady=5)

        def Lire_notes_txt():
            pass

        def Ecrire_notes_tkt():
            pass

