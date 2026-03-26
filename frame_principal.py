from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage,filedialog
from PIL import Image
import time
import os
from math import ceil
from csv import *
import re


from applications.app_morpion import frame_Morpion

# Style ---------------------------------
# text_color    : couleur du texte             "color"      Liste des couleurs : https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html
# fg_color      : couleur du premier plan      "color"
# bg_color      : couleur du fond              "color"
# hover_color   : couleur de survol            "color"
# font          : police et taille du texte   ("Arial",14,"Bold")
# corner_radius : arrondi des coins            int
# border_width  : largeur de la bordure        int
# border_color  : couleur de la bordure        "color"

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

set_appearance_mode("dark")
theme = "dark"

fenetre = CTk()
fenetre.title("ESEOFOX")
icon = PhotoImage(file="image/IconBitMap_ESEOFOX.png")
fenetre.iconphoto(True,icon)

global ws
global hs
global profil

profil = ""
ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()
fenetre.geometry(f"{ws}x{hs}")
fenetre.minsize(int(ws/2),int(hs/2))
fenetre.maxsize(ws,hs)

fenetre.grid_rowconfigure(0,weight=1)
fenetre.grid_columnconfigure(0,weight=1)

framePrincipal = CTkFrame(fenetre,fg_color=couleur_Fond)
framePrincipal.rowconfigure(0,weight=0)
framePrincipal.rowconfigure(1,weight=1)
framePrincipal.columnconfigure(0,weight=1)
framePrincipal.grid(row=0,column=0,sticky="nsew")


# FONCTION CHANGEMENT DE FRAME 

def show_frame_app(frame) :
    frame.tkraise()
    
def show_frame(frame) :
    label_Error.configure(text="")
    label_ErrorC.configure(text="")
    if frame == frameMenuPrincipal :
        frame.tkraise()
        frame_MenuApplications.tkraise()
    elif frame == framePrincipal :
        frame.tkraise()
        show_frame(frameMenuPrincipal)
    else :
        frame.tkraise()
    fenetre.focus_force()    
    
def switch_theme():
    global theme
    if theme == "dark":
        set_appearance_mode("light")
        theme = "light"
    else:
        set_appearance_mode("dark")
        theme = 'dark'
        
def red_fen(event) :
    if lBox_Recherche.winfo_ismapped() :
        lBox_Recherche.place(x=fenetre.winfo_width()/2-240,y=60)
    if frame_chtPrenom.winfo_ismapped() :
        frame_chtPrenom.place(x=fenetre.winfo_width()/4,y=fenetre.winfo_height()/5)
        
def creer_compte() :
    label_Error.configure(text="")

    mdp = entry_MdP1.get()
    mail = entry_Mail1.get()
    prenom = entry_Profil2.get()
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,mail) is None :
        label_Error.configure(text="Mauvais format d'adresse mail")
    else :
        if len(mdp) < 8 or not re.search(r"[A-Z]",mdp) or not re.search(r"[a-z]",mdp) or not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]']", mdp):
             label_Error.configure(text="Le mot de passe doit contenir : 8 caractères, 1 majuscule, 1 minuscule, 1 caractère spécial")
        else : 
            if re.match(r"^[a-zA-Z]+$", prenom) == None :
                label_Error.configure(text="Le prénom ne doit contenir que des lettres")
            else :
                L = []
                with open('local/identifiant.csv',newline='') as csvfile :
                    spamreader = reader(csvfile, delimiter=",")
                    for row in spamreader :
                        L.append(row[1])
                if mail in L :
                    label_Error.configure(text="Adresse mail déja existante")
                else :
                    with open('local/identifiant.csv','a',newline='') as csvfile :
                        ecrire=writer(csvfile)
                        ecrire.writerow([prenom,mail,mdp])
                    csvfile.close()
                    show_frame(frame_Connexion)
                    entry_MdP1.delete(0,"end")
                    entry_Mail1.delete(0,"end")
                    entry_Profil2.delete(0,"end") 
                    
