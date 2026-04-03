from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage
import os
from PIL import Image
import json

black = "gray90"
white = "gray15"

couleur_Fond2 = ("grey95","grey23")
couleur_Fond = (black,"grey15")
couleur_Widget = ("grey74","grey43")
couleur_Bouton1 = (black,"grey3")
couleur_Bouton2 = ("DarkOrange1","DarkOrange3")
couleur_Surbrillance =("grey74","grey43")
couleur_Bord = (white,black)
couleur_Texte1 = (white,black)
couleur_Texte2 = ("grey26","grey80")
couleur_Texte3 = (black,white)

# FONCTION : Supprimer mise en forme, Position texte, Puce, Décalage texte, Bouton coller, Appliquer un style à un ligne,enregistrement rapide
#  ne pas ouvrir un nouveau fichier si non enregistrer

class frame_Notes(CTkFrame):
    def __init__(self, parent) :
        super().__init__(parent)
        
        self.tag = "black"
        self.font = "Arial+012+normal+roman+0+0"
        self.background = "white"
        
        self.c = 0
        self.enregistrer = 1
        self.fichier_ouvert = ""

        
        
        
        ## BARRE DU HAUT
        
        
        self.editeurParametres = CTkFrame(self)
        self.editeurParametres.grid(row=0,column=0,sticky="ew",ipady=5)
        self.editeurParametres.configure(fg_color=couleur_Fond2,corner_radius=0,border_width=2,border_color=couleur_Fond)
        
        self.frame_Couleur = CTkFrame(self,border_width=1,border_color=couleur_Texte1,corner_radius=0)
        self.frame_Couleur.rowconfigure(0,weight=0)
        self.frame_Couleur.rowconfigure(1,weight=0)
        self.frame_Couleur.rowconfigure(2,weight=0)
        self.frame_Couleur.rowconfigure(3,weight=0)
        self.frame_Couleur.rowconfigure(4,weight=0)
        self.frame_Couleur.rowconfigure(5,weight=0)
        self.frame_Couleur.rowconfigure(6,weight=0)
        self.frame_Couleur.columnconfigure(0,weight=0)
        self.frame_Couleur.columnconfigure(1,weight=0)
        self.frame_Couleur.columnconfigure(2,weight=0)
        self.frame_Couleur.columnconfigure(3,weight=0)
        self.frame_Couleur.columnconfigure(4,weight=0)
        self.frame_Couleur.columnconfigure(5,weight=0)
        self.frame_Couleur.columnconfigure(6,weight=0)
        self.frame_Couleur.place(x=5,y=30)
        
        self.frame_CouleurFond = CTkFrame(self,border_width=1,border_color=couleur_Texte1,corner_radius=0)
        self.frame_CouleurFond.rowconfigure(0,weight=0)
        self.frame_CouleurFond.rowconfigure(1,weight=0)
        self.frame_CouleurFond.columnconfigure(0,weight=0)
        self.frame_CouleurFond.columnconfigure(1,weight=0)
        self.frame_CouleurFond.columnconfigure(2,weight=0)
        self.frame_CouleurFond.columnconfigure(3,weight=0)
        self.frame_CouleurFond.columnconfigure(4,weight=0)
        self.frame_CouleurFond.columnconfigure(5,weight=0)
        self.frame_CouleurFond.columnconfigure(6,weight=0)
        self.frame_CouleurFond.place(x=5,y=88)
        
        ## TAG STYLE 
        
        self.liste_police = [ "Arial", "Times New Roman", "Courier New", "Calibri", "Georgia", "Impact", "Comic Sans MS", "Lucida Console","Brush Script MT","Papyrus","Rockwell","Segoe UI"]
        self.liste_taille = [6,8,10,11,12,14,15,16,18,20,22,24,28,32,40,48,54]
        self.liste_taille_str = ["6","8","10","11","12","14","15","16","18","20","22","24","28","32","40","48","54"]
        self.liste_epaisseur = ["normal","bold"]
        
        self.liste_background = ["white","red", "orange", "yellow", "green", "blue", "purple", "pink"]
        
        self.liste_slant = ["roman","italic"]
        
        self.liste_underline = [0,1]
        
        self.liste_overstrike = [0,1] 
        
        self.tableau_couleurs = [
            ["white", "black", "lightgray", "orangered", "skyblue", "limegreen", "violet"],
            ["ivory", "dimgray", "gainsboro", "tomato", "dodgerblue", "forestgreen", "plum"],
            ["alice blue", "gray", "silver", "coral", "cornflowerblue", "chartreuse", "orchid"],
            ["beige", "slategray", "whitesmoke", "salmon", "lightblue", "seagreen", "magenta"],
            ["antique white", "darkslategray", "lightgrey", "orange", "blue", "mediumseagreen", "fuchsia"],
            ["linen", "black", "darkgray", "darkorange", "mediumblue", "green", "hotpink"],
            ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        ]
            
        for i in range(len(self.tableau_couleurs)) :
            for j in range(len(self.tableau_couleurs[0])) :
                bouton = CTkButton(self.frame_Couleur,text="",bg_color=self.tableau_couleurs[i][j],fg_color=self.tableau_couleurs[i][j],width=15,height=15,hover_color=couleur_Surbrillance,command=lambda c=self.tableau_couleurs[i][j]: self.changement_couleur(c))
                bouton.grid(row=i,column=j,padx=2,pady=2)
                
        self.c_placementBackground = 0        
                
        for i in self.liste_background :
            if i == "white" :
                bouton = CTkButton(self.frame_CouleurFond,text="Aucun Fond",text_color=couleur_Fond2,bg_color=i,fg_color=i,height=15,width=129,hover_color=couleur_Surbrillance,command=lambda c=i: self.changement_couleurFond(c))
                bouton.grid(row=0,column=0,columnspan=7,padx=2,pady=2)
            else :
                bouton = CTkButton(self.frame_CouleurFond,text="",bg_color=i,fg_color=i,width=15,height=15,hover_color=couleur_Surbrillance,command=lambda c=i: self.changement_couleurFond(c))
                bouton.grid(row=1,column=self.c_placementBackground,padx=2,pady=2)
                self.c_placementBackground += 1
                    
        self.button_chtCouleur = CTkButton(self.editeurParametres,height=25,width=55,text="A  ▼",font=("Arial",12,"bold"),text_color=couleur_Texte1,command= lambda:self.show_frame(self.frame_Couleur))
        self.button_chtCouleur.configure(fg_color=couleur_Fond,hover_color=couleur_Surbrillance)
        self.button_chtCouleur.grid(row=0,column=0,padx=5,pady=(10,0),sticky="w")
        
        self.button_italic = CTkButton(self.editeurParametres,text="I",font=CTkFont("Times New Roman", 18,"normal","italic"),height=25,width=25,text_color=couleur_Texte1,fg_color=couleur_Fond,hover_color=couleur_Surbrillance,command=lambda:self.changement_italic())
        self.button_italic.grid(row=1,column=0,padx=(5,0),pady=2,sticky="w")
        
        self.button_souligne = CTkButton(self.editeurParametres,text="a",font=CTkFont("Arial", 18,"normal","roman",1),height=25,width=25,text_color=couleur_Texte1,fg_color=couleur_Fond,hover_color=couleur_Surbrillance,command=lambda:self.changement_souligne())
        self.button_souligne.grid(row=1,column=0,padx=(35,0),pady=2,sticky="w")
        
        self.img_Surligneur = CTkImage(light_image=Image.open("image/light/SurligneurLight.png"),dark_image=Image.open("image/dark/SurligneurDark.png"))
        self.img_Surligneur.configure(size=(15,15))
        
        self.button_chtCouleurFond = CTkButton(self.editeurParametres,height=25,width=55,text="▼",image=self.img_Surligneur,font=("Arial",12,"bold"),text_color=couleur_Texte1,anchor="e",compound="left",command = lambda : self.show_frame(self.frame_CouleurFond))
        self.button_chtCouleurFond.configure(fg_color=couleur_Fond,hover_color=couleur_Surbrillance)
        self.button_chtCouleurFond.grid(row=2,column=0,padx=(5,0),pady=2,sticky="w")  
        
        self.option_Police = CTkOptionMenu(self.editeurParametres,height=25,width=200,values=self.liste_police,fg_color=couleur_Fond,button_hover_color=couleur_Fond,dropdown_hover_color=couleur_Surbrillance,button_color=couleur_Fond,text_color=couleur_Texte1,command=self.changement_police)
        self.option_Police.grid(row=0,column=1,padx=(0,0),pady=(10,0),sticky="w") 
        
        self.button_retrecirTexte = CTkButton(self.editeurParametres,height=25,width=55,text="A  ▼",font=("Arial",12,"bold"),text_color=couleur_Texte1,hover_color=couleur_Surbrillance,fg_color=couleur_Fond,command = lambda:self.changement_taille('-')) 
        self.button_retrecirTexte.grid(row=2,column=1,padx=(0,0),pady=2,sticky='w') 
        
        self.option_Taille = CTkOptionMenu(self.editeurParametres,height=25,width=85,values=self.liste_taille_str,fg_color=couleur_Fond,button_hover_color=couleur_Fond,dropdown_hover_color=couleur_Surbrillance,button_color=couleur_Fond,text_color=couleur_Texte1,command=self.changement_taille)
        self.option_Taille.grid(row=2,column=1,padx=(57,0),pady=2,sticky='w')
        self.option_Taille.set("12")
         
        self.button_agrandirTexte = CTkButton(self.editeurParametres,height=25,width=55,text="A  ▲",font=("Arial",18,"bold"),text_color=couleur_Texte1,hover_color=couleur_Surbrillance,fg_color=couleur_Fond,command = lambda:self.changement_taille('+')) 
        self.button_agrandirTexte.grid(row=2,column=1,padx=(145,0),pady=2,sticky='w') 
        
        self.button_barre = CTkButton(self.editeurParametres,text="a",font=CTkFont("Arial", 18,"normal","roman",0,1),height=25,width=25,text_color=couleur_Texte1,fg_color=couleur_Fond,hover_color=couleur_Surbrillance,command=lambda:self.changement_barre())
        self.button_barre.grid(row=1,column=1,padx=(0,0),pady=2,sticky="w")      
    
        ## PAGE 
        
        self.textbox_Page = CTkTextbox(self)
        self.textbox_Page.configure(corner_radius=0,fg_color="white",text_color="white",border_width=3,border_color=couleur_Texte1)
        
        self.textbox_Page._textbox.configure(insertbackground="black",insertborderwidth=2)
        self.textbox_Page.grid(row=1,column=0,sticky="ns",padx=20,pady=5,ipadx=250)
        
        ## TAG STYLE 2
        
        for i in self.liste_police :
            for j in self.liste_taille :
                for k in self.liste_epaisseur :
                    for l in self.liste_slant :
                        for m in self.liste_underline :
                            for n in self.liste_overstrike :
                                self.textbox_Page.tag_config(i + "+" + "0" + f"{j}" + "+" + k + "+" + l + "+" + f"{m}" + "+" + f"{n}",font=CTkFont(family=i,size=j,weight=k,slant=l,underline=m,overstrike=n))
        
        for i in range(len(self.tableau_couleurs)) :
            for j in range(len(self.tableau_couleurs[0])) :
                self.textbox_Page.tag_config(self.tableau_couleurs[i][j],foreground=self.tableau_couleurs[i][j])
                
        for i in self.liste_background :
            if i == 'white' :
                self.textbox_Page.tag_config("background_" + i, background="")
            else :
                self.textbox_Page.tag_config("background_" + i, background=i)       
        
             
            
        self.textbox_Page.tag_config("bold",font=CTkFont("Times New Roman",12,"bold"))
        
        self.textbox_Page.bind("<KeyRelease>",self.on_key)
        
        self.bind("<Button-1>",self.masquer_frame_event)
        self.editeurParametres.bind("<Button-1>",self.masquer_frame_event)
        self.textbox_Page.bind("<Button-1>",self.masquer_frame_event)
        
        self.label_NomFichier2 = CTkLabel(self,text=f"Non enregistré")
        self.label_NomFichier2.grid(row=1,column=0,sticky="nw",padx=5)
        

        
        
        ## BARRE DU BAS
        
        img_Plus = CTkImage(light_image=Image.open("image/light/PlusLight.png"),dark_image=Image.open("image/dark/PlusDark.png"))
        img_Plus.configure(size=(40,40)) 
        
        img_Ouvrir = CTkImage(light_image=Image.open("image/light/OuvrirLight.png"),dark_image=Image.open("image/dark/OuvrirDark.png"))
        img_Ouvrir.configure(size=(40,40)) 
        
        img_Enregistrer = CTkImage(light_image=Image.open("image/light/EnregistrerLight.png"),dark_image=Image.open("image/dark/EnregistrerDark.png"))
        img_Enregistrer.configure(size=(40,40)) 
               
        self.btn_nouvelPage = CTkButton(self,text="",image=img_Plus,height=55,width=55,corner_radius=40,fg_color=couleur_Fond2,hover_color=couleur_Surbrillance,command = lambda : self.nouveau_fichier() )
        self.btn_nouvelPage.grid(row=1,column=0,sticky="se",padx=(0,20),pady=(0,10))
        
        self.btn_Ouvrir = CTkButton(self,text="",image=img_Ouvrir,height=55,width=55,corner_radius=40,fg_color=couleur_Fond2,hover_color=couleur_Surbrillance,command=lambda:self.show_frame(self.frame_Ouvrir))
        self.btn_Ouvrir.grid(row=1,column=0,sticky="se",padx=(0,20),pady=(0,80))
        
        self.btn_Enregistrer = CTkButton(self,text="",image=img_Enregistrer,height=55,width=55,corner_radius=40,fg_color=couleur_Fond2,hover_color=couleur_Surbrillance,command = lambda:self.show_frame(self.frame_Enregister))
        self.btn_Enregistrer.grid(row=1,column=0,sticky="se",padx=(0,20),pady=(0,150))
        
        ## FRAME ENREGISTRER
        
        self.frame_Enregister = CTkFrame(self,border_width=1,fg_color=couleur_Fond2,border_color=couleur_Texte1,corner_radius=0)
        self.frame_Enregister.grid_rowconfigure(0,weight=1)
        self.frame_Enregister.grid_rowconfigure(1,weight=1)
        self.frame_Enregister.grid_rowconfigure(2,weight=1)
        self.frame_Enregister.grid_columnconfigure(0,weight=1)
        
        self.btn_Valider = CTkButton(self.frame_Enregister,text="Enregistrer",command=lambda:self.enregistrer_fichier())
        self.btn_Valider.grid(row=2,column=0,sticky='es',padx=(0,10),pady=(0,10))
        self.btn_Valider.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

        self.btn_Annuler = CTkButton(self.frame_Enregister,text="Annuler",command=lambda:self.masquer_frame(self.frame_Enregister))
        self.btn_Annuler.grid(row=2,column=0,sticky="es",padx=(0,160),pady=(0,10))
        self.btn_Annuler.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

        self.label_Enregistrer = CTkLabel(self.frame_Enregister,text="Enregistrer",font=("Arial",24,"bold"))
        self.label_Enregistrer.grid(row=0,column=0,sticky='nw',padx=(60,0),pady=(20,0))

        self.label_NomFichier = CTkLabel(self.frame_Enregister,text="Nom du fichier",font=("Arial",16,"normal"))
        self.label_NomFichier.grid(row=1,column=0,sticky='nw',padx=(60,0),pady=(20,0))
        
        self.entry_Enregistrer = CTkEntry(self.frame_Enregister,placeholder_text="Nom du fichier")
        self.entry_Enregistrer.grid(row=1,column=0,sticky="nw",padx=(50,0),pady=(70,0),ipadx=100)
        self.entry_Enregistrer.configure(fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,text_color=couleur_Texte1,corner_radius=0)
        
        self.label_ErreurVide = CTkLabel(self.frame_Enregister,text='',text_color="red")
        self.label_ErreurVide.grid(row=1,column=0,sticky="sw",padx=(50,0))
        
        
        ## POP UP - NON ENREGISTRER
        
        self.frame_NonEnregister = CTkFrame(self,border_width=1,fg_color=couleur_Fond2,border_color=couleur_Texte1,corner_radius=0)
        self.frame_NonEnregister.grid_rowconfigure(0,weight=1)
        self.frame_NonEnregister.grid_rowconfigure(1,weight=1)
        self.frame_NonEnregister.grid_rowconfigure(2,weight=1)
        self.frame_NonEnregister.grid_columnconfigure(0,weight=1)
        
        self.btn_Valider = CTkButton(self.frame_NonEnregister,text="Enregistrer",command=lambda:self.choix_enregistrement(1))
        self.btn_Valider.grid(row=2,column=0,sticky='es',padx=(0,10),pady=(0,10))
        self.btn_Valider.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

        self.btn_Annuler = CTkButton(self.frame_NonEnregister,text="Ne pas enregistrer",command=lambda:self.choix_enregistrement(0))
        self.btn_Annuler.grid(row=2,column=0,sticky="es",padx=(0,160),pady=(0,10))
        self.btn_Annuler.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

        self.label_Enregistrer = CTkLabel(self.frame_NonEnregister,text="Fichier non enregistré",font=("Arial",24,"bold"))
        self.label_Enregistrer.grid(row=0,column=0,sticky='nw',padx=(60,0),pady=(20,0))

        self.label_NomFichier = CTkLabel(self.frame_NonEnregister,text="Faites votre choix",font=("Arial",16,"normal"))
        self.label_NomFichier.grid(row=1,column=0,sticky='nw',padx=(60,0),pady=(20,0))
        
        self.masquer_frame_event("event")
        
        ## FRAME OUVRIR FICHIER
        
        self.frame_Ouvrir = CTkFrame(self,border_width=1,fg_color=couleur_Fond2,border_color=couleur_Texte1,corner_radius=0)
        self.frame_Ouvrir.grid_rowconfigure(0,weight=0)
        self.frame_Ouvrir.grid_rowconfigure(1,weight=1)
        self.frame_Ouvrir.grid_rowconfigure(2,weight=0)
        self.frame_Ouvrir.grid_rowconfigure(3,weight=0)
        self.frame_Ouvrir.grid_columnconfigure(0,weight=1)
        
        self.btn_Valider = CTkButton(self.frame_Ouvrir,text="Ouvrir",command=lambda:self.ouvrir_fichier())
        self.btn_Valider.grid(row=3,column=0,sticky='es',padx=(0,10),pady=(0,10))
        self.btn_Valider.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

        self.btn_Annuler = CTkButton(self.frame_Ouvrir,text="Annuler",command=lambda:self.masquer_frame(self.frame_Ouvrir))
        self.btn_Annuler.grid(row=3,column=0,sticky="es",padx=(0,160),pady=(0,10))
        self.btn_Annuler.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)
        
        self.btn_Supprimer = CTkButton(self.frame_Ouvrir,text="Supprimer le fichier",command=lambda:self.supprimer_fichier())
        self.btn_Supprimer.grid(row=3,column=0,sticky="ws",padx=(10,0),pady=(0,10))
        self.btn_Supprimer.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

        self.label_Enregistrer = CTkLabel(self.frame_Ouvrir,text="Ouvrir une note",font=("Arial",24,"bold"))
        self.label_Enregistrer.grid(row=0,column=0,sticky='nw',padx=(60,0),pady=(20,0))
        
        self.lb_Fichiers = CTkListbox(self.frame_Ouvrir)
        self.lb_Fichiers.grid(row=1,column=0,sticky="nsew",padx=5)
        self.lb_Fichiers.configure(border_width=0,hover_color=couleur_Surbrillance,highlight_color=couleur_Bouton2)
        
        self.label_ErreurOuvert = CTkLabel(self.frame_Ouvrir,text='',text_color="red")
        self.label_ErreurOuvert.grid(row=2,column=0,sticky="sw",padx=(50,0))        
        
    
        
        self.masquer_frame_event("event")
        
     
    def on_key(self,event) :
        self.enregistrer = 0
        if event.keysym != 'BackSpace' and event.keysym != 'Delete' :
            if self.c == 0 :
                self.c += 1
                self.textbox_Page.tag_add(self.tag,f"{self.textbox_Page.index("insert")}-1c",self.textbox_Page.index("insert"))
                self.textbox_Page.tag_add(self.font,f"{self.textbox_Page.index("insert")}-1c",self.textbox_Page.index("insert"))
                self.textbox_Page.tag_add(self.background,f"{self.textbox_Page.index("insert")}-1c",self.textbox_Page.index("insert"))
                self.label_NomFichier2.configure(text=f"Non enregistré")
                
            else : 
                self.textbox_Page.tag_add(self.tag,f"{self.textbox_Page.index("insert")}-2c",self.textbox_Page.index("insert"))  
                self.textbox_Page.tag_add(self.font,f"{self.textbox_Page.index("insert")}-2c",self.textbox_Page.index("insert"))
                self.textbox_Page.tag_add(self.background,f"{self.textbox_Page.index("insert")}-2c",self.textbox_Page.index("insert"))
        else :
            self.c = 0

        
    def changement_couleur(self,couleur) :
        self.tag = couleur
        self.c = 0  
        self.masquer_frame(self.frame_Couleur)
        self.button_chtCouleur.configure(text_color=couleur)
        
    def changement_couleurFond(self,couleur) :
        self.background ="background_" + couleur
        self.c = 0
        self.masquer_frame(self.frame_CouleurFond)
        
    def changement_italic(self) :
        self.c = 0
        if "roman" in self.font :
            self.font = self.font.replace("roman","italic")
            self.button_italic.configure(fg_color = couleur_Bouton2)
        else :
            self.font = self.font.replace("italic","roman")
            self.button_italic.configure(fg_color = couleur_Fond)
    
    def changement_souligne(self) :
        self.c = 0
        if self.font[-3] == "0" :
            self.font = self.font[:-3] + "1" + self.font[-2:]
            self.button_souligne.configure(fg_color = couleur_Bouton2)
        else :
            self.font = self.font[:-3] + "0" + self.font[-2:]
            self.button_souligne.configure(fg_color = couleur_Fond)  
            
    def changement_police(self,police) :
        self.c = 0
        for i in self.liste_police :
            if i in self.font :
                self.font = self.font.replace(i,police)
                
    def changement_taille(self,taille) :
        self.c = 0
        if taille == "+" :
            for i in range(len(self.liste_taille_str)) :
                if "0" + self.liste_taille_str[i] in self.font and self.liste_taille_str[i] != '54' :
                    self.font = self.font.replace("0" + self.liste_taille_str[i], "0" + self.liste_taille_str[i+1])
                    self.option_Taille.set(self.liste_taille_str[i+1])
                    return
        elif taille == '-' :
            for i in range(len(self.liste_taille_str)) :
                if "0" + self.liste_taille_str[i] in self.font and self.liste_taille_str[i] != '6'  :
                    self.font = self.font.replace("0" + self.liste_taille_str[i], "0" + self.liste_taille_str[i-1])
                    self.option_Taille.set(self.liste_taille_str[i-1])
                    return 
        else :
            for i in self.liste_taille_str :
                if "0" + i in self.font :
                    self.font = self.font.replace("0" + i, "0" + taille)

    def changement_barre(self) :
        self.c = 0
        if self.font[-1] == "0" :
            self.font = self.font[:-1] + "1" 
            self.button_barre.configure(fg_color = couleur_Bouton2)
        else :
            self.font = self.font[:-1] + "0" 
            self.button_barre.configure(fg_color = couleur_Fond)            
        
    def show_frame(self,frame) :
        if frame == self.frame_Couleur :
            self.masquer_frame(self.frame_CouleurFond)
            frame.place(x=5,y=30)
        if frame == self.frame_CouleurFond :
            frame.place(x=5,y=88)
            self.masquer_frame(self.frame_Couleur)
        if frame == self.frame_Enregister :
            frame.place(x=self.winfo_screenwidth()/4,y=self.winfo_screenheight()/5,relwidth=0.5,relheight=0.4)
            self.entry_Enregistrer.insert(0,self.fichier_ouvert)
        if frame == self.frame_Ouvrir :
            self.label_ErreurOuvert.configure(text="")
            if self.enregistrer == 1 :
                self.lb_Fichiers.delete(0,"END")
                fichier = os.listdir("./notes")
                for i in fichier : 
                    self.lb_Fichiers.insert("END",i[:-5])
                frame.place(x=self.winfo_screenwidth()/4,y=self.winfo_screenheight()/5,relwidth=0.5,relheight=0.4)
            else :
                self.show_frame(self.frame_NonEnregister)  
                self.frame_aOuvrir = frame          
        if frame == self.frame_NonEnregister :
            frame.place(x=self.winfo_screenwidth()/4,y=self.winfo_screenheight()/5,relwidth=0.5,relheight=0.4)
    
    def masquer_frame(self,frame) :
        if frame == self.frame_Couleur :
            self.frame_Couleur.place_forget()
        if frame == self.frame_CouleurFond :
            self.frame_CouleurFond.place_forget()
        else :
            frame.place_forget()
    
    def masquer_frame_event(self,event) :
        self.frame_Couleur.place_forget()
        self.frame_CouleurFond.place_forget()
        
    def enregistrer_fichier(self) :
        if self.entry_Enregistrer.get() == "" :
            self.label_ErreurVide.configure(text='Le nom de fichier ne doit pas être vide')
        else :
            self.masquer_frame(self.frame_Enregister)
            self.label_ErreurVide.configure(text='')
            self.enregistrer = 1
            char = []
            
            if self.fichier_ouvert != self.entry_Enregistrer.get() and self.fichier_ouvert != "" :
                os.remove(f"notes/{self.fichier_ouvert}.json")
            
            self.fichier_ouvert = self.entry_Enregistrer.get()
                
            self.label_NomFichier2.configure(text=f"{self.fichier_ouvert} - Enregistré")
            
            indice = "1.0" 
            fin = self.textbox_Page.index("end-1c")
            
            while self.textbox_Page.compare(indice,"<=",fin) :
                caractere = self.textbox_Page.get(indice)
                tags = self.textbox_Page.tag_names(indice)
                
                char.append({"char" : caractere, "tags" : list(tags)})
                
                indice = self.textbox_Page.index(f"{indice} + 1c")
            
            with open(f"notes/{self.entry_Enregistrer.get()}.json","w") as f :
                json.dump(char,f,indent=4,ensure_ascii=False)
            f.close()
    
    
    def ouvrir_fichier(self) :
        if self.lb_Fichiers.get() :
            with open(f"notes/{self.lb_Fichiers.get()}.json",'r') as f :
                data = json.load(f)
            f.close()
            self.textbox_Page.delete("1.0","end-1c")
            self.fichier_ouvert = self.lb_Fichiers.get()
            self.label_NomFichier2.configure(text=f"{self.fichier_ouvert} - Enregistré")
            
            index = "1.0"
            
            for item in data :
                char = item["char"]
                tag = item["tags"]
                
                self.textbox_Page.insert(index,char,tag)
                
                index = self.textbox_Page.index(f"{index} + 1c")
            
            
            self.masquer_frame(self.frame_Ouvrir)
            
    
    def nouveau_fichier(self) :
        if self.enregistrer == 0 :
            self.show_frame(self.frame_NonEnregister)
            self.frame_aOuvrir = "nouveau"
        else :
            self.fichier_ouvert = ""
            self.textbox_Page.delete("1.0", "end-1c")
            self.label_NomFichier2.configure(text=f"Non enregistré")
    
    def choix_enregistrement(self,choix) :
        if choix == 0 :
            self.masquer_frame(self.frame_NonEnregister)
            self.enregistrer = 1
            if self.frame_aOuvrir == "nouveau" :
                self.nouveau_fichier()
            else :
                self.show_frame(self.frame_aOuvrir)
        else :
            self.masquer_frame(self.frame_NonEnregister)
            if self.fichier_ouvert != "" :
                self.enregistrer_fichier()   
                self.show_frame(self.frame_aOuvrir)
            else :
                self.show_frame(self.frame_Enregister)
                
    def supprimer_fichier(self) :
        if self.lb_Fichiers.get() and self.lb_Fichiers.get() != self.fichier_ouvert :
            os.remove(f'notes/{self.lb_Fichiers.get()}.json')
            self.lb_Fichiers.delete(0,"END")
            fichier = os.listdir("./notes")
            for i in fichier : 
                self.lb_Fichiers.insert("END",i[:-5])
        elif self.lb_Fichiers.get() and self.lb_Fichiers.get() == self.fichier_ouvert :
            self.label_ErreurOuvert.configure(text="Suppression impossible. Fichier ouvert")
            