from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage,filedialog
from PIL import Image
from math import ceil
from csv import *
import time
import os
import re
import webbrowser



from user import app_User
from couleur import *


from applications.app_morpion import frame_Morpion
from applications.app_chrono import frame_Chrono
from applications.app_snake import frame_Snake
from applications.app_notes import frame_Notes
from applications.app_calculatrice import frame_Calculatrice
from applications.app_chatbot import frame_Chatbot
from applications.app_simon import frame_Simon

#-------------- TO DO --------------# 

# Bloc notes - exportation pdf ( à finir)
# Suivi crypto & actions
# Carte interactive
# Jeu trading
# Robot aideur
# Chatbot - Enregistrement des conversations / Différent chatbots & modeles /
# Gestionnaire de tâches (rappels)

# Redimensionnement fenetre (Morpion, Chatbot, Simon, Mastermind)
# Parametres enregistrer
# Snake à améliorer





#-------------- INIT FENETRES --------------# 

global frame_morpion
global frame_chrono
global frame_snake
global frame_mastermind
global frame_notes
global frame_calculatrice
global frame_chatbot

set_appearance_mode("dark")
theme = "dark"

fenetre = CTk()
fenetre.title("ESEOFOX")

sys_exp = os.name

if sys_exp == "nt" :
    fenetre.iconbitmap(r"image/logoApplication/IconBitMap_ESEOFOX.ico")
else :
    icon = PhotoImage(file="image/logoApplication/IconBitMap_ESEOFOX.png")
    fenetre.iconphoto(True,icon)


global ws
global hs

path = ""

utilisateur = []
profil = ""

ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()
fenetre.geometry(f"{ws}x{hs}")
fenetre.minsize(int(ws/2),int(hs/2))
fenetre.maxsize(ws,hs)

fenetre.grid_rowconfigure(0,weight=1)
fenetre.grid_columnconfigure(0,weight=1)





#-------------- FRAME PRINCIPAL --------------# 

framePrincipal = CTkFrame(fenetre,fg_color=couleur_Fond)
framePrincipal.rowconfigure(0,weight=0)
framePrincipal.rowconfigure(1,weight=1)
framePrincipal.columnconfigure(0,weight=1)
framePrincipal.grid(row=0,column=0,sticky="nsew")






#-------------- FONCTIONS --------------# 

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
        frame_Notes.textbox_Page._textbox.configure(insertbackground="black",insertborderwidth=2)
    else:
        set_appearance_mode("dark")
        theme = 'dark'
        frame_Notes.textbox_Page._textbox.configure(insertbackground="black",insertborderwidth=2)
        
def red_fen(event) :
    if lBox_Recherche.winfo_ismapped() :
        lBox_Recherche.place(x=fenetre.winfo_width()/2-300,y=60)
    if frame_chtPrenom.winfo_ismapped() :
        frame_chtPrenom.place(x=fenetre.winfo_width()/4,y=fenetre.winfo_height()/5)
    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()
        
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
                    global path
                    
                    csvfile.close()
                    
                    path = f"user/{mail}"
                    os.makedirs(path,exist_ok=True)
                    os.makedirs(path + "/notes",exist_ok=True)
                    os.makedirs(path + "/conv",exist_ok=True)
                    os.makedirs(path + "/settings",exist_ok=True)
                    csvfile.close()
                    show_frame(frame_Connexion)
                    entry_MdP1.delete(0,"end")
                    entry_Mail1.delete(0,"end")
                    entry_Profil2.delete(0,"end") 
                    
