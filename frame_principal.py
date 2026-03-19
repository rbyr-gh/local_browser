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
                


def ch_taille(ws,hs) :
    if fenetre.winfo_height != ws :
        fenetre.update_idletasks()
        scalingW = fenetre.winfo_width()/ws
        scalingH = fenetre.winfo_height()/hs
        frame_BarreRecherche.configure(height=int(hs/10*scalingH),width=int(ws*scalingW))
        frame_BarreRecherche.grid_propagate(False)
        frame_MenuLateral.configure(height=int((hs-hs/10-50)*scalingH),width=int((ws/9)*scalingW))
        frame_MenuLateral.grid_propagate(False)
        frame_MenuApplications.configure(height=int((hs-hs/10-50)*scalingH),width=int((ws-ws/9-40)*scalingW))
        frame_ScrollApp.configure(height=((hs-hs/10-100)*scalingH),width=int((ws-270)*scalingW))
        print(fenetre.winfo_height())
        fenetre.update_idletasks()

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
                        
        
# ------------------------ Fonction

# Initaliser taille widget en fonction dimension de base
# Modifier taille wiidget en fonction du redimensionnement 


# Widgets --------------------------------

frame_BarreRecherche = CTkFrame(frameBarreSuperieur)

img_LogoBarre = CTkImage(Image.open("IconBitMap_ESEOFOX.png"))
img_Loupe = CTkImage(Image.open("icone-loupe-gris.png"))
img_Label = CTkLabel(frameBarreSuperieur,image=img_LogoBarre,text="")
btn_Frame = CTkButton(frameBarreSuperieur,text="Accueil")
entry_barreRecherche = CTkEntry(frame_BarreRecherche,placeholder_text="Rechercher une application")
label_Loupe = CTkLabel(frame_BarreRecherche,image=img_Loupe,text="")
lBox_Recherche = CTkListbox(fenetre)
lBox_Recherche._scrollbar.configure(button_color="gray21",button_hover_color="gray21")

frame_MenuLateral = CTkFrame(frameMenuPrincipal)

label_LogoFP = CTkLabel(frame_MenuLateral,text="ESEOFOX")
btn_Settings = CTkButton(frame_MenuLateral, text="Paramètres")
btn_Help = CTkButton(frame_MenuLateral, text="Aide")
switch_Theme = CTkSwitch(frame_MenuLateral, text ="Sombre/Clair")


frame_MenuApplications = CTkFrame(frameMenuPrincipal)

label_App = CTkLabel(frame_MenuApplications,text="Applications")

frame_ScrollApp = CTkScrollableFrame(frame_MenuApplications)
frame_ScrollApp.grid(row=1,column=0,padx=5,pady=40)

chronoImage = CTkImage(Image.open("Chrono_darkmode.png"))
btn_chronoImage = CTkButton(frame_ScrollApp, image=chronoImage, text="", fg_color= "transparent")

snakeImage = CTkImage(light_image=Image.open("Snake.png"))
btn_snakeImage = CTkButton(frame_ScrollApp, image=snakeImage, text="", fg_color= "transparent")

notesImage = CTkImage(light_image=Image.open("Notes.png"))
btn_notesImage = CTkButton(frame_ScrollApp, image=notesImage, text="", fg_color= "transparent")

morpionImage = CTkImage(light_image=Image.open("Morpion.png"))
btn_morpionImage = CTkButton(frame_ScrollApp, image=morpionImage, text="", fg_color= "transparent")

contactsImage = CTkImage(light_image=Image.open("Contacts.png"))
btn_contactsImage = CTkButton(frame_ScrollApp, image=contactsImage, text="", fg_color= "transparent")

messagesImage = CTkImage(light_image=Image.open("Messages.png"))
btn_messagesImage = CTkButton(frame_ScrollApp, image=messagesImage, text="", fg_color= "transparent")

wikiImage = CTkImage(light_image=Image.open("Wiki.png"))
btn_wikiImage = CTkButton(frame_ScrollApp, image=wikiImage, text="", fg_color= "transparent")

L=[btn_chronoImage,btn_contactsImage,btn_messagesImage,btn_morpionImage,btn_notesImage,btn_snakeImage,btn_wikiImage]

#--------------------------------  Widgets

frame_BarreRecherche.configure(height=hs/10,width=ws)

img_LogoBarre.configure(size=(70,70))
img_Loupe.configure(size=(30,30))
img_Label.configure()
btn_Frame.configure(height=45)
entry_barreRecherche.configure(height=45,width=500)
label_Loupe.configure()
lBox_Recherche.configure(height=30,width=500)

frame_MenuLateral.configure(height=hs-hs/10-50,width=ws/9)

label_LogoFP.configure()
btn_Settings.configure()
btn_Help.configure()
switch_Theme.configure()


