from tkinter import *
import random

def snake():

    fenetre = Tk()
    fenetre.title("Snake")

    TAILLE_CASE = 20
    LARGEUR = 25
    HAUTEUR = 25

    cnv = Canvas(fenetre, width=TAILLE_CASE*LARGEUR,
                 height=TAILLE_CASE*HAUTEUR, bg="black")
    cnv.pack()

    restart_btn = Button(fenetre, text="Restart", font=("Arial",14), command=lambda: restart())

    def init_game():
        nonlocal snake_body, direction, pomme, jeu_en_cours

        snake_body = [(15,15), (14,15), (13,15)]
        direction = "Right"
        pomme = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
        jeu_en_cours = True

        restart_btn.pack_forget()

        draw()
        move()

    def draw():
        cnv.delete("all")

        for x,y in snake_body:
            cnv.create_rectangle(
                x*TAILLE_CASE, y*TAILLE_CASE,
                x*TAILLE_CASE+TAILLE_CASE, y*TAILLE_CASE+TAILLE_CASE,
                fill="green"
            )

        x,y = pomme
        cnv.create_rectangle(
            x*TAILLE_CASE, y*TAILLE_CASE,
            x*TAILLE_CASE+TAILLE_CASE, y*TAILLE_CASE+TAILLE_CASE,
            fill="red"
        )

    def move():
        nonlocal snake_body, pomme, jeu_en_cours

        if not jeu_en_cours:
            return

        x,y = snake_body[0]

        if direction == "Up":
            y -= 1
        elif direction == "Down":
            y += 1
        elif direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1

        if x<0 or x>=LARGEUR or y<0 or y>=HAUTEUR or (x,y) in snake_body:
            jeu_en_cours = False
            cnv.create_text(
                LARGEUR*TAILLE_CASE//2,
                HAUTEUR*TAILLE_CASE//2,
                text="GAME OVER",
                fill="white",
                font=("Arial",30)
            )
            restart_btn.pack(pady=10)
            return

        snake_body = [(x,y)] + snake_body

        if (x,y) == pomme:
            while True:
                pomme = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
                if pomme not in snake_body:
                    break
        else:
            snake_body.pop()

        draw()
        fenetre.after(100, move)

    def key(event):
        nonlocal direction

        if event.keysym in ["Up","Down","Left","Right"]:
            if (direction=="Up" and event.keysym!="Down") or \
               (direction=="Down" and event.keysym!="Up") or \
               (direction=="Left" and event.keysym!="Right") or \
               (direction=="Right" and event.keysym!="Left"):
                direction = event.keysym

    def restart():
        init_game()

    fenetre.bind("<Key>", key)

    snake_body = []
    direction = "Right"
    pomme = (0,0)
    jeu_en_cours = True

    init_game()

    fenetre.mainloop()