def connexion() :
    global profil
    global utilisateur
    global path
    
    global frame_morpion
    global frame_chrono
    global frame_snake
    global frame_mastermind
    global frame_notes
    global frame_calculatrice
    global frame_chatbot
    global frame_simon
    
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
            
            utilisateur = [prenom,mail,mdp]
            
    
    if check == False :
        label_ErrorC.configure(text="Ce compte n'existe pas")
    else :
        optionMenu_Profil.configure(text=prenom)
        entry_MdP.delete(0,"end")
        entry_Mail.delete(0,"end")
    
        path = f"user/{mail}"
        app_User.path = path
        
        # FRAME APP MORPION

        frame_morpion = frame_Morpion(framePrincipal)

        frame_morpion.configure(fg_color=couleur_Fond)

        frame_morpion.grid(row=1,column=0,sticky="nsew")
        frame_morpion.grid_columnconfigure(0,weight=1)
        frame_morpion.grid_rowconfigure(0,weight=0)
        frame_morpion.grid_rowconfigure(1,weight=3)
        frame_morpion.grid_rowconfigure(2,weight=9)

        # FRAME APP CHRONO

        frame_chrono = frame_Chrono(framePrincipal)
        frame_chrono.grid(row=1,column=0,sticky="nsew")


        # FRAME APP SNAKE

        frame_snake = frame_Snake(framePrincipal)
        frame_snake.grid(row=1,column=0,sticky="nsew")


        # FRAME APP NOTES

        frame_notes = frame_Notes(framePrincipal)
        frame_notes.grid(row=1,column=0,sticky="nsew")
        frame_notes.grid_rowconfigure(0,weight=0)
        frame_notes.grid_rowconfigure(1,weight=1)
        frame_notes.grid_columnconfigure(0,weight=1)

        # FRAME CALCULATRICE

        frame_calculatrice = frame_Calculatrice(framePrincipal)
        frame_calculatrice.grid(row=1,column=0,sticky="nsew")

        # FRAME APP CHATBOT

        frame_chatbot = frame_Chatbot(framePrincipal)
        frame_chatbot.grid(row=1,column=0,sticky="nsew")
        frame_chatbot.grid_rowconfigure(0,weight=1)
        frame_chatbot.grid_columnconfigure(0,weight=0)
        frame_chatbot.grid_columnconfigure(1,weight=1)
        
        # FRAME APP SIMON
        
        frame_simon = frame_Simon(framePrincipal)
        frame_simon.grid(row=1,column=0,sticky="nsew")
        
        show_frame(framePrincipal)
        
    
def deconnexion() :
    show_frame(frame_Connexion)
    
    frame_morpion.destroy()
    frame_chrono.destroy()
    frame_snake.destroy()
    frame_mastermind.destroy()
    frame_notes.destroy()
    frame_calculatrice.destroy()
    frame_chatbot.destroy()
    
    
        
   
 

        
#-------------- FRAME CONNEXION --------------# 

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

entry_Mail.bind("<Return>",lambda event :entry_MdP.focus_force())
entry_MdP.bind("<Return>",lambda event :connexion())





    

#-------------- FRAME CREATION COMPTE --------------# 

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






#-------------- FP - BARRE DU HAUT --------------# 

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

optionMenu_Profil = CTkLabel(frameBarreSuperieur,text=profil,width=200)

optionMenu_Profil.configure(fg_color=couleur_Fond2,anchor="e")

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
entry_barreRecherche.grid(row=0,column=0,pady=5,padx=(100,0),sticky="nsew")
label_Loupe.grid(row=0,column=0,padx=20,pady=10,sticky="e")
optionMenu_Profil.grid(row=0,column=2,sticky="e",padx=85)






#-------------- FP - BARRE DE RECHERCHE --------------#

def recherche(texte) :
    L_application = ["contacts","morpion","snake","notes","messages","wiki","chrono","mastermind","calculatrice","chatbot","simon"]
    if texte == "" :
        lBox_Recherche.place_forget()
        lBox_Recherche.configure(height=0)
    else :
        lBox_Recherche.place(x=fenetre.winfo_width()/2-300,y=60)
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
        show_frame(frame_morpion)
    if selection == "Chrono" :
        show_frame(frame_chrono)
    if selection == "Mastermind" :
        show_frame(frame_mastermind)
    if selection == "Snake" :
        show_frame(frame_snake)
    if selection == "Notes" :
        show_frame(frame_notes)
    if selection == "Wiki" :
        pass
    if selection == "Messages" :
        pass
    if selection == "Contacts" :
        pass
    if selection == "Calculatrice" :
        show_frame(frame_calculatrice)
    if selection == "Chatbot" :
        show_frame(frame_chatbot)
    if selection == "Simon" :
        show_frame(frame_simon)
        
    entry_barreRecherche.delete(0,'end')
    lBox_Recherche.place_forget()
    fenetre.focus_force()

def on_entry() :
    recherche = entry_barreRecherche.get() 
    if len(recherche) > 9 :
        if recherche[0:7] == "search:" :
            if len(recherche) > 10 :
                if recherche[7:10] == 'www' :
                    resultat = recherche[7:].replace(" ","")
                    webbrowser.open(f'{resultat}')
                else :
                    resultat = recherche[7:].replace(" ","+")
                    webbrowser.open(f'www.google.com/search?q={resultat}')
    entry_barreRecherche.delete(0,'end')
        

