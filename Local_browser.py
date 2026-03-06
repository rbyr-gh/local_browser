import customtkinter as ctk

# Configuration globale
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("ESEOFOX")
        self.geometry("900x600")
        
        # Configuration de la grille (2 colonnes : Menu + Contenu)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- 1. CRÉATION DU MENU LATÉRAL (Gauche) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1) # Espace flexible en bas

        # Titre du menu
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ESEOFOX", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Boutons du menu
            # Boutons d'accueil
        self.btn_home = ctk.CTkButton(self.sidebar_frame, text="Accueil", command=self.show_home)
        self.btn_home.grid(row=1, column=0, padx=20, pady=10)
            # Boutons des paramètres
        self.btn_settings = ctk.CTkButton(self.sidebar_frame, text="Paramètres", command=self.show_settings)
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)
            # Boutons des aides
        self.btn_help = ctk.CTkButton(self.sidebar_frame, text="Aide", command=self.show_help)
        self.btn_help.grid(row=3, column=0, padx=20, pady=10)

        # Interrupteur de thème (dans le menu)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Mode :", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        
        self.switch_theme = ctk.CTkSwitch(self.sidebar_frame, text="Dark/Light", command=self.switch_theme_event)
        self.switch_theme.grid(row=5, column=0, padx=20, pady=10)

        # --- 2. ZONE DE CONTENU (Droite) ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Label de bienvenue (contenu par défaut)
        self.welcome_label = ctk.CTkLabel(self.content_frame, text="Bienvenue sur l'Accueil", 
                                          font=ctk.CTkFont(size=24))
        self.welcome_label.pack(pady=50)

    # --- Fonctions de gestion du thème ---
    def switch_theme_event(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    # --- Fonctions de navigation (Simulation) ---
    def show_home(self):
        self.welcome_label.configure(text="Bienvenue sur l'Accueil")
        # Ici, vous pourriez effacer le frame et ajouter d'autres widgets

    def show_settings(self):
        self.welcome_label.configure(text="Page des Paramètres")

    def show_help(self):
        self.welcome_label.configure(text="Page d'Aide")

if __name__ == "__main__":
    app = App()
    app.mainloop()