def connexion() :
    global profil
    label_ErrorC.configure(text="")
    
    mdp = entry_MdP.get()
    mail = entry_Mail.get()
    
    L = []
    with open('local/identifiant.csv',newline='') as csvfile :
        spamreader = reader(csvfile, delimiter=",")
        for row in spamreader :
            L.append(row) 
    csvfile.close()
    check = False 
    
    for idd in L :
        if mail in idd and mdp in idd :
            check = True
            prenom = idd[0]  
    
    if check == False :
        label_ErrorC.configure(text="Ce compte n'existe pas")
    else :
        optionMenu_Profil.configure(text=prenom)
        show_frame(framePrincipal)
        entry_MdP.delete(0,"end")
        entry_Mail.delete(0,"end")
        
 

        
## FRAME CONNEXION 

frame_Connexion = CTkFrame(fenetre)

frame_Connexion.grid(row=0,column=0,sticky="nsew")

frame_Connexion.grid_columnconfigure(0,weight=2)
frame_Connexion.grid_columnconfigure(1,weight=1)

frame_Connexion.grid_rowconfigure(0,weight=1)

frame_C1 = CTkFrame(frame_Connexion)
frame_C1.grid(row=0,column=0,sticky="nsew")
frame_C1.configure(fg_color=couleur_Texte1,corner_radius=0)
frame_C1.grid_columnconfigure(0,weight=1)
frame_C1.grid_rowconfigure(0,weight=1)

img_Connexion = CTkImage(Image.open("image/imageConnexion.jpg"))
img_Connexion.configure(size=(ws,hs))

label_Image = CTkLabel(frame_Connexion,text="",image=img_Connexion) 
label_Image.grid(row=0,column=0,columnspan=2,sticky="nsew")
 
frame_C2 = CTkFrame(frame_Connexion)

frame_C2.grid(row=0,column=1,sticky="nsew")   
frame_C2.configure(fg_color=couleur_Fond,corner_radius=0)
frame_C2.grid_rowconfigure(0,weight=1)
frame_C2.grid_rowconfigure(1,weight=1)
frame_C2.grid_rowconfigure(2,weight=0)
frame_C2.grid_rowconfigure(3,weight=0)
frame_C2.grid_rowconfigure(4,weight=0)
frame_C2.grid_rowconfigure(5,weight=7)

frame_C2.grid_columnconfigure(0,weight=1)

label_Bjr = CTkLabel(frame_C2,text="Bon retour parmi nous !")
label_Bjr.configure(font=CTkFont('Arial',size=50,weight='bold'),text_color=couleur_Texte1)
label_Bjr.grid(row=0,column=0,pady=(0,0),padx=(50,0),sticky="ws")

label_Co = CTkLabel(frame_C2,text="Connectez-vous à votre compte")
label_Co.configure(font=CTkFont('Arial',size=17,weight='normal'),text_color=couleur_Texte2)
label_Co.grid(row=1,column=0,padx=(50,0),sticky='wn')

img_Cadena = CTkImage(light_image=Image.open("image/light/CadenaLight.png"),dark_image=Image.open("image/dark/CadenaDark.png"))
img_Mail = CTkImage(light_image=Image.open("image/light/MailLight.png"),dark_image=Image.open("image/dark/MailDark.png"))
img_Mail.configure(size=(40,40))
img_Cadena.configure(size=(25,25))

frame_Donnees = CTkFrame(frame_C2)
frame_Donnees.grid(row=2,column=0,sticky="nsew")
frame_Donnees.configure(fg_color=couleur_Fond)
frame_Donnees.grid_rowconfigure(0,weight=0)
frame_Donnees.grid_rowconfigure(1,weight=0)
frame_Donnees.grid_rowconfigure(2,weight=0)
frame_Donnees.grid_rowconfigure(3,weight=0)

label_imgMail = CTkLabel(frame_Donnees,text='',image=img_Mail)
label_imgMail.grid(row=0,column=0,sticky='sw',padx=(50,0),pady=(0,0))

label_Mail = CTkLabel(frame_Donnees,text="Email : ")
label_Mail.configure(font=CTkFont('Arial',size=23,weight='normal'),text_color=couleur_Texte1)
label_Mail.grid(row=0,column=0,padx=(100,0),sticky='sw',pady=(0,6))

