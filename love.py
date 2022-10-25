-----------------------------------------------
#Librerias para el funcionamiento del software
-----------------------------------------------

from cProfile import label
import math
import turtle
from turtle import *
import os
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
from matplotlib import image

---------------------------
#Descripción sobre mí
---------------------------

print(os.getcwd())
def popup():
    MessageBox.showinfo("Sobre mí","Soy un desarrollador de software. Si quieres ver más proyectos visita mi Github:\n\nMike538")
    
-----------------------
#Propiedades de imagen
-----------------------

root = Tk()
root.config(bd=15)
root.title("I love you <3")
image = Image.open("astronauta.png")
image = image.resize((200,200), Image.ANTIALIAS)


img = ImageTk.PhotoImage(image)
foto = Label(root, image=img, bd=0 )
foto.grid(row=0, column=0)

------------------------------
#Propiedades de barra de menú
------------------------------

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Información", menu=helpmenu)
helpmenu.add_command(label="Sobre mí",command=popup)
menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="El tiempo es relativo:\n\nun minuto lejos de quien amas te parece una eternidad;\nun minuto junto a la mujer que amas, un segundo.")
instrucciones.grid(row=0, column=1)

---------------------
#Titulo del programa
---------------------

title("I love You <3")

-------------------------------------
#Realiamos la estrcutura del corazón
-------------------------------------

def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
        math.cos(2*t)-2*\
            math.cos(3*t)-\
            math.cos(4*t)

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

for i in range (2550):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor('red')
    t.goto(0, 0)
