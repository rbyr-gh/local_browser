from tkinter import *
import random

fenetre = Tk()
fenetre.title("Snake Tkinter")
fenetre.geometry("600x600")

TAILLE_CASE = 20
LARGEUR = 25
HAUTEUR = 25

snake = [(15,15), (14,15), (13,15)]  
direction = "Right"
pomme = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
jeu_en_cours = True

cnv = Canvas(fenetre, width=TAILLE_CASE*LARGEUR, height=TAILLE_CASE*HAUTEUR, bg="black")
cnv.pack()

def draw():
    cnv.delete("all")
    # serpent
    for x,y in snake:
        cnv.create_rectangle(x*TAILLE_CASE, y*TAILLE_CASE,
                             x*TAILLE_CASE+TAILLE_CASE, y*TAILLE_CASE+TAILLE_CASE,
                             fill="green")
    # pomme
    x,y = pomme
    cnv.create_rectangle(x*TAILLE_CASE, y*TAILLE_CASE,
                         x*TAILLE_CASE+TAILLE_CASE, y*TAILLE_CASE+TAILLE_CASE,
                         fill="red")


def move():
    global snake, pomme, jeu_en_cours
    if not jeu_en_cours:
        return

    x,y = snake[0]

    if direction == "Up":
        y -= 1
    elif direction == "Down":
        y += 1
    elif direction == "Left":
        x -= 1
    elif direction == "Right":
        x += 1

    if x<0 or x>=LARGEUR or y<0 or y>=HAUTEUR or (x,y) in snake:
        jeu_en_cours = False
        cnv.create_text(LARGEUR*TAILLE_CASE//2, HAUTEUR*TAILLE_CASE//2,
                        text="GAME OVER", fill="white", font=("Arial",30))
        return

    snake = [(x,y)] + snake

    if (x,y) == pomme:
        while True:
            pomme = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
            if pomme not in snake:
                break
    else:
        snake.pop()

    draw()
    fenetre.after(100, move)  # vitesse du snake (100ms)

# ---------------- Gestion des touches ----------------
def key(event):
    global direction
    if event.keysym in ["Up","Down","Left","Right"]:
        # empêcher de faire demi-tour
        if (direction=="Up" and event.keysym!="Down") or \
           (direction=="Down" and event.keysym!="Up") or \
           (direction=="Left" and event.keysym!="Right") or \
           (direction=="Right" and event.keysym!="Left"):
            direction = event.keysym

fenetre.bind("<Key>", key)

# ---------------- Démarrage ----------------
draw()
move()
fenetre.mainloop()