entry_Mail = CTkEntry(frame_Donnees)
entry_Mail.configure(fg_color=couleur_Fond,border_color=couleur_Texte1,border_width=1)
entry_Mail.grid(row=1,column=0,padx=(50,0),sticky='nw',ipadx=200,ipady=5,pady=(0,20))

label_imgMdP = CTkLabel(frame_Donnees,text='',image=img_Cadena)
label_imgMdP.grid(row=2,column=0,sticky='nw',padx=(55,0),pady=(5,0))

label_MdP = CTkLabel(frame_Donnees,text="Mot de Passe : ")
label_MdP.configure(font=CTkFont('Arial',size=23,weight='normal'),text_color=couleur_Texte1)
label_MdP.grid(row=2,column=0,padx=(87,0),sticky='nw',pady=(4,0))

entry_MdP = CTkEntry(frame_Donnees,show="*")
entry_MdP.configure(fg_color=couleur_Fond,border_color=couleur_Texte1,border_width=1)
entry_MdP.grid(row=3,column=0,padx=(50,0),sticky='nw',ipadx=200,ipady=5,pady=2)

btn_Login = CTkButton(frame_C2,text="Se connecter",command= connexion)
btn_Login.grid(row=3,column=0,sticky="nw",padx=(50,0),ipadx=200,ipady=5,pady=(20,10))
btn_Login.configure(fg_color=couleur_Bouton2,hover_color=couleur_Surbrillance,font=CTkFont('Arial',size=20),text_color=couleur_Texte1)

btn_CreerCompte = CTkButton(frame_C2,text="Créer un compte",command = lambda : show_frame(frame_CreationCompte))
btn_CreerCompte.grid(row=4,column=0,sticky="nw",padx=(50,0),ipadx=190,ipady=5)
btn_CreerCompte.configure(fg_color=couleur_Fond,hover_color=couleur_Surbrillance,border_width=1,border_color=couleur_Bord,font=CTkFont('Arial',size=20),text_color=couleur_Texte1)

label_ErrorC = CTkLabel(frame_C2,text="")
label_ErrorC.grid(row=5,column=0,padx=(50,0),sticky='wn')
label_ErrorC.configure(text_color="red")
    

## FRAME CREATION COMPTE

frame_CreationCompte = CTkFrame(fenetre)

frame_CreationCompte.grid(row=0,column=0,sticky="nsew")

frame_CreationCompte.grid_columnconfigure(0,weight=2)
frame_CreationCompte.grid_columnconfigure(1,weight=1)

frame_CreationCompte.grid_rowconfigure(0,weight=1)

frame_C1 = CTkFrame(frame_CreationCompte)
frame_C1.grid(row=0,column=0,sticky="nsew")
frame_C1.configure(fg_color=couleur_Texte1,corner_radius=0)
frame_C1.grid_columnconfigure(0,weight=1)
frame_C1.grid_rowconfigure(0,weight=1)

label_Image = CTkLabel(frame_CreationCompte,text="",image=img_Connexion) 
label_Image.grid(row=0,column=0,columnspan=2,sticky="nsew")
 
frame_CC2 = CTkFrame(frame_CreationCompte)

frame_CC2.grid(row=0,column=1,sticky="nsew")   
frame_CC2.configure(fg_color=couleur_Fond,corner_radius=0)
frame_CC2.grid_rowconfigure(0,weight=1)
frame_CC2.grid_rowconfigure(1,weight=1)
frame_CC2.grid_rowconfigure(2,weight=0)
frame_CC2.grid_rowconfigure(3,weight=0)
frame_CC2.grid_rowconfigure(4,weight=7)

frame_CC2.grid_columnconfigure(0,weight=1)

img_Profil2 = CTkImage(dark_image=Image.open("image/dark/Profil2Dark.png"),light_image=Image.open("image/light/Profil2Light.png"))
img_Profil2.configure(size=(35,35))

btn_retour = CTkButton(frame_CC2,text="<  Retour",command= lambda : show_frame(frame_Connexion))
btn_retour.grid(row=0,column=0,sticky="ne",pady=30,padx=30)
btn_retour.configure(fg_color=couleur_Bouton2,hover_color=couleur_Surbrillance)

