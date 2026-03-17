from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage
from os import *
from PIL import Image
import time
from math import ceil

set_appearance_mode("dark")
set_default_color_theme("blue")

fenetre = CTk()
fenetre.title("ESEOFOX")
icon = PhotoImage(file="IconBitMap_ESEOFOX.png")
fenetre.iconphoto(True,icon)
fenetre.attributes("-alpha",1)

global ws
global hs
ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()
fenetre.geometry(f"{ws}x{hs}")
fenetre.minsize(int(ws/2),int(hs/2))
fenetre.maxsize(ws,hs)


set_appearance_mode("light")
set_default_color_theme("blue")

# Frame Principal -------------------

framePrincpal = CTkFrame(fenetre,width=fenetre.winfo_width(),height=fenetre.winfo_height(),fg_color="gray30")
framePrincpal.grid(row=0,column=0,sticky="nsew")

frameBarreSuperieur = CTkFrame(framePrincpal,width=ws,height=75,fg_color="gray21")
frameBarreSuperieur.grid(row=0,column=0,sticky=N)
frameBarreSuperieur.grid_propagate(False)
frameBarreSuperieur.grid_columnconfigure(0,weight=1)
frameBarreSuperieur.grid_columnconfigure(1,weight=1)
frameBarreSuperieur.grid_columnconfigure(2,weight=1)
frameBarreSuperieur.grid_rowconfigure(0,weight=1)
frameBarreSuperieur.grid_rowconfigure(2,weight=1)

frameMenuPrincipal = CTkFrame(framePrincpal,width=ws,height=hs-75,fg_color="gray30")
frameMenuPrincipal.grid(row=1,column=0,sticky=N)
frameMenuPrincipal.grid_propagate(False)



# ------------------ Frame Principal


# Fonction -------------------------

def recherche(texte) :
    L_application = ["contacts","morpion","snake","notes","messages","wiki","chrono"]
    if texte == "" :
        listRecherche.place_forget()
        listRecherche.configure(height=0)
    else :
        listRecherche.place(x=720,y=60)
        listRecherche.lift()
        listRecherche.delete(0, "END")
        listeElement = [item for item in L_application if texte.lower() in item]
        listRecherche.configure(height=len(listeElement)*35 if listeElement else 0)
        if len(listeElement) == 0 :
            listRecherche.place_forget() 
        for item in listeElement :
            listRecherche.insert("END",item.capitalize())
                

fenetre._set_scaling(1,1)

def ch_taille(ws,hs) :
    if fenetre.winfo_height != ws :
        ws = fenetre.winfo_height()
        hs = fenetre.winfo_width()
        print(ws,":",hs)
        boutton_frame.configure(height=45)
                
        
# ------------------------ Fonction



# Widgets --------------------------------

frameBarreRecherche = CTkFrame(frameBarreSuperieur,width=500,height=45)
imageLogo = CTkImage(Image.open("IconBitMap_ESEOFOX.png"),size=(70,70))
imageLoupe = CTkImage(Image.open("icone-loupe-gris.png"),size=(30,30))
image_label = CTkLabel(frameBarreSuperieur,image=imageLogo,text="")
boutton_frame = CTkButton(frameBarreSuperieur,text="Accueil",height=45)
barreRecherche = CTkEntry(frameBarreRecherche,placeholder_text="Rechercher une application",width=500,height=45)
imageBarre_lavel = CTkLabel(frameBarreRecherche,image=imageLoupe,text="")
listRecherche = CTkListbox(fenetre,width=500,height=30)
listRecherche._scrollbar.configure(button_color="gray21",button_hover_color="gray21")

frameMenuLateral = CTkFrame(frameMenuPrincipal,width=200,height=hs-200)

logo_label = CTkLabel(frameMenuLateral,text="ESEOFOX",font=CTkFont(size=20,weight="bold"))
btn_settings = CTkButton(frameMenuLateral, text="Paramètres")
btn_help = CTkButton(frameMenuLateral, text="Aide")
switch_theme = CTkSwitch(frameMenuLateral, text ="Sombre/Clair")


frameMenuApplications = CTkFrame(frameMenuPrincipal,width=ws-250,height=hs-200)

label_App = CTkLabel(frameMenuApplications,text="Applications")

frameScrollApp = CTkScrollableFrame(frameMenuApplications,width=ws-200-70,height=hs-200)
frameScrollApp.grid(row=1,column=0,padx=5,pady=0)

chronoImage = CTkImage(Image.open("Chrono_darkmode.png"), size=(90, 90))
button_chronoImage = CTkButton(frameScrollApp, image=chronoImage, text="", fg_color= "transparent")

snakeImage = CTkImage(light_image=Image.open("Snake.png"), size=(90, 90))
button_snakeImage = CTkButton(frameScrollApp, image=snakeImage, text="", fg_color= "transparent")

