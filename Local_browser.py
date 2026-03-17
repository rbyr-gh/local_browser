import customtkinter as ctk
from PIL import Image
from App_features.snake import snake

# Initialisation des constantes
color_background_light = "#eeeeee"
color_background_dark = "#242429"
# Configuration globale
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Paramètre de l'application
        self.title("ESEOFOX") 
        self.attributes('-fullscreen', True)
        
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Frame de la sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1) 

        # Titre du menu
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ESEOFOX", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(100, 10))

        # Boutons du menu
            # Bouton d'accueil
        self.btn_home = ctk.CTkButton(self.sidebar_frame, text="Accueil", command=self.show_home)
        self.btn_home.grid(row=1, column=0, padx=20, pady=10)
            # Bouton des paramètres
        self.btn_settings = ctk.CTkButton(self.sidebar_frame, text="Paramètres", command=self.show_settings)
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)
            # Bouton des aides
        self.btn_help = ctk.CTkButton(self.sidebar_frame, text="Aide", command=self.show_help)
        self.btn_help.grid(row=3, column=0, padx=20, pady=10)
            # Bouton pour quitter la page
        self.btn_quit = ctk.CTkButton(self.sidebar_frame, text="Quitter la page", command = self.quit)
        self.btn_quit.grid(row=7, column=0, padx=20, pady=(0,50), sticky='s')

        # Interrupteur de thème (dans le menu)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Mode :", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        
        self.switch_theme = ctk.CTkSwitch(self.sidebar_frame, text="Dark/Light", command=self.switch_theme_event)
        self.switch_theme.grid(row=5, column=0, padx=20, pady=10)

        # FRAME ACCUEIL
        self.content_frame_accueil = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame_accueil.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content_frame_accueil.grid_rowconfigure(3, weight=1) 
        self.content_frame_accueil.grid_columnconfigure(2, weight=1) 

        # Label de bienvenue
        self.welcome_label = ctk.CTkLabel(self.content_frame_accueil, text="Bienvenue sur l'Accueil", font=ctk.CTkFont(size=24))
        self.welcome_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Label d'applications 
        self.app_label = ctk.CTkLabel(self.content_frame_accueil,text="Applications : ",font=ctk.CTkFont(size=16))
        self.app_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Logo App
        chronoImage = ctk.CTkImage(light_image=Image.open("Image_app\Chrono_lightmode.png"), dark_image=Image.open("Image_app/Chrono_darkmode.png"), size=(150, 150))
        button_chronoImage = ctk.CTkButton(self.content_frame_accueil, image=chronoImage, text="", fg_color= "transparent", command=lambda: self.launch_app("chrono"))
        button_chronoImage.grid(row=2, column=0, padx=100, pady=10, sticky="w")

        snakeImage = ctk.CTkImage(light_image=Image.open("Image_app/Snake.png"), size=(150, 150))
        button_snakeImage = ctk.CTkButton(self.content_frame_accueil, image=snakeImage, text="", fg_color= "transparent", command=lambda: self.launch_app("snake"))
        button_snakeImage.grid(row=2, column=1, padx=100, pady=10, sticky="nsew")

        notesImage = ctk.CTkImage(light_image=Image.open("Image_app/Notes.png"), size=(150, 150))
        button_notesImage = ctk.CTkButton(self.content_frame_accueil, image=notesImage, text="", fg_color= "transparent", command=lambda: self.launch_app("notes"))
        button_notesImage.grid(row=2, column=2, padx=100, pady=10, sticky="e")

        morpionImage = ctk.CTkImage(light_image=Image.open("Image_app/Morpion.png"), size=(150, 150))
        button_morpionImage = ctk.CTkButton(self.content_frame_accueil, image=morpionImage, text="", fg_color= "transparent", command=lambda: self.launch_app("notes"))
        button_morpionImage.grid(row=3, column=0, padx=100, pady=10, sticky="w")

        contactsImage = ctk.CTkImage(light_image=Image.open("Image_app/Contacts.png"), size=(150, 150))
        button_contactsImage = ctk.CTkButton(self.content_frame_accueil, image=contactsImage, text="", fg_color= "transparent", command=lambda: self.launch_app("contacts"))
        button_contactsImage.grid(row=3, column=1, padx=100, pady=0, sticky="we")

        messagesImage = ctk.CTkImage(light_image=Image.open("Image_app/Messages.png"), size=(150, 150))
        button_messagesImage = ctk.CTkButton(self.content_frame_accueil, image=messagesImage, text="", fg_color= "transparent", command=lambda: self.launch_app("messages"))
        button_messagesImage.grid(row=3, column=2, padx=100, pady=0, sticky="e")

        wikiImage = ctk.CTkImage(light_image=Image.open("Image_app/Wiki.png"), size=(150, 150))
        button_wikiImage = ctk.CTkButton(self.content_frame_accueil, image=wikiImage, text="", fg_color= "transparent", command=lambda: self.launch_app("wiki"))
        button_wikiImage.grid(row=4, column=0, padx=100, pady=0, sticky="w")

        calculatriceImage = ctk.CTkImage(light_image=Image.open("Image_app/Calculatrice.png"), size=(150, 150))
        button_calculatriceImage = ctk.CTkButton(self.content_frame_accueil, image=calculatriceImage, text="", fg_color= "transparent", command=lambda: self.launch_app("calculatrice"))
        button_calculatriceImage.grid(row=4, column=1, padx=100, pady=10, sticky="nsew")

        # FRAME PARAMETRE
        self.content_frame_settings = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Label Paramètre
        self.settings_label = ctk.CTkLabel(self.content_frame_settings, text = "Paramètres", font=ctk.CTkFont(size=24))
        self.settings_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # FRAME AIDE
        self.content_frame_help = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Label Paramètre
        self.help_label = ctk.CTkLabel(self.content_frame_help, text = "Aides", font=ctk.CTkFont(size=24))
        self.help_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # --- Fonctions de gestion du thème ---

    def switch_theme_event(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
            

    # --- Fonctions de navigation (Simulation) ---
    def show_home(self):
        if hasattr(self, 'current_app_frame'):
            self.current_app_frame.destroy() 
        
            del self.current_app_frame 

        self.content_frame_settings.grid_forget()
        self.content_frame_help.grid_forget()

        self.content_frame_accueil.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_settings(self):
        
        if hasattr(self, 'current_app_frame'):
            self.current_app_frame.destroy()
            del self.current_app_frame

        self.content_frame_accueil.grid_forget()
        self.content_frame_help.grid_forget()
        self.content_frame_settings.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_help(self):
        
        if hasattr(self, 'current_app_frame'):
            self.current_app_frame.destroy()
            del self.current_app_frame

        self.content_frame_accueil.grid_forget()
        self.content_frame_settings.grid_forget()
        self.content_frame_help.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def launch_app(self, app_name):

        self.content_frame_accueil.grid_forget()
        
        if hasattr(self, 'current_app_frame'):
            self.current_app_frame.destroy()
        
        self.current_app_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.current_app_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        
        if app_name == "snake":
            snake(self.current_app_frame)
        


if __name__ == "__main__":
    app = App()
    app.mainloop()


