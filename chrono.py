from tkinter import *
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Chrono")
fenetre.geometry("300x300")



image = Image.open("imagechrono.png")
photo = ImageTk.PhotoImage(image)
background_label = Label(fenetre, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

cadre = Frame(fenetre, bg='')
btn_chronometre = Button()


# Création des boutons
b1 = Button(fenetre, text="Chronometre", bg = 'grey' , fg = 'white', width = 30, height = 4)
b2 = Button(fenetre, text="Minuteur", bg = 'grey' , fg = 'white', width = 30, height = 4)
b3 = Button(fenetre, text="Jeu 10 secondes", bg = 'grey' , fg = 'white', width = 30, height = 4)


# Position
b1.place(x=565, y=200)
b2.place(x=565, y=300)
b3.place(x=565, y=400)



fenetre.mainloop()