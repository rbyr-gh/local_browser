import customtkinter as ctk
import tkinter
from CTkListbox import *
from os import *
from PIL import Image
import time
from math import ceil
from App_features.snake import snake
from App_features.calculatrice import calculatrice



# INITIALISATION DES CONSTANTES


color_background_light = "#eeeeee"
color_background_dark = "#242429"


# CONFIGURATION GLOBALE

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# DEFINITION DE LA CLASSE APP

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

# PARAMETRE DE L'APPLICATION 

        global ws
        global hs 
        self.title("ESEOFOX") 
        icon = tkinter.PhotoImage(file="Image_app\IconBitMap_ESEOFOX.png")
        self.iconphoto(True,icon)
        self.attributes("-alpha",1)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        self.geometry(f"{ws}x{hs}")
        self.minsize(int(ws/2),int(hs/2))
        self.maxsize(ws,hs)


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
# FRAMES

                # FRAME SIDEBAR
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1) 

                # FRAME ACCUEIL
        self.content_frame_accueil = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame_accueil.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content_frame_accueil.grid_rowconfigure(4, weight=1) 
        self.content_frame_accueil.grid_columnconfigure(2, weight=1) 

                # FRAME BARRE SUPERIEURE
        self.frameBarreSuperieur = ctk.CTkFrame(self.content_frame_accueil,width=ws,height=75,fg_color="gray21")
        self.frameBarreSuperieur.grid(row=0,column=0,sticky="nsew")
        self.frameBarreSuperieur.grid_propagate(False)
        self.frameBarreSuperieur.grid_columnconfigure(0,weight=1)
        self.frameBarreSuperieur.grid_columnconfigure(1,weight=1)
        self.frameBarreSuperieur.grid_columnconfigure(2,weight=1)
        self.frameBarreSuperieur.grid_rowconfigure(0,weight=1)
        self.frameBarreSuperieur.grid_rowconfigure(2,weight=1)

                # FRAME PARAMETRE
        self.content_frame_settings = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

                # FRAME AIDE
        self.content_frame_help = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

                # FRAME POUR LES APPLICATIONS
        self.apps_frame = ctk.CTkFrame(self.content_frame_accueil, fg_color="transparent")
        self.apps_frame.grid(row=3, column=0, columnspan=3, pady=20)

# LABEL
                # LABEL TITRE
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ESEOFOX", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(100, 10))

                # LABEL PARAMETRE
        self.help_label = ctk.CTkLabel(self.content_frame_help, text = "Aides", font=ctk.CTkFont(size=24))
        self.help_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

                # LABEL MODE - Interrupteur de thème (dans le menu)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Mode :", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))

                # LABEL DE BIENVENUE
        self.welcome_label = ctk.CTkLabel(self.content_frame_accueil, text="Bienvenue sur l'Accueil", font=ctk.CTkFont(size=24))
        self.welcome_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

                # LABEL D'APPLICATIONS
        self.app_label = ctk.CTkLabel(self.content_frame_accueil,text="Applications : ",font=ctk.CTkFont(size=16))
        self.app_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        
