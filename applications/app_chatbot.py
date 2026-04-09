from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage,filedialog
from PIL import Image
import time
import os
from math import ceil
from csv import *
import re
import webbrowser
import threading
from user import app_User
import json

from openai import OpenAI
import openai
from google import genai
from groq import Groq
from anthropic import Anthropic

# Supprimer conversion
# Changer de modele

black = "gray90"
white = "gray15"

couleur_Fond2 = ("grey95","grey23")
couleur_Fond = (black,"grey15")
couleur_Widget = ("grey74","grey43")
couleur_Bouton1 = (black,"grey3")
couleur_Bouton2 = ("DarkOrange1","DarkOrange3")
couleur_Bouton3 = ("cornsilk4","DarkGray")
couleur_Surbrillance =("grey74","grey43")
couleur_Bord = (white,black)
couleur_Texte1 = (white,black)
couleur_Texte2 = ("grey26","grey80")


class frame_Chatbot(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        
        # INITIALISATION 
        
        self.api_ChatGPT = "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"
        self.api_Gemini = "AIzaSyDa_a7SVRuahMgnnl9-WdaZ9xO8NpHzA1g"
        self.api_Claude = ""
        self.api_Groq = "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"
        
        self.path = app_User.path
        self.liste_conversation = os.listdir(self.path + f"/conv")
        
        self.liste_conversation_sansJson = [i[:-5] for i in self.liste_conversation]
        
        self.client_ChatGPT = OpenAI(api_key=self.api_ChatGPT)
        self.client_Gemini = genai.Client(api_key=self.api_Gemini)
        self.client_Groq = Groq(api_key=self.api_Groq)
        
        self.modeles_ChatGPT_full = self.client_ChatGPT.models.list()
        self.modeles_ChatGPT_nom = []
        
        for full in self.modeles_ChatGPT_full :
            self.modeles_ChatGPT_nom.append(full.id)
            
        
        
        self.conversation = []
        self.nbMsgConv = 0
        
        
        
        # FRAME LATERAL 
        img_Plus = CTkImage(light_image=Image.open("image/light/PlusLight.png"),dark_image=Image.open("image/dark/PlusDark.png"))
        img_Plus.configure(size=(25,25)) 
        
        self.frame_Lateral = CTkFrame(self,fg_color=couleur_Fond)
        self.frame_Lateral.grid(row=0,column=0,sticky="nsew")
        self.frame_Lateral.grid_columnconfigure(0,weight=1)
        self.frame_Lateral.grid_rowconfigure(0,weight=0)
        self.frame_Lateral.grid_rowconfigure(1,weight=0)
        self.frame_Lateral.grid_rowconfigure(2,weight=1)
        
        self.button_nouveauChat = CTkButton(self.frame_Lateral,text="Nouveau chat",image=img_Plus,command = lambda : self.nouveau_chat())
        self.button_nouveauChat.grid(row=0,column=0,sticky="ew",padx=5,pady=5,ipadx=50,ipady=10)
        self.button_nouveauChat.configure(fg_color=couleur_Fond,hover_color=couleur_Fond2,anchor="w",font=CTkFont("Arial",16,"normal"),text_color=couleur_Texte1,compound="w")
        
        self.label_vosChats = CTkLabel(self.frame_Lateral,text="Vos chats")
        self.label_vosChats.grid(row=1,column=0,sticky="nw",padx=10,pady=(10,0))
        
        self.listbox_conversation = CTkListbox(self.frame_Lateral)
        self.listbox_conversation.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")
        self.listbox_conversation.configure(fg_color=couleur_Fond,text_color=couleur_Texte1,hover_color=couleur_Surbrillance,border_width=0,highlight_color=couleur_Bouton2)
        
        for item in self.liste_conversation_sansJson :
            self.listbox_conversation.insert("END",item)
            
        self.listbox_conversation.update_idletasks()
        self.listbox_conversation._parent_canvas.yview_moveto(1.0)    
        
        self.listbox_conversation.bind("<<ListboxSelect>>",lambda event : self.ouvrir())        
        
        
        
        
        
        # FRAME CONVERSATION 
        
        self.frame_Conversation = CTkFrame(self,fg_color=couleur_Fond2,corner_radius=0)
        self.frame_Conversation.grid(row=0,column=1,sticky="nsew")
        self.frame_Conversation.grid_columnconfigure(0,weight=1)
        
        self.frame_Conversation.grid_rowconfigure(0,weight=0)
        self.frame_Conversation.grid_rowconfigure(1,weight=8)
        self.frame_Conversation.grid_rowconfigure(2,weight=0)
        
        self.entry_Message = CTkTextbox(self.frame_Conversation)
        self.entry_Message.grid(row=2,column=0,ipadx=400,ipady=10,sticky="ew",padx=300,pady=(0,40))
        self.entry_Message.configure(border_width=0,height=10,corner_radius=20,fg_color=couleur_Fond)
        
        self.option_Modele = CTkOptionMenu(self.frame_Conversation,values=["ChatGPT","Gemini","Claude","Groq"])
        self.option_Modele.grid(row=0,column=0,sticky='nw',padx=10,pady=10)
        self.option_Modele.configure(fg_color=couleur_Fond2,button_color=couleur_Fond2,button_hover_color=couleur_Fond2,font=CTkFont("Arial",18,"bold"),text_color=couleur_Texte1)
        
        self.option_Variante = CTkOptionMenu(self.frame_Conversation)
        self.option_Variante.grid(row=0,column=0,sticky='nw',padx=170,pady=10)
        self.option_Variante.configure(fg_color=couleur_Fond2,button_color=couleur_Fond2,button_hover_color=couleur_Fond2,font=CTkFont("Arial",12,"bold"),text_color=couleur_Texte1)
        
        self.button_Envoyer = CTkButton(self.frame_Conversation,text="▲",command=lambda:self.envoyer_texte())
        self.button_Envoyer.grid(row=2,column=0,sticky="e",padx=(0,330),pady=(0,40))
        self.button_Envoyer.configure(height=40,width=40,corner_radius=10,fg_color=couleur_Texte1,text_color=couleur_Bouton1,bg_color=couleur_Fond,hover_color=couleur_Surbrillance)
        
        self.frame_Conversation = CTkScrollableFrame(self.frame_Conversation)
        self.frame_Conversation.grid(row=1,column=0,sticky="nsew")
        self.frame_Conversation.configure(fg_color=couleur_Fond2)
        self.frame_Conversation.grid_columnconfigure(0,weight=1)
        
        self.entry_Message.bind("<Return>",lambda event :self.envoyer_texte())
        

        
    def envoyer_texte(self):
        self.anim_index = 0
        self.anim_running = False
        self.points = ['.','..','...']
        
        self.message = self.entry_Message.get("1.0","end")
        
        nouveau_message_user = {"role" : "user", "content" : self.message}
        self.conversation.append(nouveau_message_user)
        
        if len(self.conversation) == 1 :
            self.titre_Conv = self.groq_titre(f"Donne un titre court (5-8 mots) pour cette conversation basée sur le premier message :'{self.message}' Seul le titre, pas de texte supplémentaire. Attention ! : Il doit être différents d'au moins un caractere de ceux qu'il y a dans cette liste : {self.liste_conversation_sansJson}")
            self.listbox_conversation.insert("end",self.titre_Conv)
        
        self.entry_Message.delete("1.0","end")
        self.entry_Message.mark_set("insert","1.0")
        
        self.nbMsgConv += 1
        
        label_Message = CTkLabel(self.frame_Conversation,text=self.message)
        self.frame_Conversation.grid_rowconfigure(self.nbMsgConv,weight=0)
        label_Message.grid(row=self.nbMsgConv,column=0,sticky="ne",padx=(0,100),ipadx=10,ipady=5,pady=5)
        label_Message.configure(wraplength=600,fg_color=couleur_Fond,justify="left",anchor="s",corner_radius=10)
        
        # -------- RÉPONSE BOT --------
        
        self.button_Envoyer.configure(state="disabled")
        
        self.nbMsgConv += 1
        
        self.bot = self.option_Modele.get()
        
        
        self.label_Reponse = CTkLabel(self.frame_Conversation,text='')
        self.frame_Conversation.grid_rowconfigure(self.nbMsgConv,weight=0)
        self.label_Reponse.grid(row=self.nbMsgConv,column=0,sticky="nw",padx=(0,100),ipadx=10,ipady=5,pady=5)
        self.label_Reponse.configure(wraplength=1200,fg_color=couleur_Fond2,justify='left')
        
        self.anim_running = True
        self.animation_chargement()
                
        if self.bot == "Groq" :
            thread = threading.Thread(target=self.groq_thread,daemon=True)
            thread.start()
        elif self.bot == "ChatGPT" :
            pass
        elif self.bot == "Gemini" :
            pass
        else :
            pass
        
        # -------- FIN BOT --------
        
        self.button_Envoyer.configure(state="normal")
        self.entry_Message.mark_set("insert","1.0")
        
        self.frame_Conversation.update_idletasks()
        self.frame_Conversation._parent_canvas.yview_moveto(1.0)
        
        
        return "break"
        
    # -------- CHATGPT --------    
        
    def chat_gpt(self,message,modele) :
        response_ChatGPT = client.response.create(model=modele,instructions="",input=message)
        return response_ChatGPT.output_text
    
    # -------- GEMINI --------
    
    def gemini(self,message,modele) :
        response_Gemini = client.models.generate_content(model=modele,contents=message)
        return response_Gemini.text
    
    # -------- CLAUDE --------
    
    def claude(self,message,modele) :
        pass
    
    # -------- GROQ --------
    
    def groq_titre(self,message) :
        response_Groq = self.client_Groq.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role" : "user","content" : message}])
        self.anim_running = False
        return re.sub(r'[\*\#]','',response_Groq.choices[0].message.content)
    
    def groq(self) :
        response_Groq = self.client_Groq.chat.completions.create(model="llama-3.3-70b-versatile",messages=self.conversation)
        self.anim_running = False
        return re.sub(r'[\*\#]','',response_Groq.choices[0].message.content)
    
    def groq_thread(self) :
        response = self.groq()
        self.anim_running = False
        nouveau_message_assistant = {"role" : "assistant","content" : response}    
        self.conversation.append(nouveau_message_assistant)    
        self.label_Reponse.configure(text=response)
        
        self.frame_Conversation.update_idletasks()
        self.frame_Conversation._parent_canvas.yview_moveto(1.0)
        self.enregistrer()
        
    # -------- ANIMATION CHARGEMENT --------  
        
    def animation_chargement(self) :
        if self.anim_running :
            self.points = ['.','..','...']
            self.label_Reponse.configure(text=f"Chargement{self.points[self.anim_index % 3]}")
            self.anim_index += 1
            self.after(500,self.animation_chargement)
    
    # -------- ENREGISTRER CONV --------
    
    def enregistrer(self) :
        with open(app_User.path + f"/conv/{self.titre_Conv}.json","w") as f :
            json.dump(self.conversation,f,indent=4,ensure_ascii=False)
            
    # -------- OUVRIR CONV --------        
            
    def ouvrir(self) :
        self.nbMsgConv = 0
        self.conversation = []
        for widget in self.frame_Conversation.winfo_children() :
            widget.destroy() 
        
        selection = self.listbox_conversation.get()
        
        with open(self.path + f"/conv/{selection}.json","r") as f :
            self.conversation = json.load(f)    
        
        self.titre_Conv = selection
            
        for i in range(len(self.conversation)) :
            self.nbMsgConv += 1
            if i % 2 == 0 :
                label_Message = CTkLabel(self.frame_Conversation,text=self.conversation[i]["content"])
                self.frame_Conversation.grid_rowconfigure(self.nbMsgConv,weight=0)
                label_Message.grid(row=self.nbMsgConv,column=0,sticky="ne",padx=(0,100),ipadx=10,ipady=5,pady=5)
                label_Message.configure(wraplength=600,fg_color=couleur_Fond,justify="left",anchor="s",corner_radius=10)
            else :
                self.label_Reponse = CTkLabel(self.frame_Conversation,text=self.conversation[i]["content"])
                self.frame_Conversation.grid_rowconfigure(self.nbMsgConv,weight=0)
                self.label_Reponse.grid(row=self.nbMsgConv,column=0,sticky="nw",padx=(0,100),ipadx=10,ipady=5,pady=5)
                self.label_Reponse.configure(wraplength=1200,fg_color=couleur_Fond2,justify='left')
     
    # -------- NOUVEAU CHAT --------
                
    def nouveau_chat(self) :
        self.nbMsgConv = 0
        self.conversation = []
        for i in range(self.listbox_conversation.size()) :
            self.listbox_conversation.deselect(i)
        for widget in self.frame_Conversation.winfo_children() :
            widget.destroy()
        self.listbox_conversation.update_idletasks()
        self.listbox_conversation._parent_canvas.yview_moveto(1.0)    
            
    
        
                
            
        
        