label_Bjr = CTkLabel(frame_CC2,text="L'aventure débute ici !")
label_Bjr.configure(font=CTkFont('Arial',size=50,weight='bold'),text_color=couleur_Texte1)
label_Bjr.grid(row=0,column=0,pady=(0,0),padx=(50,0),sticky="ws")

label_Co = CTkLabel(frame_CC2,text="Rentrez vos informations pour commencer")
label_Co.configure(font=CTkFont('Arial',size=17,weight='normal'),text_color=couleur_Texte2)
label_Co.grid(row=1,column=0,padx=(50,0),sticky='wn')

frame_Donnees = CTkFrame(frame_CC2)
frame_Donnees.grid(row=2,column=0,sticky="nsew")
frame_Donnees.configure(fg_color=couleur_Fond)
frame_Donnees.grid_rowconfigure(0,weight=0)
frame_Donnees.grid_rowconfigure(1,weight=0)
frame_Donnees.grid_rowconfigure(2,weight=0)
frame_Donnees.grid_rowconfigure(3,weight=0)

label_imgProfil2 = CTkLabel(frame_Donnees,text='',image=img_Profil2)
label_imgProfil2.grid(row=0,column=0,sticky='sw',padx=(50,0),pady=(0,0))

label_Profil2 = CTkLabel(frame_Donnees,text="Prénom : ")
label_Profil2.configure(font=CTkFont('Arial',size=23,weight='normal'),text_color=couleur_Texte1)
label_Profil2.grid(row=0,column=0,padx=(90,0),sticky='sw',pady=(0,6))

entry_Profil2 = CTkEntry(frame_Donnees)
entry_Profil2.configure(fg_color=couleur_Fond,border_color=couleur_Texte1,border_width=1)
entry_Profil2.grid(row=1,column=0,padx=(50,0),sticky='nw',ipadx=200,ipady=5,pady=(0,20))

label_imgMail = CTkLabel(frame_Donnees,text='',image=img_Mail)
label_imgMail.grid(row=2,column=0,sticky='sw',padx=(50,0),pady=(0,0))

label_Mail = CTkLabel(frame_Donnees,text="Email : ")
label_Mail.configure(font=CTkFont('Arial',size=23,weight='normal'),text_color=couleur_Texte1)
label_Mail.grid(row=2,column=0,padx=(100,0),sticky='sw',pady=(0,6))

entry_Mail1 = CTkEntry(frame_Donnees)
entry_Mail1.configure(fg_color=couleur_Fond,border_color=couleur_Texte1,border_width=1)
entry_Mail1.grid(row=3,column=0,padx=(50,0),sticky='nw',ipadx=200,ipady=5,pady=(0,20))

label_imgMdP = CTkLabel(frame_Donnees,text='',image=img_Cadena)
label_imgMdP.grid(row=4,column=0,sticky='nw',padx=(55,0),pady=(2,0))

label_MdP = CTkLabel(frame_Donnees,text="Mot de Passe : ")
label_MdP.configure(font=CTkFont('Arial',size=23,weight='normal'),text_color=couleur_Texte1)
label_MdP.grid(row=4,column=0,padx=(87,0),sticky='nw',pady=(3,0))

entry_MdP1 = CTkEntry(frame_Donnees,show="*")
entry_MdP1.configure(fg_color=couleur_Fond,border_color=couleur_Texte1,border_width=1)
entry_MdP1.grid(row=5,column=0,padx=(50,0),sticky='nw',ipadx=200,ipady=5,pady=2)

btn_CC = CTkButton(frame_CC2,text="Créer mon compte",command= creer_compte)
btn_CC.grid(row=3,column=0,sticky="nw",padx=(50,0),ipadx=180,ipady=5,pady=(20,10))
btn_CC.configure(fg_color=couleur_Bouton2,hover_color=couleur_Surbrillance,font=CTkFont('Arial',size=20),text_color=couleur_Texte1)

label_Error = CTkLabel(frame_CC2,text="")
label_Error.grid(row=4,column=0,padx=(50,0),sticky='wn')
label_Error.configure(text_color="red")

