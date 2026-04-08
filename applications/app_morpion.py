import customtkinter as ctk
from tkinter import Canvas, Toplevel
import random
from PIL import Image

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
        
        self.r = 1

        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
    
        self.tab1 = [[0,0,0],[0,0,0],[0,0,0]]
        self.tour = 1
        self.c_score1 = 0
        self.c_score2 = 0

        self.joueur1 = ctk.CTkFrame(self,border_width=2,corner_radius=10,border_color=couleur_Bord,fg_color=couleur_Fond)
        self.joueur1.grid(row=0,column=1,sticky="ns",padx=(250,0),ipadx=50,ipady=5,pady=(20,0))
        
        self.joueur1.grid_rowconfigure(0,weight=1)
        self.joueur1.grid_columnconfigure(0,weight=1)
        self.joueur1.grid_columnconfigure(1,weight=1)
        
        self.texte1 = ctk.CTkLabel(self.joueur1,text="X",font=("Arial",24,"bold"))
        self.texte1.grid(row=0,column=0,sticky="w",ipadx=10,ipady=10,padx=10)
        
        self.score1 = ctk.CTkLabel(self.joueur1,text=f"{self.c_score2}",font=("Arial",24),text_color=couleur_Texte2)
        self.score1.grid(row=0,column=1,sticky="e",ipadx=10,ipady=10,padx=(0,10))

        self.joueur2 = ctk.CTkFrame(self,border_width=2,corner_radius=10,border_color="aquamarine4",fg_color=couleur_Fond)
        self.joueur2.grid(row=0,column=1,sticky="ns",padx=(0,250),ipadx=50,ipady=5,pady=(20,0))
        
        self.joueur2.grid_rowconfigure(0,weight=1)
        self.joueur2.grid_columnconfigure(0,weight=1)
        self.joueur2.grid_columnconfigure(1,weight=1)
        
        self.texte2 = ctk.CTkLabel(self.joueur2,text=f"O",font=("Arial",24,"bold"))
        self.texte2.grid(row=0,column=0,sticky="w",ipadx=10,ipady=10,padx=10)
        
        self.score2 = ctk.CTkLabel(self.joueur2,text=f"{self.c_score1}",font=("Arial",24),text_color=couleur_Texte2)
        self.score2.grid(row=0,column=1,sticky="e",ipadx=10,ipady=10,padx=(0,10))

        self.cnv = Canvas(self, width=1200*self.r, height=600*self.r, bg="aquamarine3")
        self.cnv.grid(row=1,column=1)

        self.dessiner_grille()

        self.btn_rejouer = ctk.CTkButton(self,text="Rejouer", command=self.vider,fg_color=couleur_Fond,text_color="aquamarine3",hover_color=couleur_Surbrillance,border_width=1,border_color="aquamarine3")
        self.btn_rejouer.grid(row=0,column=1,sticky="w",padx=(130,0),pady=(20,0))

        self.cnv.bind("<Button-1>", self.clic)

    def dessiner_grille(self):
        self.cnv.delete("all")
        self.cnv.create_line(525*self.r,75*self.r,525*self.r,525*self.r,fill="aquamarine4",width=10)
        self.cnv.create_line(675*self.r,75*self.r,675*self.r,525*self.r,fill="aquamarine4",width=10)
        self.cnv.create_line(375*self.r,225*self.r,825*self.r,225*self.r,fill="aquamarine4",width=10)
        self.cnv.create_line(375*self.r,375*self.r,825*self.r,375*self.r,fill="aquamarine4",width=10)

    def vider(self):
        self.tab1 = [[0,0,0],[0,0,0],[0,0,0]]
        self.tour = 1
        self.dessiner_grille()

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

    def egalite_test(self):
        for ligne in self.tab1:
            if 0 in ligne:
                return False
        return True   

    def fenetreVictoire(self, joueur):
        self.cnv.delete("all")
        
        if joueur == 1 :
            self.c_score2 += 1
            self.score2.configure(text=f'{self.c_score2}')
            self.cnv.create_text(600,450,text="GAGNÉ !",fill="grey30",font=("Arial",50,"bold"))
            self.cnv.create_oval(475,125,725,375, outline="grey30", width=20) # 300,200
        elif joueur == 2 :
            self.c_score1 += 1
            self.score1.configure(text=f"{self.c_score1}")
            self.cnv.create_text(600,450,text="GAGNÉ !",fill="grey30",font=("Arial",50,"bold"))
            self.cnv.create_line(475,125,725,375, fill="grey90", width=20)
            self.cnv.create_line(725,125,475,375, fill="grey90", width=20)
        elif joueur == 3:
            self.cnv.create_text(600,450,text="MATCH NUL",fill="grey30",font=("Arial",50,"bold")) #600
            self.cnv.create_oval(380,175,580,375, outline="grey30", width=20) # 300,200
            self.cnv.create_line(620,175,820,375, fill="grey90", width=20)
            self.cnv.create_line(820,175,620,375, fill="grey90", width=20)

    def verifVictoire(self, joueur):
        if self.victoire_test(joueur):
            self.fenetreVictoire(joueur)
            return True
        
        elif self.egalite_test():
            self.fenetreVictoire(3)
            return True
        
        else :
            return False

    def coup_aleatoire(self):
        cases = [(i,j) for i in range(3) for j in range(3) if self.tab1[i][j]==0]
        return random.choice(cases) if cases else None

    def ordinateur(self):
        coup = self.coup_aleatoire()
        if coup:
            self.joueur2.configure(border_color="aquamarine4")
            self.joueur1.configure(border_color=couleur_Texte1)
            i,j = coup
            self.tab1[i][j] = 2
            self.dessiner_x(i,j)
            self.tour = 1
            self.verifVictoire(2)
            
    def dessiner_o(self,i,j):
        coords = self.get_coords(i,j)
        self.cnv.create_oval(*coords, outline="grey30", width=8)

    def dessiner_x(self,i,j):
        x1,y1,x2,y2 = self.get_coords(i,j)
        self.cnv.create_line(x1,y1,x2,y2, fill="grey90", width=8)
        self.cnv.create_line(x2,y1,x1,y2, fill="grey90", width=8)

    def get_coords(self,i,j):
        base_x = (375 + j*150)
        base_y = (75 + i*150)
        return (base_x+15, base_y+15, base_x+135, base_y+135)

    def clic(self, event):
        if self.tour != 1:
            return False

        x,y = event.x, event.y

        i = (y-75)//150
        j = (x-375)//150

        if 0 <= i < 3 and 0 <= j < 3:
            if self.tab1[i][j] == 0:
                self.tab1[i][j] = 1
                self.dessiner_o(i,j)

                if not self.verifVictoire(1) :
                    self.joueur1.configure(border_color="aquamarine4")
                    self.joueur2.configure(border_color=couleur_Texte1)
                    self.after(300, self.ordinateur)
                    self.tour = 2
                
        