lBox_Recherche = CTkListbox(fenetre)
lBox_Recherche._scrollbar.configure(button_color=couleur_Fond2,button_hover_color=couleur_Fond2)
lBox_Recherche.configure(fg_color=couleur_Fond2,corner_radius=0,bg_color="transparent",border_width=2)

lBox_Recherche.configure(text_color=couleur_Texte1,width=400,hover_color=couleur_Surbrillance)

lBox_Recherche.bind("<<ListboxSelect>>",lambda event : on_select())
entry_barreRecherche.bind("<Return>",lambda event : on_entry())
entry_barreRecherche.bind("<KeyRelease>",lambda event: recherche(entry_barreRecherche.get()))






#-------------- FP - MENU PRINCIPAL --------------#

frameMenuPrincipal = CTkFrame(framePrincipal,fg_color=couleur_Fond)
frameMenuPrincipal.grid(row=1,column=0,sticky="nsew")
frameMenuPrincipal.grid_columnconfigure(0,weight=0)
frameMenuPrincipal.grid_columnconfigure(1,weight=5)
frameMenuPrincipal.grid_rowconfigure(0,weight=1)






#-------------- FP - MENU LATERAL --------------#

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
btn_Deconnexion = CTkButton(frame_MenuLateral,text="",image=img_Deconnexion,command = lambda : deconnexion())

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






#-------------- FP - MENU APPLICATIONS --------------#

frame_MenuApplications = CTkFrame(frameMenuPrincipal)

frame_MenuApplications.grid(row=0,column=1,sticky="nsew")
frame_MenuApplications.grid_columnconfigure(0,weight=1)
frame_MenuApplications.grid_rowconfigure(1,weight=1)

label_App = CTkLabel(frame_MenuApplications,text="Bibliothèque d'applications")

frame_ScrollApp = CTkScrollableFrame(frame_MenuApplications)
frame_ScrollApp.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

label_App.grid(row=0,column=0,padx=10,pady=5)

chronoImage = CTkImage(Image.open("image/Chrono.png"))
btn_chronoImage = CTkButton(frame_ScrollApp, image=chronoImage, text="Chrono", fg_color= "transparent",hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_chrono))

snakeImage = CTkImage(light_image=Image.open("image/Snake.png"))
btn_snakeImage = CTkButton(frame_ScrollApp, image=snakeImage, text="Snake", fg_color= "transparent",hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_snake))

notesImage = CTkImage(light_image=Image.open("image/Notes.png"))
btn_notesImage = CTkButton(frame_ScrollApp, image=notesImage, text="Notes", fg_color= "transparent",hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_notes))

morpionImage = CTkImage(light_image=Image.open("image/Morpion.png"))
btn_morpionImage = CTkButton(frame_ScrollApp, image=morpionImage, text="Morpion", fg_color= "transparent",hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_morpion))

contactsImage = CTkImage(light_image=Image.open("image/Contacts.png"))
btn_contactsImage = CTkButton(frame_ScrollApp, image=contactsImage, text="Contacts", fg_color= "transparent",hover_color=couleur_Surbrillance)

messagesImage = CTkImage(light_image=Image.open("image/Messages.png"))
btn_messagesImage = CTkButton(frame_ScrollApp, image=messagesImage, text="Messages", fg_color= "transparent",hover_color=couleur_Surbrillance)

wikiImage = CTkImage(light_image=Image.open("image/Wiki.png"))
btn_wikiImage = CTkButton(frame_ScrollApp, image=wikiImage, text="Wiki", fg_color= "transparent",hover_color=couleur_Surbrillance)

calculatriceImage = CTkImage(light_image=Image.open("image/Calculatrice.png"))
btn_calculatriceImage = CTkButton(frame_ScrollApp, image=calculatriceImage, text="Calculatrice", fg_color= "transparent",hover_color=couleur_Surbrillance, command=lambda:show_frame(frame_calculatrice))

chatbotImage = CTkImage(light_image=Image.open("image/ChatBot.png"))
btn_chatbotImage = CTkButton(frame_ScrollApp, image=chatbotImage, text="ChatBot", fg_color= "transparent", hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_chatbot))

simonImage = CTkImage(light_image=Image.open("image/Simon.png"))
btn_simonImage = CTkButton(frame_ScrollApp, image=simonImage, text="Simon", fg_color= "transparent", hover_color=couleur_Surbrillance,command=lambda:show_frame(frame_simon))