## BARRE DU HAUT
frameBarreSuperieur = CTkFrame(framePrincipal,fg_color=couleur_Fond2)
frameBarreSuperieur.grid(row=0,column=0,sticky="ew")

frameBarreSuperieur.grid_columnconfigure(0,weight=1)
frameBarreSuperieur.grid_columnconfigure(1,weight=0)
frameBarreSuperieur.grid_columnconfigure(2,weight=1)

frameBarreSuperieur.grid_rowconfigure(0,weight=1)
frameBarreSuperieur.grid_rowconfigure(2,weight=1)

frameBarreSuperieur.configure(corner_radius=0)

frame_BarreRecherche = CTkFrame(frameBarreSuperieur)

img_Profil = CTkImage(light_image=Image.open("image/light/ProfilLight.png"),dark_image=Image.open("image/dark/ProfilDark.png"))
img_Loupe = CTkImage(Image.open("image/icone-loupe-gris.png"))
img_Accueil = CTkImage(light_image=Image.open("image/light/AccueilLight.png"),dark_image=Image.open("image/dark/AccueilDark.png"))

label_Accueil = CTkLabel(frameBarreSuperieur,image=img_Profil,text="",corner_radius=10)
btn_Frame = CTkButton(frameBarreSuperieur,text="",image=img_Accueil,command = lambda: show_frame(frameMenuPrincipal))

entry_barreRecherche = CTkEntry(frame_BarreRecherche,placeholder_text="Rechercher une application")
label_Loupe = CTkLabel(frame_BarreRecherche,image=img_Loupe,text="")

optionMenu_Profil = CTkLabel(frameBarreSuperieur,text=profil)

optionMenu_Profil.configure(fg_color=couleur_Fond2)

btn_Frame.configure(width=45,height=45,fg_color=couleur_Fond2,border_width=0,border_color=couleur_Bord,hover_color=couleur_Surbrillance)
img_Profil.configure(size=(45,45))
label_Accueil.configure(width=60,height=60)
entry_barreRecherche.configure(width=400)

frame_BarreRecherche.configure(fg_color=couleur_Fond2)
frame_BarreRecherche.grid_columnconfigure(0,weight=1)

entry_barreRecherche.configure(font=CTkFont(size=12),corner_radius=25,fg_color=couleur_Fond2,text_color=couleur_Texte1,border_width=2,border_color=couleur_Surbrillance)
label_Loupe.configure(fg_color=couleur_Fond2)

frame_BarreRecherche.grid(row=0,column=1,sticky="ew")
label_Accueil.grid(row=0,column=2,padx=20,pady=5,sticky="e")
btn_Frame.grid(row=0,column=0,padx=20,pady=10,sticky="w")
entry_barreRecherche.grid(row=0,column=0,pady=5,padx=(60,0),sticky="nsew")
label_Loupe.grid(row=0,column=0,padx=20,pady=10,sticky="e")
optionMenu_Profil.grid(row=0,column=2,sticky="e",padx=85)

## RESULTAT RECHERCHE
def recherche(texte) :
    L_application = ["contacts","morpion","snake","notes","messages","wiki","chrono"]
    if texte == "" :
        lBox_Recherche.place_forget()
        lBox_Recherche.configure(height=0)
    else :
        lBox_Recherche.place(x=fenetre.winfo_width()/2-240,y=60)
        lBox_Recherche.lift()
        lBox_Recherche.delete(0, "END")
        listeElement = [item for item in L_application if texte.lower() in item]
        lBox_Recherche.configure(height=len(listeElement)*35 if listeElement else 0)
        if len(listeElement) == 0 :
            lBox_Recherche.place_forget() 
        for item in listeElement :
            lBox_Recherche.insert("END",item.capitalize())

def on_select() :
    selection = lBox_Recherche.get()
    if selection == "Morpion" :
        show_frame(frame_Morpion)
    
    entry_barreRecherche.delete(0,'end')
    lBox_Recherche.place_forget()
    fenetre.focus_force()