# BOUTONS

        # BOUTONS DU MENU
                # BOUTON D'ACCUEIL
        self.btn_home = ctk.CTkButton(self.sidebar_frame, text="Accueil", command=self.show_home)
        self.btn_home.grid(row=1, column=0, padx=20, pady=10)

                # BOUTON DES PARAMETRES
        self.btn_settings = ctk.CTkButton(self.sidebar_frame, text="Paramètres", command=self.show_settings)
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)
        
                # BOUTON DES AIDES
        self.btn_help = ctk.CTkButton(self.sidebar_frame, text="Aide", command=self.show_help)
        self.btn_help.grid(row=3, column=0, padx=20, pady=10)

                # BOUTON POUR QUITTER L'APPLICATION
        self.btn_quit = ctk.CTkButton(self.sidebar_frame, text="Quitter la page", command = self.quit)
        self.btn_quit.grid(row=7, column=0, padx=20, pady=(0,50), sticky='s')

                # CONFIGURATION DE LA GRILLE D'APPLICATION
        for i in range(3):
            self.apps_frame.grid_columnconfigure(i, weight=1)

                # IMAGES
        chronoImage = ctk.CTkImage(light_image=Image.open("Image_app/Chrono_lightmode.png"), dark_image=Image.open("Image_app/Chrono_darkmode.png"), size=(120, 120)     )
        snakeImage = ctk.CTkImage(light_image=Image.open("Image_app/Snake.png"), size=(120, 120))
        notesImage = ctk.CTkImage(light_image=Image.open("Image_app/Notes.png"), size=(120, 120))
        morpionImage = ctk.CTkImage(light_image=Image.open("Image_app/Morpion.png"), size=(120, 120))
        contactsImage = ctk.CTkImage(light_image=Image.open("Image_app/Contacts.png"), size=(120, 120))
        messagesImage = ctk.CTkImage(light_image=Image.open("Image_app/Messages.png"), size=(120, 120))
        wikiImage = ctk.CTkImage(light_image=Image.open("Image_app/Wiki.png"), size=(120, 120))
        calculatriceImage = ctk.CTkImage(light_image=Image.open("Image_app/Calculatrice.png"), size=(120, 120))

                # LISTES DES APPLICATIONS
        apps = [("chrono", chronoImage), ("snake", snakeImage), ("notes", notesImage), ("morpion", morpionImage), ("contacts", contactsImage), ("messages", messagesImage), ("wiki", wikiImage), ("calculatrice", calculatriceImage)]

                # CREATION DES BOUTONS
        for index, (name, img) in enumerate(apps):
            row = index // 3
            col = index % 3

            btn = ctk.CTkButton(self.apps_frame, image=img, text="", fg_color="transparent", hover_color="gray25", command=lambda n=name: self.launch_app(n))
            btn.grid(row=row, column=col, padx=40, pady=20)

        
# SWITCH               
        
        self.switch_theme = ctk.CTkSwitch(self.sidebar_frame, text="Dark/Light", command=self.switch_theme_event)
        self.switch_theme.grid(row=5, column=0, padx=20, pady=10)

# FONCTION
            #  FONCTION DE GESTION DU THEME

    def switch_theme_event(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")
            

            #  FONTION DE NAVIGATION
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
        elif app_name == "calculatrice":
            calculatrice(self.current_app_frame)

    def recherche(texte) :
        L_application = ["contacts","morpion","snake","notes","messages","wiki","chrono"]
        if texte == "" :
            lBox_Recherche.place_forget()
            lBox_Recherche.configure(height=0)
        else :
            lBox_Recherche.place(x=720,y=60)
            lBox_Recherche.lift()
            lBox_Recherche.delete(0, "END")
            listeElement = [item for item in L_application if texte.lower() in item]
            lBox_Recherche.configure(height=len(listeElement)*35 if listeElement else 0)
            if len(listeElement) == 0 :
                lBox_Recherche.place_forget() 
            for item in listeElement :
                lBox_Recherche.insert("END",item.capitalize())

    def ch_taille(self,ws,hs) :
        if self.winfo_height != ws :
            self.update_idletasks()
            scalingW = self.winfo_width()/ws
            scalingH = self.winfo_height()/hs
            self.frame_BarreRecherche.configure(height=int(hs/10*scalingH),width=int(ws*scalingW))
            self.frame_BarreRecherche.grid_propagate(False)
            self.frame_MenuLateral.configure(height=int((hs-hs/10-50)*scalingH),width=int((ws/9)*scalingW))
            self.frame_MenuLateral.grid_propagate(False)
            self.frame_MenuApplications.configure(height=int((hs-hs/10-50)*scalingH),width=int((ws-ws/9-40)*scalingW))
            self.rame_ScrollApp.configure(height=((hs-hs/10-100)*scalingH),width=int((ws-270)*scalingW))
            # test -> print(self.winfo_height())
            self.update_idletasks()

            column_app = int((frame_ScrollApp.winfo_width())/120)
            print(column_app)
            row_app = int(ceil(len(L)/column_app))
            c=0

            for i in range(row_app) :
                for j in range(column_app) :
                    if c < len(L) :
                        L[c].grid_configure(row=i,column=j,pady=10,padx=10)
                        c += 1
                    else :
                        pass
        

# Fonction de lancement de l'application 

if __name__ == "__main__":
    app = App()
    app.mainloop()


