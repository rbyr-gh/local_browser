import customtkinter as ctk
import time

black = "gray90"
white = "gray15"

couleur_Fond = (black,"grey15")
couleur_Bouton = ("DarkOrange1","DarkOrange3")
couleur_Surbrillance = ("grey74","grey43")
couleur_Texte = (white,black)


class frame_Chrono(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.en_cours = False
        self.temps = 0
        self.debut = 0

        self.en_cours_jeu = False
        self.temps_jeu = 0
        self.debut_jeu = 0

        self.menu = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.menu.pack(fill="both", expand=True)

        self.btn_chrono = ctk.CTkButton(
            self.menu, text="Chronomètre",
            command=self.afficher_chrono,
            fg_color=couleur_Bouton,
            hover_color=couleur_Surbrillance,
            text_color=couleur_Texte
        )
        self.btn_chrono.pack(pady=40)

        self.btn_jeu = ctk.CTkButton(
            self.menu, text="Jeu 10 secondes",
            command=self.afficher_jeu,
            fg_color=couleur_Bouton,
            hover_color=couleur_Surbrillance,
            text_color=couleur_Texte
        )
        self.btn_jeu.pack(pady=20)

        self.chrono = ctk.CTkFrame(self, fg_color=couleur_Fond)

        self.label_chrono = ctk.CTkLabel(
            self.chrono, text="0.000 s",
            font=("Arial", 40, "bold"),
            text_color=couleur_Texte
        )
        self.label_chrono.pack(pady=40)

        ctk.CTkButton(self.chrono, text="Start", command=self.start).pack(pady=10)
        ctk.CTkButton(self.chrono, text="Stop", command=self.stop).pack(pady=10)
        ctk.CTkButton(self.chrono, text="Reset", command=self.reset).pack(pady=10)
        ctk.CTkButton(self.chrono, text="Retour", command=self.retour_menu).pack(pady=20)

        self.jeu10 = ctk.CTkFrame(self, fg_color=couleur_Fond)

        self.label_jeu = ctk.CTkLabel(
            self.jeu10,
            text="Appuie sur Start et arrête-toi à 10 secondes",
            font=("Arial", 25),
            text_color=couleur_Texte
        )
        self.label_jeu.pack(pady=30)

        ctk.CTkButton(self.jeu10, text="Start", command=self.start_jeu).pack(pady=10)
        ctk.CTkButton(self.jeu10, text="Stop", command=self.stop_jeu).pack(pady=10)
        ctk.CTkButton(self.jeu10, text="Reset", command=self.reset_jeu).pack(pady=10)
        ctk.CTkButton(self.jeu10, text="Retour", command=self.retour_menu_jeu).pack(pady=20)

    def afficher_chrono(self):
        self.menu.pack_forget()
        self.chrono.pack(fill="both", expand=True)

    def afficher_jeu(self):
        self.menu.pack_forget()
        self.jeu10.pack(fill="both", expand=True)

    def retour_menu(self):
        self.chrono.pack_forget()
        self.menu.pack(fill="both", expand=True)

    def retour_menu_jeu(self):
        self.jeu10.pack_forget()
        self.menu.pack(fill="both", expand=True)

    def update(self):
        if self.en_cours:
            t = (time.time() - self.debut) + self.temps
            self.label_chrono.configure(text=f"{t:.3f} s")
            self.after(10, self.update)

    def start(self):
        if not self.en_cours:
            self.debut = time.time()
            self.en_cours = True
            self.update()

    def stop(self):
        if self.en_cours:
            self.temps += time.time() - self.debut
        self.en_cours = False

    def reset(self):
        self.en_cours = False
        self.temps = 0
        self.debut = 0
        self.label_chrono.configure(text="0.000 s")

    def update_jeu(self):
        if self.en_cours_jeu:
            t = (time.time() - self.debut_jeu) + self.temps_jeu
            self.label_jeu.configure(text=f"{t:.3f} s")
            self.after(10, self.update_jeu)

    def start_jeu(self):
        if not self.en_cours_jeu:
            self.debut_jeu = time.time()
            self.en_cours_jeu = True
            self.update_jeu()

    def stop_jeu(self):
        if self.en_cours_jeu:
            self.temps_jeu += time.time() - self.debut_jeu
        self.en_cours_jeu = False

        ecart = abs(10 - self.temps_jeu)
        score = max(0, 10 - ecart * 10)

        self.label_jeu.configure(text=f"Score : {score:.2f} / 10")

    def reset_jeu(self):
        self.en_cours_jeu = False
        self.temps_jeu = 0
        self.debut_jeu = 0
        self.label_jeu.configure(text="0.000 s")