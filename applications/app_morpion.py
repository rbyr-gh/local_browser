import customtkinter as ctk
from tkinter import Canvas, Toplevel
import random

black = "gray90"
white = "gray15"

couleur_Fond2 = ("grey95","grey23")
couleur_Fond = (black,"grey15")
couleur_Widget = ("grey74","grey43")
couleur_Bouton1 = (black,"grey3")
couleur_Bouton2 = ("DarkOrange1","DarkOrange3")
couleur_Surbrillance =("grey74","grey43")
couleur_Bord = (white,black)
couleur_Texte1 = (white,black)
couleur_Texte2 = ("grey26","grey80")


class frame_Morpion(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # 🔹 Variables (IMPORTANT : plus de global)
        self.tab1 = [[0,0,0],[0,0,0],[0,0,0]]
        self.tour = 1

        # 🔹 Labels CTk
        self.joueur1 = ctk.CTkLabel(self, text="Joueur 1 : O")
        self.joueur1.pack(pady=5)

        self.joueur2 = ctk.CTkLabel(self, text="Ordinateur : X")
        self.joueur2.pack(pady=5)

        # 🔹 Canvas (reste Tkinter, normal)
        self.cnv = Canvas(self, width=1200, height=600, bg="aquamarine3")
        self.cnv.pack(pady=10)

        self.dessiner_grille()

        # 🔹 Bouton CTk
        self.btn_rejouer = ctk.CTkButton(self, text="Rejouer", command=self.vider,fg_color=couleur_Fond,text_color="aquamarine3",hover_color=couleur_Surbrillance)
        self.btn_rejouer.pack(pady=10)

        self.cnv.bind("<Button-1>", self.clic)

    # =============================
    # 🔹 Dessin grille
    # =============================
    def dessiner_grille(self):
        self.cnv.delete("all")
        self.cnv.create_line(525,75,525,525,fill="aquamarine4",width=10)
        self.cnv.create_line(675,75,675,525,fill="aquamarine4",width=10)
        self.cnv.create_line(375,225,825,225,fill="aquamarine4",width=10)
        self.cnv.create_line(375,375,825,375,fill="aquamarine4",width=10)

    # =============================
    # 🔹 Reset
    # =============================
    def vider(self):
        self.tab1 = [[0,0,0],[0,0,0],[0,0,0]]
        self.tour = 1
        self.dessiner_grille()

    # =============================
    # 🔹 Victoire
    # =============================
    def victoire_test(self, j):
        t = self.tab1
        for i in range(3):
            if t[i][0]==t[i][1]==t[i][2]==j:
                return True
        for j2 in range(3):
            if t[0][j2]==t[1][j2]==t[2][j2]==j:
                return True
        if t[0][0]==t[1][1]==t[2][2]==j:
            return True
        if t[0][2]==t[1][1]==t[2][0]==j:
            return True
        return False

    def fenetreVictoire(self, joueur):
        win = ctk.CTkToplevel(self)
        win.geometry("300x200")
        win.attributes("-topmost", True)

        label = ctk.CTkLabel(win, text=f"Victoire de {joueur}")
        label.pack(pady=20)

        btn = ctk.CTkButton(win, text="OK", command=win.destroy)
        btn.pack()

        self.vider()

    def verifVictoire(self, joueur):
        if self.victoire_test(joueur):
            self.fenetreVictoire(joueur)

    # =============================
    # 🔹 IA
    # =============================
    def coup_aleatoire(self):
        cases = [(i,j) for i in range(3) for j in range(3) if self.tab1[i][j]==0]
        return random.choice(cases) if cases else None

    def ordinateur(self):
        coup = self.coup_aleatoire()
        if coup:
            i,j = coup
            self.tab1[i][j] = 2
            self.dessiner_x(i,j)
            self.tour = 1
            self.verifVictoire(2)

    # =============================
    # 🔹 Dessins
    # =============================
    def dessiner_o(self,i,j):
        coords = self.get_coords(i,j)
        self.cnv.create_oval(*coords, outline="grey30", width=8)

    def dessiner_x(self,i,j):
        x1,y1,x2,y2 = self.get_coords(i,j)
        self.cnv.create_line(x1,y1,x2,y2, fill="grey90", width=8)
        self.cnv.create_line(x2,y1,x1,y2, fill="grey90", width=8)

    def get_coords(self,i,j):
        base_x = 375 + j*150
        base_y = 75 + i*150
        return (base_x+15, base_y+15, base_x+135, base_y+135)

    # =============================
    # 🔹 Clic joueur
    # =============================
    def clic(self, event):
        if self.tour != 1:
            return

        x,y = event.x, event.y

        i = (y-75)//150
        j = (x-375)//150

        if 0 <= i < 3 and 0 <= j < 3:
            if self.tab1[i][j] == 0:
                self.tab1[i][j] = 1
                self.dessiner_o(i,j)

                self.verifVictoire(1)

                self.tour = 2
                self.after(300, self.ordinateur)