lBox_Recherche = CTkListbox(fenetre)
lBox_Recherche._scrollbar.configure(button_color=couleur_Fond2,button_hover_color=couleur_Fond2)
lBox_Recherche.configure(fg_color=couleur_Fond2,corner_radius=0,bg_color="transparent",border_width=2)

lBox_Recherche.configure(text_color=couleur_Texte1,width=400,hover_color=couleur_Surbrillance)

lBox_Recherche.bind("<<ListboxSelect>>",lambda event : on_select())


entry_barreRecherche.bind("<KeyRelease>",lambda event: recherche(entry_barreRecherche.get()))

## MENU PRINCIPAL 

frameMenuPrincipal = CTkFrame(framePrincipal,fg_color=couleur_Fond)
frameMenuPrincipal.grid(row=1,column=0,sticky="nsew")
frameMenuPrincipal.grid_columnconfigure(0,weight=0)
frameMenuPrincipal.grid_columnconfigure(1,weight=5)
frameMenuPrincipal.grid_rowconfigure(0,weight=1)

## MENU LATERAL 

frame_MenuLateral = CTkFrame(frameMenuPrincipal)

frame_MenuLateral.grid_columnconfigure(0,weight=1)
frame_MenuLateral.grid_columnconfigure(1,weight=1)

frame_MenuLateral.grid_rowconfigure(0,weight=0)
frame_MenuLateral.grid_rowconfigure(1,weight=0)
frame_MenuLateral.grid_rowconfigure(2,weight=12)

img_Settings = CTkImage(dark_image=Image.open("image/dark/SettingsDark.png"),light_image=Image.open("image/light/SettingsLight.png"))
img_Help = CTkImage(dark_image=Image.open("image/dark/HelpDark.png"),light_image=Image.open("image/light/HelpLight.png"))
img_Deconnexion = CTkImage(dark_image=Image.open("image/dark/DeconnexionDark.png"),light_image=Image.open("image/light/DeconnexionLight.png"))

btn_Settings = CTkButton(frame_MenuLateral, text="",image = img_Settings,command= lambda: show_frame(frame_Parametres))
btn_Help = CTkButton(frame_MenuLateral, text="",image=img_Help, command = lambda: show_frame(frame_Aide))
btn_Deconnexion = CTkButton(frame_MenuLateral,text="",image=img_Deconnexion,command = lambda : show_frame(frame_Connexion))

frame_MenuLateral.configure(fg_color=couleur_Fond2)

frame_MenuLateral.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
frame_MenuLateral.grid_columnconfigure(0,weight=1)
frame_MenuLateral.configure(corner_radius=5)

btn_Settings.configure(height=45,width=45,corner_radius=3,fg_color=couleur_Fond2,hover_color=couleur_Surbrillance)
btn_Help.configure(height=45,width=45,corner_radius=3,fg_color=couleur_Fond2,hover_color=couleur_Surbrillance)
btn_Deconnexion.configure(height=45,width=45,corner_radius = 3, fg_color=couleur_Fond2,hover_color=couleur_Surbrillance )

btn_Settings.grid(row=1,column=1,padx=(10,10),pady=10)
btn_Help.grid(row=2,column=1,padx=(10,10),sticky="n")
btn_Deconnexion.grid(row=3,column=1,padx=(10,10),sticky="s",pady=10)

## MENU APPLICATIONS

frame_MenuApplications = CTkFrame(frameMenuPrincipal)

frame_MenuApplications.grid(row=0,column=1,sticky="nsew")
frame_MenuApplications.grid_columnconfigure(0,weight=1)
frame_MenuApplications.grid_rowconfigure(1,weight=1)

label_App = CTkLabel(frame_MenuApplications,text="Bibliothéque d'applications")

frame_ScrollApp = CTkScrollableFrame(frame_MenuApplications)
frame_ScrollApp.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

label_App.grid(row=0,column=0,padx=10,pady=5)

chronoImage = CTkImage(Image.open("image/Chrono.png"))
btn_chronoImage = CTkButton(frame_ScrollApp, image=chronoImage, text="Chrono", fg_color= "transparent",hover_color=couleur_Surbrillance)

snakeImage = CTkImage(light_image=Image.open("image/Snake.png"))
btn_snakeImage = CTkButton(frame_ScrollApp, image=snakeImage, text="Snake", fg_color= "transparent",hover_color=couleur_Surbrillance)

