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

class frame_Note(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  

        frame_menu_note = ctk.CTkFrame(self)
        frame_menu_note.grid(row=0, column=0, sticky="ns")
        frame_menu_note.grid_rowconfigure(0, weight=1)
        frame_menu_note.grid_columnconfigure(0, weight=1)
        frame_menu_note.grid_propagate(True)  

        frame_notes = ctk.CTkFrame(self, fg_color="DeepPink3")
        frame_notes.grid(row=0, column=1, sticky="nsew")
        frame_notes.grid_rowconfigure(0, weight=1)
        frame_notes.grid_columnconfigure(0, weight=1)
        frame_notes.grid_propagate(True)

        textbox = ctk.CTkTextbox(frame_notes)
        textbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        titre = ctk.CTkLabel(frame_menu_note, text= "MES NOTES", text_color="DeepPink3", font=ctk.CTkFont(size=20))
        titre.grid(row=0, column=0, padx=10, sticky="nsw")

        