L=[btn_chronoImage,btn_morpionImage,btn_snakeImage, btn_calculatriceImage,btn_notesImage,btn_contactsImage,btn_messagesImage,btn_wikiImage,btn_chatbotImage,btn_simonImage]

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

wikiImage.configure(size=(90, 90))
btn_wikiImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

calculatriceImage.configure(size=(90, 90))
btn_calculatriceImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

chatbotImage.configure(size=(90, 90))
btn_chatbotImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)

simonImage.configure(size=(90, 90))
btn_simonImage.configure(height=100,width=100,compound="top",anchor="s",text_color=couleur_Texte1)


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






#-------------- FP - FRAME PARAMETRES --------------# 

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
frame_gen.grid_rowconfigure(0,weight=0)
frame_gen.grid_rowconfigure(1,weight=0)
frame_gen.grid_columnconfigure(0,weight=1)

label_infoProfil = CTkLabel(frame_gen,text="Personalisation")
label_infoProfil.grid(row=0,column=0,sticky="nw",padx=20,pady=3)

switch_Theme = CTkSwitch(frame_gen, text ="Sombre/Clair",command=switch_theme,button_color=couleur_Bouton2,progress_color=couleur_Bouton2,text_color=couleur_Texte1)
switch_Theme.grid(row=1,column=0,sticky="nw",padx=25)

               

label_profil = CTkLabel(frame_Parametres,text="Profil")
label_profil.configure(font=CTkFont("Arial",size=20),padx=30,pady=30)
label_profil.grid(row=2,column=0,sticky="w")

frame_profil = CTkFrame(frame_Parametres,fg_color=couleur_Fond2)
frame_profil.grid(row=3,column=0,sticky="nsew",padx=(10,20),pady=(0,10))
frame_profil.grid_rowconfigure(0,weight=0)
frame_profil.grid_rowconfigure(1,weight=0)
frame_profil.grid_rowconfigure(2,weight=0)
frame_profil.grid_rowconfigure(3,weight=0)
frame_profil.grid_rowconfigure(4,weight=0)
frame_profil.grid_rowconfigure(5,weight=0)
frame_profil.grid_columnconfigure(0,weight=1)

label_infoProfil = CTkLabel(frame_profil,text="Informations Personnelles")
label_infoProfil.grid(row=0,column=0,sticky="nw",padx=20,pady=3)

def modification_profil(modif_entree) :
    nouvel_utilisateur = []
    global utilisateur
    if modif_entree == 1 :
        nouvel_utilisateur = [entry_chtPrenom.get(),utilisateur[1],utilisateur[2]]
        optionMenu_Profil.configure(text=entry_chtPrenom.get())
        masquer_frameCht(frame_chtPrenom)
        pass
    
    elif modif_entree == 2 :
        nouvel_utilisateur = [utilisateur[0],entry_chtMail.get(),utilisateur[2]]
        masquer_frameCht(frame_chtMail)
        pass
    
    elif modif_entree == 3 :
        nouvel_utilisateur = [utilisateur[0],utilisateur[1],entry_chtMdP.get()]
        masquer_frameCht(frame_chtMdP)
        pass
    
    lignes = []
    with open('local/identifiant.csv',mode='r',newline='') as csvfile :
        spamreader = reader(csvfile, delimiter=",")
        for row in spamreader :
            if row == utilisateur :
                row = nouvel_utilisateur
                utilisateur = [nouvel_utilisateur[0],nouvel_utilisateur[1],nouvel_utilisateur[2]]
            lignes.append(row)
    csvfile.close()
    
    with open('local/identifiant.csv',mode='w',newline='') as csvfile :
        ecriture = writer(csvfile)
        for i in lignes :
            ecriture.writerow(i)
    csvfile.close()

def afficher_frameCht(frame) :
    frame.place(x=fenetre.winfo_screenwidth()/4,y=fenetre.winfo_screenheight()/5,relwidth=0.4,relheight=0.4)
    if frame == frame_chtPrenom :
        entry_chtPrenom.insert(0,f"{utilisateur[0]}")
    if frame == frame_chtMail :
        entry_chtMail.insert(0,f"{utilisateur[1]}")
    if frame == frame_chtMdP :
        entry_chtMdP.insert(0,f"{utilisateur[2]}")
    
def masquer_frameCht(frame) :
    frame.place_forget() 
    if frame == frame_chtPrenom :
        entry_chtPrenom.delete(0,"end")
    if frame == frame_chtMail :
        entry_chtMail.delete(0,"end")
    if frame == frame_chtMdP :
        entry_chtMdP.delete(0,'end')
        
        
