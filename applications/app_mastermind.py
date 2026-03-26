import customtkinter as ctk
import random

# =============================
# 🔹 CONFIG COULEURS / CONSTANTES
# =============================
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10

black = "gray90"
white = "gray15"

couleur_Fond = (black,"grey15")
couleur_Bouton = ("DarkOrange1","DarkOrange3")
couleur_Surbrillance = ("grey74","grey43")


# =============================
# 🔹 FRAME MASTERMIND
# =============================
class frame_Mastermind(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=couleur_Fond)

        # Variables du jeu
        self.secret_code = []
        self.current_guess = []
        self.attempts = 0
        self.game_over = False

        # Création des widgets
        self.create_widgets()
        self.new_game()


    # =============================
    # 🔹 WIDGETS
    # =============================
    def create_widgets(self):
        # Titre
        self.title_label = ctk.CTkLabel(
            self, text="MASTERMIND", font=("Arial",24,"bold"), text_color="white"
        )
        self.title_label.pack(pady=10)

        # Historique
        self.history_frame = ctk.CTkScrollableFrame(self, width=400, height=250, fg_color=couleur_Fond)
        self.history_frame.pack(pady=5, padx=10)

        # Proposition actuelle
        self.current_frame = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.current_frame.pack(pady=5)

        ctk.CTkLabel(
            self.current_frame, text="Votre proposition:", font=("Arial",12), text_color="white"
        ).pack(pady=3)

        self.guess_display = ctk.CTkFrame(self.current_frame, fg_color=couleur_Fond)
        self.guess_display.pack(pady=3)

        self.guess_circles = []
        for i in range(CODE_LENGTH):
            circle = ctk.CTkButton(
                self.guess_display, text="", width=40, height=40,
                corner_radius=20, fg_color="gray30", hover=False
            )
            circle.pack(side="left", padx=3)
            self.guess_circles.append(circle)

        # Palette de couleurs
        self.palette_frame = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.palette_frame.pack(pady=5)

        ctk.CTkLabel(
            self.palette_frame, text="Choisissez les couleurs:", font=("Arial",10), text_color="white"
        ).pack(pady=2)

        self.color_buttons_frame = ctk.CTkFrame(self.palette_frame, fg_color=couleur_Fond)
        self.color_buttons_frame.pack(pady=2)

        for color in COLORS:
            btn = ctk.CTkButton(
                self.color_buttons_frame, text="", width=30, height=30,
                corner_radius=15, fg_color=color, hover_color=self.lighten_color(color),
                command=lambda c=color: self.add_color(c)
            )
            btn.pack(side="left", padx=2)

        # Boutons actions
        self.action_frame = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.action_frame.pack(pady=5)

        self.clear_btn = ctk.CTkButton(
            self.action_frame, text="Effacer", width=80, command=self.clear_guess,
            fg_color=couleur_Bouton, hover_color=couleur_Surbrillance
        )
        self.clear_btn.pack(side="left", padx=3)

        self.submit_btn = ctk.CTkButton(
            self.action_frame, text="Valider", width=80, command=self.submit_guess,
            fg_color="green", hover_color="darkgreen"
        )
        self.submit_btn.pack(side="left", padx=3)

        self.new_game_btn = ctk.CTkButton(
            self.action_frame, text="Nouvelle partie", width=110, command=self.new_game,
            fg_color=couleur_Bouton, hover_color=couleur_Surbrillance
        )
        self.new_game_btn.pack(side="left", padx=3)

        # Statut
        self.status_label = ctk.CTkLabel(
            self, text="", font=("Arial",12,"bold"), text_color="white"
        )
        self.status_label.pack(pady=5)

        # Légende
        self.legend_frame = ctk.CTkFrame(self, fg_color=couleur_Fond)
        self.legend_frame.pack(pady=2)

        ctk.CTkLabel(self.legend_frame, text="🔴 = bonne couleur, bonne place", 
                     font=("Arial",9), text_color="white").pack(side="left", padx=5)
        ctk.CTkLabel(self.legend_frame, text="⚪ = bonne couleur, mauvaise place",
                     font=("Arial",9), text_color="white").pack(side="left", padx=5)


    # =============================
    # 🔹 UTILS
    # =============================
    def lighten_color(self, color):
        lighter = {
            "red": "#ff6666", "blue": "#6666ff", "green": "#66ff66",
            "yellow": "#ffff66", "orange": "#ffcc66", "purple": "#cc66ff"
        }
        return lighter.get(color, color)


    # =============================
    # 🔹 NOUVELLE PARTIE
    # =============================
    def new_game(self):
        self.secret_code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
        self.current_guess = []
        self.attempts = 0
        self.game_over = False

        # Reset historique
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        self.update_guess_display()
        self.status_label.configure(text=f"Tentatives restantes: {MAX_ATTEMPTS}")
        self.submit_btn.configure(state="normal")


    # =============================
    # 🔹 AJOUT COULEUR
    # =============================
    def add_color(self, color):
        if len(self.current_guess) < CODE_LENGTH and not self.game_over:
            self.current_guess.append(color)
            self.update_guess_display()

    def clear_guess(self):
        self.current_guess = []
        self.update_guess_display()

    def update_guess_display(self):
        for i, circle in enumerate(self.guess_circles):
            if i < len(self.current_guess):
                circle.configure(fg_color=self.current_guess[i])
            else:
                circle.configure(fg_color="gray30")


    # =============================
    # 🔹 VALIDATION
    # =============================
    def check_guess(self, guess):
        correct_position = 0
        correct_color = 0
        secret_copy = self.secret_code.copy()
        guess_copy = guess.copy()

        for i in range(CODE_LENGTH):
            if guess[i] == self.secret_code[i]:
                correct_position += 1
                secret_copy[i] = None
                guess_copy[i] = None

        for i in range(CODE_LENGTH):
            if guess_copy[i] is not None and guess_copy[i] in secret_copy:
                correct_color += 1
                secret_copy[secret_copy.index(guess_copy[i])] = None

        return correct_position, correct_color

    def submit_guess(self):
        if len(self.current_guess) != CODE_LENGTH or self.game_over:
            return

        self.attempts += 1
        correct_pos, correct_color = self.check_guess(self.current_guess)
        self.add_to_history(self.current_guess.copy(), correct_pos, correct_color)

        if correct_pos == CODE_LENGTH:
            self.game_over = True
            self.status_label.configure(
                text=f"🎉 Gagné en {self.attempts} tentative(s) !",
                text_color="green"
            )
            self.submit_btn.configure(state="disabled")
        elif self.attempts >= MAX_ATTEMPTS:
            self.game_over = True
            code_str = " ".join([c[0].upper() for c in self.secret_code])
            self.status_label.configure(
                text=f"😢 Perdu ! Code: {code_str}",
                text_color="red"
            )
            self.submit_btn.configure(state="disabled")
            self.reveal_code()
        else:
            self.status_label.configure(
                text=f"Tentatives restantes: {MAX_ATTEMPTS - self.attempts}",
                text_color="white"
            )

        self.current_guess = []
        self.update_guess_display()


    # =============================
    # 🔹 HISTORIQUE / INDICES
    # =============================
    def add_to_history(self, guess, correct_pos, correct_color):
        row = ctk.CTkFrame(self.history_frame, fg_color=couleur_Fond)
        row.pack(pady=2, fill="x")

        ctk.CTkLabel(row, text=f"{self.attempts}.", width=25, text_color="white").pack(side="left", padx=3)

        for color in guess:
            circle = ctk.CTkButton(
                row, text="", width=25, height=25, corner_radius=12,
                fg_color=color, hover=False
            )
            circle.pack(side="left", padx=2)

        result_frame = ctk.CTkFrame(row, fg_color=couleur_Fond)
        result_frame.pack(side="left", padx=10)
        hints = "🔴" * correct_pos + "⚪" * correct_color
        ctk.CTkLabel(result_frame, text=hints if hints else "—", font=("Arial",10), text_color="white").pack()


    # =============================
    # 🔹 REVELER LE CODE
    # =============================
    def reveal_code(self):
        reveal_frame = ctk.CTkFrame(self.history_frame, fg_color=couleur_Fond)
        reveal_frame.pack(pady=5)
        ctk.CTkLabel(reveal_frame, text="Code secret:", font=("Arial",11,"bold"), text_color="white").pack(side="left", padx=3)
        for color in self.secret_code:
            circle = ctk.CTkButton(reveal_frame, text="", width=25, height=25, corner_radius=12,
                                   fg_color=color, hover=False)
            circle.pack(side="left", padx=2)