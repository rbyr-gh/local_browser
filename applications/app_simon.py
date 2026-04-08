import customtkinter as ctk
import random
from local.couleur import *

class frame_Simon(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=couleur_Fond)

        # Variables
        self.niveau = 1
        self.sequence = []
        self.reponse_joueur = []
        self.couleurs = ["green", "red", "yellow", "blue"]

        self.labelSimon = ctk.CTkLabel(
            self,
            text=f"NIVEAU {self.niveau}",
            font=("Arial", 20, "bold")
        )
        self.labelSimon.pack(pady=20)

        self.grid_frame = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.grid_frame.pack()

        self.bouton_vert = self.create_btn("green", "#2ecc71", "#27ae60")
        self.bouton_rouge = self.create_btn("red", "#e74c3c", "#c0392b")
        self.bouton_jaune = self.create_btn("yellow", "#f1c40f", "#d4ac0d")
        self.bouton_bleu = self.create_btn("blue", "#3498db", "#2980b9")

        self.bouton_vert.grid(row=0, column=0, padx=10, pady=10)
        self.bouton_rouge.grid(row=0, column=1, padx=10, pady=10)
        self.bouton_jaune.grid(row=1, column=0, padx=10, pady=10)
        self.bouton_bleu.grid(row=1, column=1, padx=10, pady=10)

        self.btn_rejouer = ctk.CTkButton(
            self,
            text="Rejouer",
            command=self.reset,
            fg_color=couleur_Bouton2,
            hover_color=couleur_Surbrillance,
            text_color=couleur_Texte1
        )
        self.btn_rejouer.pack(pady=20)

        # Lancer le jeu
        self.ajouter_couleur()
        self.jouer_sequence()

    def create_btn(self, couleur, base, hover):
        return ctk.CTkButton(
            self.grid_frame,
            command=lambda: self.clic(couleur),
            fg_color=base,
            hover_color=hover,
            corner_radius=20,
            width=150,
            height=150,
            text=""
        )

    def ajouter_couleur(self):
        self.sequence.append(random.choice(self.couleurs))

    def flash(self, bouton, couleur):
        bouton.configure(fg_color="white")
        self.update()
        self.after(200)
        bouton.configure(fg_color=couleur)
        self.update()
        self.after(200)

    def jouer_sequence(self):
        for couleur in self.sequence:
            if couleur == "green":
                self.flash(self.bouton_vert, "#2ecc71")
            elif couleur == "red":
                self.flash(self.bouton_rouge, "#e74c3c")
            elif couleur == "yellow":
                self.flash(self.bouton_jaune, "#f1c40f")
            elif couleur == "blue":
                self.flash(self.bouton_bleu, "#3498db")

    def clic(self, couleur):
        self.reponse_joueur.append(couleur)
        self.verifier()

    def verifier(self):
        if self.reponse_joueur == self.sequence[:len(self.reponse_joueur)]:
            if len(self.reponse_joueur) == len(self.sequence):
                self.passer_niveau()
        else:
            self.perdu()

    def passer_niveau(self):
        self.niveau += 1
        self.labelSimon.configure(text=f"NIVEAU {self.niveau}")
        self.reponse_joueur.clear()
        self.ajouter_couleur()
        self.after(500, self.jouer_sequence)

    def perdu(self):
        self.labelSimon.configure(text="PERDU !")

    def reset(self):
        self.sequence.clear()
        self.reponse_joueur.clear()
        self.niveau = 1
        self.labelSimon.configure(text=f"NIVEAU {self.niveau}")
        self.ajouter_couleur()
        self.jouer_sequence()