## FRAME PARAMETRES PRENOM        
      
btn_Prenom = CTkButton(frame_profil,text="Prénom",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0,command= lambda: afficher_frameCht(frame_chtPrenom),text_color=couleur_Texte1)
btn_Prenom.grid(row=1,column=0,padx=20,pady=5,sticky="nw",ipadx=200)  

frame_chtPrenom = CTkFrame(frame_Parametres,fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,corner_radius=0)
frame_chtPrenom.grid_rowconfigure(0,weight=0)
frame_chtPrenom.grid_rowconfigure(1,weight=1)
frame_chtPrenom.grid_rowconfigure(2,weight=1)
frame_chtPrenom.grid_columnconfigure(0,weight=1)

btn_Valider = CTkButton(frame_chtPrenom,text="Valider",command= lambda: modification_profil(1))
btn_Valider.grid(row=2,column=0,sticky='es',padx=(0,10),pady=(0,10))
btn_Valider.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

btn_Annuler = CTkButton(frame_chtPrenom,text="Annuler",command= lambda : masquer_frameCht(frame_chtPrenom))
btn_Annuler.grid(row=2,column=0,sticky="es",padx=(0,160),pady=(0,10))
btn_Annuler.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

label_Prenom = CTkLabel(frame_chtPrenom,text="Prénom",font=("Arial",24,"bold"))
label_Prenom.grid(row=1,column=0,sticky='nw',padx=(60,0),pady=(20,0))

entry_chtPrenom = CTkEntry(frame_chtPrenom,placeholder_text="Prénom")
entry_chtPrenom.grid(row=1,column=0,sticky="nw",padx=(50,0),pady=(70,0),ipadx=100)
entry_chtPrenom.configure(fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,text_color=couleur_Texte1,corner_radius=0)


img_Profil3 = CTkImage(dark_image=Image.open("image/dark/Profil2Dark.png"),light_image=Image.open("image/light/Profil2Light.png"))
img_Profil3.configure(size=(90,90))

label_ImgCht = CTkLabel(frame_chtPrenom,text="",image=img_Profil3)
label_ImgCht.grid(row=0,column=0,sticky="n",pady=(30,0))

label_PrenomFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond,text_color=couleur_Texte1)
label_PrenomFleche.grid(row=1,column=0,pady=5,padx=(540,0),sticky='nw')



## FRAME PARAMETRES MAIL

btn_Mail = CTkButton(frame_profil,text=f"Mail",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0,text_color=couleur_Texte1,command= lambda:afficher_frameCht(frame_chtMail))
btn_Mail.grid(row=2,column=0,padx=20,pady=5,sticky="nw",ipadx=200)

frame_chtMail = CTkFrame(frame_Parametres,fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,corner_radius=0)
frame_chtMail.grid_rowconfigure(0,weight=0)
frame_chtMail.grid_rowconfigure(1,weight=1)
frame_chtMail.grid_rowconfigure(2,weight=1)
frame_chtMail.grid_columnconfigure(0,weight=1)

btn_Valider2 = CTkButton(frame_chtMail,text="Valider",command= lambda: modification_profil(2))
btn_Valider2.grid(row=2,column=0,sticky='es',padx=(0,10),pady=(0,10))
btn_Valider2.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

btn_Annuler2 = CTkButton(frame_chtMail,text="Annuler",command= lambda : masquer_frameCht(frame_chtMail))
btn_Annuler2.grid(row=2,column=0,sticky="es",padx=(0,160),pady=(0,10))
btn_Annuler2.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

label_Mail = CTkLabel(frame_chtMail,text="Mail",font=("Arial",24,"bold"))
label_Mail.grid(row=1,column=0,sticky='nw',padx=(60,0),pady=(20,0))

entry_chtMail = CTkEntry(frame_chtMail,placeholder_text="Mail")
entry_chtMail.grid(row=1,column=0,sticky="nw",padx=(50,0),pady=(70,0),ipadx=100)
entry_chtMail.configure(fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,text_color=couleur_Texte1,corner_radius=0)


img_Mail2 = CTkImage(dark_image=Image.open("image/dark/MailDark.png"),light_image=Image.open("image/light/MailLight.png"))
img_Mail2.configure(size=(90,90))

label_ImgChtMail = CTkLabel(frame_chtMail,text="",image=img_Mail2)
label_ImgChtMail.grid(row=0,column=0,sticky="n",pady=(30,0))

