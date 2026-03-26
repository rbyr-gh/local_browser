import customtkinter as ctk
from tkinter import Canvas
import random

black = "gray90"
white = "gray15"

couleur_Fond = (black,"grey15")
couleur_Bouton = ("DarkOrange1","DarkOrange3")
couleur_Surbrillance = ("grey74","grey43")


class frame_Snake(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # =============================
        # 🔹 CONFIG
        # =============================
        self.TAILLE_CASE = 20
        self.LARGEUR = 25
        self.HAUTEUR = 25

        # =============================
        # 🔹 CANVAS
        # =============================
        self.cnv = Canvas(
            self,
            width=self.TAILLE_CASE*self.LARGEUR,
            height=self.TAILLE_CASE*self.HAUTEUR,
            bg="black"
        )
        self.cnv.pack(pady=20)

        # =============================
        # 🔹 BOUTON RESTART
        # =============================
        self.restart_btn = ctk.CTkButton(
            self,
            text="Rejouer",
            command=self.restart,
            fg_color=couleur_Bouton,
            hover_color=couleur_Surbrillance
        )

        # =============================
        # 🔹 VARIABLES
        # =============================
        self.snake_body = []
        self.direction = "Right"
        self.pomme = (0,0)
        self.jeu_en_cours = True

        # =============================
        # 🔹 EVENTS
        # =============================
        self.cnv.bind("<Key>", self.key)
        self.cnv.focus_set()

        self.init_game()

    # =============================
    # 🔹 INIT GAME
    # =============================
    def init_game(self):
        self.cnv.focus_set()  

        self.snake_body = [(15,15), (14,15), (13,15)]
        self.direction = "Right"
        self.pomme = self.nouvelle_pomme()
        self.jeu_en_cours = True

        self.restart_btn.pack_forget()

        self.draw()
        self.move()

    # =============================
    # 🔹 DESSIN
    # =============================
    def draw(self):
        self.cnv.delete("all")

        # Snake
        for x,y in self.snake_body:
            self.cnv.create_rectangle(
                x*self.TAILLE_CASE, y*self.TAILLE_CASE,
                x*self.TAILLE_CASE+self.TAILLE_CASE,
                y*self.TAILLE_CASE+self.TAILLE_CASE,
                fill="green"
            )

        # Pomme
        x,y = self.pomme
        self.cnv.create_rectangle(
            x*self.TAILLE_CASE, y*self.TAILLE_CASE,
            x*self.TAILLE_CASE+self.TAILLE_CASE,
            y*self.TAILLE_CASE+self.TAILLE_CASE,
            fill="red"
        )

    # =============================
    # 🔹 MOUVEMENT
    # =============================
    def move(self):
        if not self.jeu_en_cours:
            return

        x,y = self.snake_body[0]

        if self.direction == "Up":
            y -= 1
        elif self.direction == "Down":
            y += 1
        elif self.direction == "Left":
            x -= 1
        elif self.direction == "Right":
            x += 1

        # Collision
        if (x<0 or x>=self.LARGEUR or
            y<0 or y>=self.HAUTEUR or
            (x,y) in self.snake_body):

            self.jeu_en_cours = False

            self.cnv.create_text(
                self.LARGEUR*self.TAILLE_CASE//2,
                self.HAUTEUR*self.TAILLE_CASE//2,
                text="GAME OVER",
                fill="white",
                font=("Arial",30,"bold")
            )

            self.restart_btn.pack(pady=10)
            return

        # Nouveau head
        self.snake_body = [(x,y)] + self.snake_body

        # Mange pomme
        if (x,y) == self.pomme:
            self.pomme = self.nouvelle_pomme()
        else:
            self.snake_body.pop()

        self.draw()
        self.after(100, self.move)

    # =============================
    # 🔹 POMME
    # =============================
    def nouvelle_pomme(self):
        while True:
            p = (
                random.randint(0,self.LARGEUR-1),
                random.randint(0,self.HAUTEUR-1)
            )
            if p not in self.snake_body:
                return p

    # =============================
    # 🔹 CONTROLES
    # =============================
    def key(self, event):
        opposés = {
            "Up":"Down",
            "Down":"Up",
            "Left":"Right",
            "Right":"Left"
        }

        if event.keysym in opposés:
            if self.direction != opposés[event.keysym]:
                self.direction = event.keysym

    # =============================
    # 🔹 RESTART
    # =============================
    def restart(self):
        self.init_game()