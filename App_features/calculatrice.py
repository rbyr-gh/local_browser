import customtkinter as ctk
import tkinter as tk


def calculatrice(parent): 

    # Frame principale
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    # Frame - configuration 

    frame.rowconfigure(5, weight=1)
    frame.columnconfigure(4, weight=1)

    # Boutons pour les chiffres de 1 à 9
    Btn_1 = ctk.CTkButton(frame, text="1", bg_color="black")
    Btn_1.grid(frame, row=0,column=0)



