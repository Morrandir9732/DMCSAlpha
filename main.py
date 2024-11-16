
#Módulos de comunicación con la nube
import os
from cProfile import label
from doctest import master

from PIL.ImageOps import scale
from google.cloud import storage

#Módulos para las interfaces gráficas
from tkinter import *
import tkinter as tk

#Ventanas
def mainmenu(): #Carga y muestra la ventana principal junto a sus procesos

    global lib
    global menu

    lib = 0

    # window

    menu = Tk()
    menu.title("DMCSAlpha")
    menu.geometry("1000x600")

    tl = Label(menu, text="Bienvenido a Drone Manuals Cloud Service", font=("Arial",20))
    tl.place(x=10, y=20)

    txt1 = Label(menu, text="Búsqueda/Registro local o en la nube", font=("Arial",10))
    txt1.place(x=80, y=500)

    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    img1 = Label(menu, image=img, background="black")
    img1.place(x=500, y=100)

    menu.iconphoto(False, img)

    btn1 = Button(menu, text="Buscar", font=("Arial",30), bg="sky blue")
    btn1.place(x=150, y=120, width=250, height=140)

    btn2 = Button(menu, text="Registrar", font=("Arial", 30), bg="sky blue", command=register)
    btn2.place(x=150, y=320, width=250, height=140)

    btn3 = Button(menu, text="Local", font=("Arial", 15), bg="sky blue", command=folderL)
    btn3.place(x=90, y=530, width=80, height=40)

    btn4 = Button(menu, text="Nube", font=("Arial", 15), bg="sky blue", command=folderC)
    btn4.place(x=190, y=530, width=80, height=40)

    btn5 = Button(menu, text="Salir", font=("Arial", 15), bg="brown1", command=menu.destroy)
    btn5.place(x=880, y=530, width=80, height=40)

    menu.mainloop()

    # window

    return

def search(): #Muestra la ventana de búsqueda y se encarga de realizar este proceso

    return

def register(): #Muestra la ventana de registro y se encarga de realizar este proceso

    global menu, lib

    menu.destroy()

    print(lib)

    # window

    regw = Tk()

    regw.mainloop()

    #window

    return

def showlist(): #Muestra la lista de drones

    return

def message(): #Muestra una ventana de indicaciones o un mensaje

    return


#Procesos internos

def folderC():
    global lib
    lib = 1
    return

def folderL():
    global lib
    lib = 0
    return

def init(): #Inicializa todos los módulos necesarios para el funcionamiento

    return

def upload(): #Sube los datos a la nube

    return

def download(): #Descarga los datos de la nube

    return

state = True

while state:
    init()

    folderL()

    mainmenu()

    state = False