notesImage = CTkImage(light_image=Image.open("image/Notes.png"))
btn_notesImage = CTkButton(frame_ScrollApp, image=notesImage, text="Notes", fg_color= "transparent",hover_color=couleur_Surbrillance)

morpionImage = CTkImage(light_image=Image.open("image/Morpion.png"))
btn_morpionImage = CTkButton(frame_ScrollApp, image=morpionImage, text="Morpion", fg_color= "transparent",hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_Morpion))

contactsImage = CTkImage(light_image=Image.open("image/Contacts.png"))
btn_contactsImage = CTkButton(frame_ScrollApp, image=contactsImage, text="Contacts", fg_color= "transparent",hover_color=couleur_Surbrillance)

messagesImage = CTkImage(light_image=Image.open("image/Messages.png"))
btn_messagesImage = CTkButton(frame_ScrollApp, image=messagesImage, text="Messages", fg_color= "transparent",hover_color=couleur_Surbrillance)

wikiImage = CTkImage(light_image=Image.open("image/Wiki.png"))
btn_wikiImage = CTkButton(frame_ScrollApp, image=wikiImage, text="Wiki", fg_color= "transparent",hover_color=couleur_Surbrillance)

L=[btn_chronoImage,btn_contactsImage,btn_messagesImage,btn_morpionImage,btn_notesImage,btn_snakeImage,btn_wikiImage]

chronoImage.configure(size=(90, 90))
btn_chronoImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

snakeImage.configure(size=(90, 90))
btn_snakeImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

notesImage.configure(size=(90, 90))
btn_notesImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

morpionImage.configure(size=(90, 90))
btn_morpionImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

contactsImage.configure(size=(90, 90))
btn_contactsImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

messagesImage.configure(size=(90, 90))
btn_messagesImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

wikiImage.configure(size=(90, 90))
btn_wikiImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

frame_MenuApplications.configure(fg_color=couleur_Fond)

label_App.configure(text_color=couleur_Texte1,font=CTkFont("Arial",size=20))

frame_ScrollApp.configure(fg_color=couleur_Fond,corner_radius=0)