notesImage = CTkImage(light_image=Image.open("Notes.png"), size=(90, 90))
button_notesImage = CTkButton(frameScrollApp, image=notesImage, text="", fg_color= "transparent")

morpionImage = CTkImage(light_image=Image.open("Morpion.png"), size=(90, 90))
button_morpionImage = CTkButton(frameScrollApp, image=morpionImage, text="", fg_color= "transparent")

contactsImage = CTkImage(light_image=Image.open("Contacts.png"), size=(90, 90))
button_contactsImage = CTkButton(frameScrollApp, image=contactsImage, text="", fg_color= "transparent")

messagesImage = CTkImage(light_image=Image.open("Messages.png"), size=(90, 90))
button_messagesImage = CTkButton(frameScrollApp, image=messagesImage, text="", fg_color= "transparent")

wikiImage = CTkImage(light_image=Image.open("Wiki.png"), size=(90, 90))
button_wikiImage = CTkButton(frameScrollApp, image=wikiImage, text="", fg_color= "transparent")

L=[button_chronoImage,button_contactsImage,button_messagesImage,button_morpionImage,button_notesImage,button_snakeImage,button_wikiImage]

#--------------------------------  Widgets


# Méthode de widget ----------------------

barreRecherche.bind("<KeyRelease>",lambda event: recherche(barreRecherche.get()))

fenetre.bind("<Configure>",lambda event : ch_taille(ws,hs))

# --------------------- Méthode de widget



# Style ---------------------------------
# text_color    : couleur du texte             "color"      Liste des couleurs : https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html
# fg_color      : couleur du premier plan      "color"
# bg_color      : couleur du fond              "color"
# hover_color   : couleur de survol            "color"
# font          : police et taille du texte   ("Arial",14,"Bold")
# corner_radius : arrondi des coins            int
# border_width  : largeur de la bordure        int
# border_color  : couleur de la bordure        "color"

frameBarreRecherche.configure(fg_color="gray21")

imageLogo.configure()
imageLoupe.configure()
image_label.configure()
boutton_frame.configure(height=100)
barreRecherche.configure(font=CTkFont(size=12),corner_radius=5,fg_color="gray21",text_color="white")
listRecherche.configure(fg_color="gray21",corner_radius=0,bg_color="transparent",border_width=2)
imageBarre_lavel.configure(fg_color="transparent")
listRecherche.configure(text_color="white")


frameMenuLateral.configure(fg_color="gray21")

logo_label.configure(text_color="white")
switch_theme.configure(text_color="white")


frameMenuApplications.configure(fg_color="gray21")

label_App.configure(text_color="white",font=CTkFont("Arial",size=20))

frameScrollApp.configure(fg_color="grey21",corner_radius=0)

# --------------------------------  Style


# Placement des Widgets -----------------

frameBarreRecherche.grid(row=0,column=1)
image_label.grid(row=0,column=2,padx=10,pady=10,sticky="e",ipadx=20)
boutton_frame.grid(row=0,column=0,sticky="w",padx=20)
barreRecherche.grid(row=0,column=1)
imageBarre_lavel.grid(row=0,column=1,sticky="e",padx=10)

frameMenuLateral.grid(row=0,column=0,pady=25,padx=10)
frameMenuLateral.grid_propagate(False)
frameMenuLateral.grid_columnconfigure(0,weight=1)

logo_label.grid(row=0,column=0,sticky="we",pady=20)
btn_settings.grid(row=1,column=0,pady=10)
btn_help.grid(row=2,column=0,pady=10)
switch_theme.grid(row=3,column=0,pady=10)

frameMenuApplications.grid(row=0,column=1,pady=25,padx=10)
frameMenuApplications.grid_propagate(False)
frameMenuApplications.grid_columnconfigure(0,weight=1)

label_App.grid(row=0,column=0,padx=10,pady=10)

frameScrollApp.grid_propagate()

frameMenuApplications.grid_columnconfigure(0,weight=1)
frameMenuApplications.grid_columnconfigure(1,weight=1)
frameMenuApplications.grid_columnconfigure(2,weight=1)
frameMenuApplications.grid_columnconfigure(3,weight=1)
frameMenuApplications.grid_columnconfigure(4,weight=1)
frameMenuApplications.grid_columnconfigure(5,weight=1)
frameMenuApplications.grid_columnconfigure(6,weight=1)

button_snakeImage.grid()
button_wikiImage.grid()
button_chronoImage.grid()
button_contactsImage.grid()
button_messagesImage.grid()
button_morpionImage.grid()
button_notesImage.grid()

fenetre.update_idletasks()

column_app = int(frameScrollApp.winfo_width()/110)
row_app = int(ceil(len(L)/9))

c=0

for i in range(row_app) :
    for j in range(column_app) :
        if c < len(L) :
            L[c].grid_configure(row=i,column=j,pady=10,padx=10)
            c += 1
        else :
            pass
   
# ----------------  Placements des Widgets

fenetre.mainloop()