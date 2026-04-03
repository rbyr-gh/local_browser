import customtkinter as ctk
import tkinter as tk
from groq import Groq
import os

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

client = Groq(api_key="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")


class frame_Chatbot(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        def demander_ia(message):
            response = client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role": "system", "content": "Tu es un assistant utile."},{"role": "user", "content": message}])
            return response.choices[0].message.content
        
        def envoyer():
            question = textbox_input.get("1.0", "end").strip()
            if question:
                reponse = demander_ia(question)
                textbox_output.delete("1.0", "end")
                textbox_output.insert("1.0", reponse)
        

        textbox_input = ctk.CTkTextbox(self, height=100)
        textbox_input.pack(padx=10, pady=10, fill="x")

        btn_envoyer = ctk.CTkButton(self, text="Envoyer", command=envoyer)
        btn_envoyer.pack(pady=5)

        textbox_output = ctk.CTkTextbox(self, height=300)
        textbox_output.pack(padx=10, pady=10, fill="both", expand=True)

        


