from tkinter import *
import random

fenetre = Tk()
ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()
x = (ws/2) - (600/2)
y = (hs/2) - (600/2)
fenetre.geometry('%dx%d+%d+%d' % (600,640,x,y))
fenetre.title("Morpion")

tab1 = [[0,0,0],[0,0,0],[0,0,0]]
tour = 1

joueur1 = Label(fenetre, text = "Joueur 1 : ")
joueur1.pack(side=TOP)

joueur2 = Label(fenetre, text = "Ordinateur : ")
joueur2.pack(side=TOP)

cnv = Canvas(fenetre,width=600,height=600,bg="white")
cnv.pack()

cnv.create_rectangle(75,75,525,525,fill="white",outline="black")
cnv.create_line(225,75,225,525,fill="black")
cnv.create_line(375,75,375,525,fill="black")
cnv.create_line(75,225,525,225,fill="black")
cnv.create_line(75,375,525,375,fill="black")

def verifVictoire(tab,forme) :
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != 0:
            return fenetreVictoire(tab,forme)

    for j in range(3):
        if tab[0][j] == tab[1][j] == tab[2][j] != 0:
            return fenetreVictoire(tab,forme)

    if tab[0][0] == tab[1][1] == tab[2][2] != 0:
        return fenetreVictoire(tab,forme)

    if tab[0][2] == tab[1][1] == tab[2][0] != 0:
        return fenetreVictoire(tab,forme)
   
def fenetreVictoire(tab,forme) :
    victoire = Toplevel(fenetre,bg="white")
    x2 = (ws/2) - (450/2)
    y2 = (hs/2) - (450/2)
    victoire.geometry('%dx%d+%d+%d' % (450,450,x2,y2))
    victoire.grab_set()
    victoire.attributes("-topmost", True)
    lbl_vic = Label(victoire, text=f"Victoire de {forme}",bg="white",fg="black")
    lbl_vic.pack()
    btn_quitter2 = Button(victoire,text="Quitter",command=victoire.destroy)
    btn_quitter2.pack(side=RIGHT)
    vider()

def vider() :
    global tab1, tour
    tab1 = [[0,0,0],[0,0,0],[0,0,0]]
    tour = 1
    cnv.delete('all')
    cnv.create_rectangle(75,75,525,525,fill="white",outline="black")
    cnv.create_line(225,75,225,525,fill="black")
    cnv.create_line(375,75,375,525,fill="black")
    cnv.create_line(75,225,525,225,fill="black")
    cnv.create_line(75,375,525,375,fill="black")


def victoire_test(j):
    for i in range(3):
        if tab1[i][0]==tab1[i][1]==tab1[i][2]==j:
            return True
    for j2 in range(3):
        if tab1[0][j2]==tab1[1][j2]==tab1[2][j2]==j:
            return True
    if tab1[0][0]==tab1[1][1]==tab1[2][2]==j:
        return True
    if tab1[0][2]==tab1[1][1]==tab1[2][0]==j:
        return True
    return False

def coup_gagnant():
    for i in range(3):
        for j in range(3):
            if tab1[i][j]==0:
                tab1[i][j]=2
                if victoire_test(2):
                    tab1[i][j]=0
                    return (i,j)
                tab1[i][j]=0
    return None

def coup_blocage():
    for i in range(3):
        for j in range(3):
            if tab1[i][j]==0:
                tab1[i][j]=1
                if victoire_test(1):
                    tab1[i][j]=0
                    return (i,j)
                tab1[i][j]=0
    return None

def coup_aleatoire():
    cases = [(i,j) for i in range(3) for j in range(3) if tab1[i][j]==0]
    return random.choice(cases) if cases else None

def ordinateur():
    global tour
    coup = coup_gagnant()
    if coup is None:
        coup = coup_blocage()
    if coup is None:
        coup = coup_aleatoire()
    if coup:
        i,j = coup
        tab1[i][j]=2
        # Dessiner X
        if i == 0 and j == 0:
            cnv.create_line(90,90,210,210,fill="red")
            cnv.create_line(210,90,90,210,fill="red")
        elif i == 0 and j == 1:
            cnv.create_line(90,240,210,360,fill="red")
            cnv.create_line(210,240,90,360,fill="red")
        elif i == 0 and j == 2:
            cnv.create_line(90,390,210,510,fill="red")
            cnv.create_line(210,390,90,510,fill="red")
        elif i == 1 and j == 0:
            cnv.create_line(240,90,360,210,fill="red")
            cnv.create_line(360,90,240,210,fill="red")
        elif i == 1 and j == 1:
            cnv.create_line(240,240,360,360,fill="red")
            cnv.create_line(360,240,240,360,fill="red")
        elif i == 1 and j == 2:
            cnv.create_line(240,390,360,510,fill="red")
            cnv.create_line(360,390,240,510,fill="red")
        elif i == 2 and j == 0:
            cnv.create_line(390,90,510,210,fill="red")
            cnv.create_line(510,90,390,210,fill="red")
        elif i == 2 and j == 1:
            cnv.create_line(390,240,510,360,fill="red")
            cnv.create_line(510,240,390,360,fill="red")
        elif i == 2 and j == 2:
            cnv.create_line(390,390,510,510,fill="red")
            cnv.create_line(510,390,390,510,fill="red")
        tour = 1
        verifVictoire(tab1,2)

def clic(event) :
    global tour
    x,y = event.x , event.y
    if tour != 1:
        return

    if 75 < x < 225 :
        if 75 < y < 225 and tab1[0][0] == 0 :
            tab1[0][0] = 1
            cnv.create_oval(90,90,210,210,outline="blue")
        elif 225 < y < 375 and tab1[0][1] == 0 :
            tab1[0][1] = 1
            cnv.create_oval(90,240,210,360,outline="blue")
        elif 375< y < 525 and tab1[0][2] == 0 :
            tab1[0][2] = 1
            cnv.create_oval(90,390,210,510,outline="blue")
    elif 225 < x < 375 :
        if 75 < y < 225 and tab1[1][0] == 0:
            tab1[1][0] = 1
            cnv.create_oval(240,90,360,210,outline="blue")
        elif 225 < y < 375 and tab1[1][1] == 0 :
            tab1[1][1] = 1
            cnv.create_oval(240,240,360,360,outline="blue")
        elif 375< y < 525 and tab1[1][2] == 0 :
            tab1[1][2] = 1
            cnv.create_oval(240,390,360,510,outline="blue")
    elif 375 < x < 525 :
        if 75 < y < 225 and tab1[2][0] == 0 :
            tab1[2][0] = 1
            cnv.create_oval(390,90,510,210,outline="blue")
        elif 225 < y < 375 and tab1[2][1] == 0 :
            tab1[2][1] = 1
            cnv.create_oval(390,240,510,360,outline="blue")
        elif 375< y < 525 and tab1[2][2] == 0 :
            tab1[2][2] = 1
            cnv.create_oval(390,390,510,510,outline="blue")

    verifVictoire(tab1,1)
    if tour == 1:
        tour = 2
        fenetre.after(300, ordinateur)

cnv.bind("<Button-1>",clic)
btn_quitter = Button(fenetre,text="Quitter",command=fenetre.destroy)
btn_quitter.pack(side=RIGHT)
btn_rejouer = Button(fenetre,text="Rejouer", command=vider)
btn_rejouer.pack(side=LEFT)

fenetre.mainloop()