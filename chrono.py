from customtkinter import *
from PIL import Image, ImageTk
import time

def chronometre():
    #fenetre
    fenetre = CTk()
    fenetre.title("Chrono")
    fenetre.geometry("300x300")


    menu = CTkFrame(fenetre)
    menu.place(x=0, y=0, relwidth=1, relheight=1)

    # Background
    image = Image.open("imagechrono.png")
    photo = ImageTk.PhotoImage(image)
    background_label = CTkLabel(menu, image=photo, text="")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Boutons menu
    def afficher_chrono():
        menu.place_forget()
        chrono.place(x=0, y=0, relwidth=1, relheight=1)

    def afficher_jeu():
        menu.place_forget()
        jeu10.place(x=0, y=0, relwidth=1, relheight=1)


    b1 = CTkButton(menu, text="Chronometre", fg_color='grey', text_color='white',
                width=225, height=50, command=afficher_chrono)
    b3 = CTkButton (menu, text="Jeu 10 secondes", fg_color='grey', text_color='white',
                width=225, height=50, command = afficher_jeu)

    b1.place(x=565, y=200)
    b3.place(x=565, y=300)


    chrono = CTkFrame(fenetre)

    label_chrono = CTkLabel(chrono, text="0.000 s", font=(None, 30))
    label_chrono.pack()

    # Variables du chrono
    en_cours = False
    temps = 0  
    debut = 0

    def update():
        nonlocal en_cours, temps
        if en_cours:
            t = (time.time() - debut) + temps
            label_chrono.configure(text=f"{t:.3f} s")
            fenetre.after(10, update)

    def start():
        nonlocal en_cours, debut
        if not en_cours:
            debut = time.time()
            en_cours = True
            update()

    def stop():
        nonlocal en_cours, temps
        if en_cours:
            temps += time.time() - debut
        en_cours = False

    def reset():
        nonlocal temps, debut, en_cours
        en_cours = False
        temps_ecoule = 0
        debut = 0
        temps = 0
        label_chrono.configure(text="0.000 s", font=(None, 30))

    def retour_menu():
        chrono.place_forget()
        menu.place(x=0, y=0, relwidth=1, relheight=1)

    # Boutons chrono
    CTkButton(chrono, text="Start", command=start).pack(pady = 10)
    CTkButton(chrono, text="Stop", command=stop).pack(pady = 10)
    CTkButton(chrono, text="Reset", command=reset).pack(pady = 10)
    CTkButton(chrono, text="Retour", command=retour_menu).pack(pady = 10)




    jeu10 = CTkFrame(fenetre)

    # Instructions du jeu
    label_jeu = CTkLabel(jeu10, text="Appuie sur Start et essaie de t'arreter à 10 secondes", font=(None, 30))
    label_jeu.pack(pady=10)

    # Variables du jeu
    en_cours_jeu = False
    temps_jeu = 0  
    debut_jeu = 0

    def update_jeu():
        nonlocal en_cours_jeu, temps_jeu
        if en_cours_jeu:
            t = (time.time() - debut_jeu) + temps_jeu
            label_jeu.configure(text=f"{t:.3f} s")
            fenetre.after(10, update_jeu)

    def start_jeu():
        nonlocal en_cours_jeu, debut_jeu
        if not en_cours_jeu:
            debut_jeu = time.time()
            en_cours_jeu = True
            update_jeu()

    def stop_jeu():
        nonlocal en_cours_jeu, temps_jeu
        if en_cours_jeu:
            temps_jeu += time.time() - debut_jeu
        en_cours_jeu = False
        ecart = abs(10 - temps_jeu)
        score = 10 - ecart*10
        if score < 0 :
            score = 0
        label_jeu.configure(text=f"Votre score est de {score: .2f}/10")

    def reset_jeu():
        nonlocal temps_jeu, debut_jeu, en_cours_jeu
        en_cours_jeu = False
        temps_ecoule = 0
        debut_jeu = 0
        temps_jeu = 0
        label_jeu.configure(text="0.000 s", font=(None, 30))

    def retour_menu_jeu():
        jeu10.place_forget()
        menu.place(x=0, y=0, relwidth=1, relheight=1)


    # Boutons jeu
    CTkButton(jeu10, text="Start", command=start_jeu).pack(pady=10)
    CTkButton(jeu10, text="Stop", command=stop_jeu).pack(pady=10)
    CTkButton(jeu10, text="Reset", command=reset_jeu).pack(pady=10)
    CTkButton(jeu10, text="Retour", command=retour_menu_jeu).pack(pady=10)



    b3.configure(command=lambda: [menu.place_forget(), jeu10.place(x=0, y=0, relwidth=1, relheight=1)])


    fenetre.mainloop()
        
chronometre()