label_MailFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond,text_color=couleur_Texte1)
label_MailFleche.grid(row=2,column=0,pady=5,padx=(540,0),sticky='nw')




## FRAME PARAMATRES MDP

btn_Mdp = CTkButton(frame_profil,text=f"Mot de passe",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0,text_color=couleur_Texte1,command= lambda:afficher_frameCht(frame_chtMdP))
btn_Mdp.grid(row=3,column=0,padx=20,pady=5,sticky="nw",ipadx=200)

frame_chtMdP = CTkFrame(frame_Parametres,fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,corner_radius=0)
frame_chtMdP.grid_rowconfigure(0,weight=0)
frame_chtMdP.grid_rowconfigure(1,weight=1)
frame_chtMdP.grid_rowconfigure(2,weight=1)
frame_chtMdP.grid_columnconfigure(0,weight=1)

btn_Valider3 = CTkButton(frame_chtMdP,text="Valider",command= lambda: modification_profil(3))
btn_Valider3.grid(row=2,column=0,sticky='es',padx=(0,10),pady=(0,10))
btn_Valider3.configure(fg_color=couleur_Bouton2,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0)

btn_Annuler3 = CTkButton(frame_chtMdP,text="Annuler",command= lambda : masquer_frameCht(frame_chtMdP))
btn_Annuler3.grid(row=2,column=0,sticky="es",padx=(0,160),pady=(0,10))
btn_Annuler3.configure(fg_color=couleur_Fond,border_color=couleur_Bord,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=1)

label_MdP = CTkLabel(frame_chtMdP,text="Mot de passe",font=("Arial",24,"bold"))
label_MdP.grid(row=1,column=0,sticky='nw',padx=(60,0),pady=(20,0))

entry_chtMdP = CTkEntry(frame_chtMdP,placeholder_text="Mot de passe")
entry_chtMdP.grid(row=1,column=0,sticky="nw",padx=(50,0),pady=(70,0),ipadx=100)
entry_chtMdP.configure(fg_color=couleur_Fond,border_width=1,border_color=couleur_Bord,text_color=couleur_Texte1,corner_radius=0)


img_MdP2 = CTkImage(dark_image=Image.open("image/dark/CadenaDark.png"),light_image=Image.open("image/light/CadenaLight.png"))
img_MdP2.configure(size=(90,90))

label_ImgChtMdP = CTkLabel(frame_chtMdP,text="",image=img_MdP2)
label_ImgChtMdP.grid(row=0,column=0,sticky="n",pady=(30,0))

label_MdpFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond,text_color=couleur_Texte1)
label_MdpFleche.grid(row=3,column=0,pady=5,padx=(540,0),sticky='nw')

def choix_fichier() :
    chemin = filedialog.askopenfilenames(title="Choisir un fichier",filetypes=[("Images",'*.png *.jpg')])
    
    img_Profil2 = CTkImage(Image.open(chemin[0]))
    img_Profil2.configure(size=(45,45))
    
    label_Accueil.configure(image=img_Profil2)
    
label_personalisation = CTkLabel(frame_profil,text="Personalisation")
label_personalisation.grid(row=4,column=0,sticky="nw",padx=20,pady=(20,0))

btn_choixImgProfil = CTkButton(frame_profil,text="Image de profil",fg_color=couleur_Fond,hover_color=couleur_Fond,anchor="w",border_width=0,text_color=couleur_Texte1,command=choix_fichier)
btn_choixImgProfil.grid(row=5,column=0,sticky='nw',ipadx=200,padx=20,pady=5)

label_ImgProfilFleche = CTkLabel(frame_profil,text=">",fg_color=couleur_Fond,bg_color=couleur_Fond,text_color=couleur_Texte1)
label_ImgProfilFleche.grid(row=5,column=0,pady=5,padx=(540,0),sticky='nw')




#-------------- FP - FRAME AIDE --------------#

frame_Aide = CTkFrame(frameMenuPrincipal)

frame_Aide.grid(row=0,column=1,sticky="nsew")
frame_Aide.grid_columnconfigure(0,weight=1)
frame_Aide.grid_rowconfigure(1,weight=1)

label_1 = CTkLabel(frame_Aide,text="Aide")
label_1.grid(row=0,column=0,sticky="w")



#-------------- INITIALISATION --------------#

show_frame(frame_Connexion)
update_grid()
fenetre.bind("<Configure>",red_fen)
fenetre.mainloop()

 
