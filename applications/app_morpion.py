import customtkinter as ctk
from tkinter import Canvas, Toplevel
import random


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
        self.cnv = Canvas(self, width=600, height=600, bg="white")
        self.cnv.pack(pady=10)

        self.dessiner_grille()

        # 🔹 Bouton CTk
        self.btn_rejouer = ctk.CTkButton(self, text="Rejouer", command=self.vider)
        self.btn_rejouer.pack(pady=10)

        self.cnv.bind("<Button-1>", self.clic)

    # =============================
    # 🔹 Dessin grille
    # =============================
    def dessiner_grille(self):
        self.cnv.delete("all")
        self.cnv.create_rectangle(75,75,525,525,outline="black")
        self.cnv.create_line(225,75,225,525)
        self.cnv.create_line(375,75,375,525)
        self.cnv.create_line(75,225,525,225)
        self.cnv.create_line(75,375,525,375)

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
        self.cnv.create_oval(*coords, outline="blue", width=3)

    def dessiner_x(self,i,j):
        x1,y1,x2,y2 = self.get_coords(i,j)
        self.cnv.create_line(x1,y1,x2,y2, fill="red", width=3)
        self.cnv.create_line(x2,y1,x1,y2, fill="red", width=3)

    def get_coords(self,i,j):
        base_x = 75 + j*150
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
        j = (x-75)//150

        if 0 <= i < 3 and 0 <= j < 3:
            if self.tab1[i][j] == 0:
                self.tab1[i][j] = 1
                self.dessiner_o(i,j)

                self.verifVictoire(1)

                self.tour = 2
                self.after(300, self.ordinateur)