def update_grid(event=None):
    width = frame_ScrollApp.winfo_width()
    cols = max(1, width // 120)

    for i, btn in enumerate(L):
        row = i // cols
        col = i % cols
        btn.grid(row=row, column=col, padx=10, pady=10) 
        
frame_ScrollApp.bind("<Configure>", update_grid)

# FRAME PARAMETRES 

frame_Parametres = CTkFrame(frameMenuPrincipal)

frame_Parametres.grid(row=0,column=1,sticky="nsew")
frame_Parametres.grid_columnconfigure(0,weight=1)
frame_Parametres.grid_rowconfigure(0,weight=0)
frame_Parametres.grid_rowconfigure(1,weight=1)
frame_Parametres.grid_rowconfigure(2,weight=0)
frame_Parametres.grid_rowconfigure(3,weight=1)
frame_Parametres.configure(fg_color=couleur_Fond)


label_gen = CTkLabel(frame_Parametres,text="Général")
label_gen.configure(font=CTkFont("Arial",size=20),padx=30,pady=30)
label_gen.grid(row=0,column=0,sticky="nw")

frame_gen = CTkFrame(frame_Parametres,fg_color=couleur_Fond2)
frame_gen.grid(row=1,column=0,sticky="nsew",padx=(10,20),pady=(0,10))
frame_gen.grid_rowconfigure(0,weight=1)
frame_gen.grid_columnconfigure(0,weight=1)

switch_Theme = CTkSwitch(frame_gen, text ="Sombre/Clair",command=switch_theme)
switch_Theme.configure(text_color="white")
switch_Theme.grid(row=0,column=0,sticky="nsew")



label_profil = CTkLabel(frame_Parametres,text="Profil")
label_profil.configure(font=CTkFont("Arial",size=20),padx=30,pady=30)
label_profil.grid(row=2,column=0,sticky="w")

frame_profil = CTkFrame(frame_Parametres,fg_color=couleur_Fond2)
frame_profil.grid(row=3,column=0,sticky="nsew",padx=(10,20),pady=(0,10))
frame_profil.grid_rowconfigure(0,weight=0)
frame_profil.grid_rowconfigure(1,weight=0)
frame_profil.grid_rowconfigure(2,weight=0)
frame_profil.grid_rowconfigure(3,weight=0)
frame_profil.grid_rowconfigure(4,weight=1)
frame_profil.grid_columnconfigure(0,weight=1)

label_infoProfil = CTkLabel(frame_profil,text="Informations Personnelles")
label_infoProfil.grid(row=0,column=0,sticky="nw",padx=6,pady=3)

def afficher_chtProfil() :
    frame_chtPrenom.place(x=fenetre.winfo_screenwidth()/4,y=fenetre.winfo_screenheight()/5,relwidth=0.4,relheight=0.4)
    
def masquer_chtProfil() :
    frame_chtPrenom.place_forget() 

btn_Prenom = CTkButton(frame_profil,text=f"Prénom",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0,command=afficher_chtProfil)
btn_Prenom.grid(row=1,column=0,padx=20,pady=5,sticky="nw",ipadx=200)  

frame_chtPrenom = CTkFrame(frame_Parametres,fg_color=couleur_Fond,border_width=3,border_color=couleur_Surbrillance)
frame_chtPrenom.grid_rowconfigure(0,weight=1)
frame_chtPrenom.grid_columnconfigure(0,weight=1)

btn_Annuler = CTkButton(frame_chtPrenom,text="Annuler",command=masquer_chtProfil)
btn_Annuler.grid(row=0,column=0,sticky="es",padx=(0,10),pady=(0,10))

label_ImgCht = CTkLabel(frame_chtPrenom,image=img_Profil)
label_ImgCht.grid(row=0,column=0)


label_PrenomFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond)
label_PrenomFleche.grid(row=1,column=0,pady=5,padx=(540,0),sticky='nw')

btn_Mail = CTkButton(frame_profil,text=f"Mail",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0)
btn_Mail.grid(row=2,column=0,padx=20,pady=5,sticky="nw",ipadx=200)

label_MailFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond)
label_MailFleche.grid(row=2,column=0,pady=5,padx=(540,0),sticky='nw')

btn_Mdp = CTkButton(frame_profil,text=f"Mot de Passe",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0)
btn_Mdp.grid(row=3,column=0,padx=20,pady=5,sticky="nw",ipadx=200)

label_MdpFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond)
label_MdpFleche.grid(row=3,column=0,pady=5,padx=(540,0),sticky='nw')

def choix_fichier() :
    chemin = filedialog.askopenfilenames(title="Choisir un fichier",filetypes=[("Images",'*.png *.jpg')])
    
    img_Profil2 = CTkImage(Image.open(chemin[0]))
    img_Profil2.configure(size=(45,45))
    
    label_Accueil.configure(image=img_Profil2)
    

btn_choixImgProfil = CTkButton(frame_profil,text="Image de profil",command=choix_fichier)
btn_choixImgProfil.grid(row=4,column=0)



# FRAME AIDE

frame_Aide = CTkFrame(frameMenuPrincipal)

frame_Aide.grid(row=0,column=1,sticky="nsew")
frame_Aide.grid_columnconfigure(0,weight=1)
frame_Aide.grid_rowconfigure(1,weight=1)

label_1 = CTkLabel(frame_Aide,text="Aide")
label_1.grid(row=0,column=0,sticky="w")

# FRAME APP 1

frame_Morpion = frame_Morpion(framePrincipal)

frame_Morpion.configure(fg_color=couleur_Fond)

frame_Morpion.grid(row=1,column=0,sticky="nsew")
frame_Morpion.grid_columnconfigure(0,weight=1)
frame_Morpion.grid_rowconfigure(0,weight=0)
frame_Morpion.grid_rowconfigure(1,weight=3)
frame_Morpion.grid_rowconfigure(2,weight=9)


show_frame(frame_Connexion)
update_grid()
fenetre.bind("<Configure>",red_fen)
fenetre.mainloop()
 