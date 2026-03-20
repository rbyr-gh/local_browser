from customtkinter import *
from CTkListbox import CTkListbox
from tkinter import PhotoImage
from os import *
from PIL import Image


class frame_NomApp(CTkFrame):
    def __init__(self, parent) :
        super().__init__(parent)
        
        ## TOUT LES WIDGETS 
        
        label = CTkLabel(self,text="test")
        label.grid(row=0,column=0,sticky="nw")
        