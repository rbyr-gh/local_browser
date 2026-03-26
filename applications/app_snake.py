import customtkinter as ctk
import tkinter as tk
import random

def snake(parent):
    # --- Configuration ---
    TAILLE_CASE = 20
    LARGEUR = 30
    HAUTEUR = 30

    # État du jeu
    # On utilise un dictionnaire ou des variables nonlocal définies avant init_game
    game = {"snake_body": [], "direction": "Right", "pomme": (0,0), "jeu_en_cours": False, "after_id": None}

    # Frame principale
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    # Canvas
    cnv = tk.Canvas(frame, width=TAILLE_CASE*LARGEUR, height=TAILLE_CASE*HAUTEUR, bg="black", highlightthickness=0)
    cnv.pack(pady=20)

    # Bouton restart
    restart_btn = ctk.CTkButton(frame, text="Restart", command=lambda: init_game())

    def init_game():
        # Annuler l'ancien mouvement si on restart en plein milieu
        if game["after_id"]:
            frame.after_cancel(game["after_id"])
            
        game["snake_body"] = [(15,15), (14,15), (13,15)]
        game["direction"] = "Right"
        game["pomme"] = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
        game["jeu_en_cours"] = True
        
        restart_btn.pack_forget()
        draw()
        move()

    def draw():
        cnv.delete("all")
        # Pomme
        px, py = game["pomme"]
        cnv.create_rectangle(px*TAILLE_CASE, py*TAILLE_CASE, 
                             px*TAILLE_CASE+TAILLE_CASE, py*TAILLE_CASE+TAILLE_CASE, fill="red")
        # Serpent
        for x, y in game["snake_body"]:
            cnv.create_rectangle(x*TAILLE_CASE, y*TAILLE_CASE, 
                                 x*TAILLE_CASE+TAILLE_CASE, y*TAILLE_CASE+TAILLE_CASE, fill="green")

    def move():
        if not game["jeu_en_cours"]:
            return

        x, y = game["snake_body"][0]

        if game["direction"] == "Up": y -= 1
        elif game["direction"] == "Down": y += 1
        elif game["direction"] == "Left": x -= 1
        elif game["direction"] == "Right": x += 1

        # Collisions
        if x<0 or x>=LARGEUR or y<0 or y>=HAUTEUR or (x,y) in game["snake_body"]:
            game["jeu_en_cours"] = False
            cnv.create_text(LARGEUR*TAILLE_CASE//2, HAUTEUR*TAILLE_CASE//2, 
                            text="GAME OVER", fill="white", font=("Arial", 30))
            restart_btn.pack(pady=10)
            return

        game["snake_body"].insert(0, (x,y))

        if (x,y) == game["pomme"]:
            while True:
                game["pomme"] = (random.randint(0,LARGEUR-1), random.randint(0,HAUTEUR-1))
                if game["pomme"] not in game["snake_body"]: break
        else:
            game["snake_body"].pop()

        draw()
        game["after_id"] = frame.after(100, move)

    def touches_possibles(event):
        # Empêcher le demi-tour direct
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if event.keysym in opposites:
            if event.keysym != opposites.get(game["direction"]):
                game["direction"] = event.keysym

    # --- Gestion des événements et nettoyage ---
    root = parent.winfo_toplevel()
    root.bind("<Key>", touches_possibles)

    def on_destroy(event):
        # On vérifie que c'est bien le frame principal qui est détruit
        if event.widget == frame:
            if game["after_id"]:
                frame.after_cancel(game["after_id"])
            root.unbind("<Key>")

    frame.bind("<Destroy>", on_destroy)
    
    # Lancement initial
    init_game()