frame_MenuApplications.configure(height=hs-hs/10-50,width=ws-ws/9-40)
frame_MenuApplications.grid_propagate(False)

label_App.configure()

frame_ScrollApp.configure(height=hs-hs/10-100,width=ws-270)

chronoImage.configure(size=(90, 90))
btn_chronoImage.configure(height=100,width=100)

snakeImage.configure(size=(90, 90))
btn_snakeImage.configure(height=100,width=100)

notesImage.configure(size=(90, 90))
btn_notesImage.configure(height=100,width=100)

morpionImage.configure(size=(90, 90))
btn_morpionImage.configure(height=100,width=100)

contactsImage.configure(size=(90, 90))
btn_contactsImage.configure(height=100,width=100)

messagesImage.configure(size=(90, 90))
btn_messagesImage.configure(height=100,width=100)

wikiImage.configure(size=(90, 90))
btn_wikiImage.configure(height=100,width=100)


# Méthode de widget ----------------------

entry_barreRecherche.bind("<KeyRelease>",lambda event: recherche(entry_barreRecherche.get()))

fenetre.bind("<Configure>",lambda event : ch_taille(ws,hs))

# --------------------- Méthode de widget


# Taille des widgets --------------------




# -------------------- Taille des widgets


# Style ---------------------------------
# text_color    : couleur du texte             "color"      Liste des couleurs : https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html
# fg_color      : couleur du premier plan      "color"
# bg_color      : couleur du fond              "color"
# hover_color   : couleur de survol            "color"
# font          : police et taille du texte   ("Arial",14,"Bold")
# corner_radius : arrondi des coins            int
# border_width  : largeur de la bordure        int
# border_color  : couleur de la bordure        "color"

frame_BarreRecherche.configure(fg_color="gray21")

img_LogoBarre.configure()
img_Loupe.configure()
img_Label.configure()
entry_barreRecherche.configure(font=CTkFont(size=12),corner_radius=5,fg_color="gray21",text_color="white")
lBox_Recherche.configure(fg_color="gray21",corner_radius=0,bg_color="transparent",border_width=2)
label_Loupe.configure(fg_color="transparent")
lBox_Recherche.configure(text_color="white")


frame_MenuLateral.configure(fg_color="gray21")

label_LogoFP.configure(text_color="white",font=CTkFont(size=20,weight="bold"))
switch_Theme.configure(text_color="white")


frame_MenuApplications.configure(fg_color="gray21")

label_App.configure(text_color="white",font=CTkFont("Arial",size=20))

frame_ScrollApp.configure(fg_color="grey21",corner_radius=0)

# --------------------------------  Style


# Placement des Widgets -----------------

frame_BarreRecherche.grid(row=0,column=1)

img_Label.grid(row=0,column=2,padx=10,pady=10,sticky="e",ipadx=20)
btn_Frame.grid(row=0,column=0,sticky="w",padx=20)
entry_barreRecherche.grid(row=0,column=1)
label_Loupe.grid(row=0,column=1,sticky="e",padx=10)


frame_MenuLateral.grid(row=0,column=0,pady=25,padx=10)
frame_MenuLateral.grid_propagate(False)
frame_MenuLateral.grid_columnconfigure(0,weight=1)

label_LogoFP.grid(row=0,column=0,sticky="we",pady=20)
btn_Settings.grid(row=1,column=0,pady=10)
btn_Help.grid(row=2,column=0,pady=10)
switch_Theme.grid(row=3,column=0,pady=10)


frame_MenuApplications.grid(row=0,column=1,pady=25,padx=10)
frame_MenuApplications.grid_columnconfigure(0,weight=1)

label_App.grid(row=0,column=0,padx=10,pady=10)
frame_ScrollApp.grid(row=1,column=0,padx=5,pady=0)


frame_MenuApplications.grid_columnconfigure(0,weight=1)
frame_MenuApplications.grid_columnconfigure(1,weight=1)
frame_MenuApplications.grid_columnconfigure(2,weight=1)
frame_MenuApplications.grid_columnconfigure(3,weight=1)
frame_MenuApplications.grid_columnconfigure(4,weight=1)
frame_MenuApplications.grid_columnconfigure(5,weight=1)
frame_MenuApplications.grid_columnconfigure(6,weight=1)

btn_snakeImage.grid()
btn_wikiImage.grid()
btn_chronoImage.grid()
btn_contactsImage.grid()
btn_messagesImage.grid()
btn_morpionImage.grid()
btn_notesImage.grid()

fenetre.update_idletasks()

column_app = int((ws-270)/120)
row_app = int(ceil(len(L)/column_app))
c=0

for i in range(row_app) :
    for j in range(column_app) :
        if c < len(L) :
            L[c].grid_configure(row=i,column=j,pady=10,padx=10)
            c += 1
        else :
            pass
   
# ----------------  Placements des Widgets

print(fenetre.winfo_height())
fenetre.mainloop()
