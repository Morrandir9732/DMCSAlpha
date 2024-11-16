
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

    global lib, menu, btn3, btn4

    lib = 0

    # window

    menu = Tk()
    menu.title("DMCSAlpha")
    menu.geometry("1000x600")

    def folderC():
        lib = 1

        btn3 = Button(menu, text="Local", font=("Arial", 15), bg="sky blue", command=folderL)
        btn4 = Button(menu, text="Nube", font=("Arial", 15), bg="green", command=folderC)
        btn3.place(x=90, y=530, width=80, height=40)
        btn4.place(x=190, y=530, width=80, height=40)

        return

    def folderL():
        lib = 0

        btn3 = Button(menu, text="Local", font=("Arial", 15), bg="green", command=folderL)
        btn4 = Button(menu, text="Nube", font=("Arial", 15), bg="sky blue", command=folderC)
        btn3.place(x=90, y=530, width=80, height=40)
        btn4.place(x=190, y=530, width=80, height=40)

        return

    tl = Label(menu, text="Bienvenido a Drone Manuals Cloud Service", font=("Arial 20 bold"))
    tl.place(x=10, y=20)

    txt1 = Label(menu, text="Búsqueda/Registro local o en la nube", font=("Arial 10 bold"))
    txt1.place(x=80, y=500)

    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    img1 = Label(menu, image=img, background="black")
    img1.place(x=500, y=100)

    menu.iconphoto(False, img)

    btn1 = Button(menu, text="Buscar", font=("Arial",30), bg="sky blue")
    btn2 = Button(menu, text="Registrar", font=("Arial", 30), bg="sky blue", command=register)
    btn1.place(x=150, y=120, width=250, height=140)
    btn2.place(x=150, y=320, width=250, height=140)

    btn3 = Button(menu, text="Local", font=("Arial", 15), bg="green", command=folderL)
    btn4 = Button(menu, text="Nube", font=("Arial", 15), bg="sky blue", command=folderC)
    btn3.place(x=90, y=530, width=80, height=40)
    btn4.place(x=190, y=530, width=80, height=40)

    btn5 = Button(menu, text="Salir", font=("Arial", 15), bg="brown1", command=menu.destroy)
    btn5.place(x=880, y=530, width=80, height=40)

    menu.mainloop()

    # window

    return

def search(): #Muestra la ventana de búsqueda y se encarga de realizar este proceso

    return

def register(): #Muestra la ventana de registro y se encarga de realizar este proceso

    global menu, lib, regw, serw

    menu.destroy()

    print(lib)

    # window

    regw = Tk()
    regw.title("DMCSAlpha")
    regw.geometry("1000x600")
    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    regw.iconphoto(False, img)

    def ret():
        regw.destroy()
        # serw.destroy()
        mainmenu()
        return

    def partone():

        return

    nmv = StringVar()
    detv = StringVar()
    obsv = StringVar()

    fdayv = IntVar()
    fmonthv = IntVar()
    fyearv = IntVar()

    ldayv = IntVar()
    lmonthv = IntVar()
    lyearv = IntVar()

    model = IntVar()

    tl = Label(regw, text="Registro de mantenimiento de unidad", font=("Arial 20 bold"))
    tl.place(x=10, y=20)

    bck = Button(regw, text="Atrás", font=("Arial", 15), bg="brown1", command=ret)
    bck.place(x=880, y=530, width=80, height=40)

    nmlb = Label(regw, text="Nombre del cliente", font=("Arial 10 bold"))
    nmin = Entry(regw, textvariable=nmv, font=("Arial", 10))

    nmlb.place(x=80, y=100)
    nmin.place(x=80, y=120)

    fdtlb = Label(regw, text="Fecha de entrada (día/mes/año)", font=("Arial 10 bold"))
    Label(regw, text="/", font=("Arial", 10)).place(x=110, y=170)
    Label(regw, text="/", font=("Arial", 10)).place(x=150, y=170)
    fdayin = Entry(regw, textvariable=fdayv, font=("Arial", 10), width=3)
    fmonthin = Entry(regw, textvariable=fmonthv, font=("Arial", 10), width=3)
    fyearin = Entry(regw, textvariable=fyearv, font=("Arial", 10), width=5)

    fdtlb.place(x=80, y=150)
    fdayin.place(x=80, y=170)
    fmonthin.place(x=120, y=170)
    fyearin.place(x=160, y=170)

    ldtlb = Label(regw, text="Fecha de salida (día/mes/año)", font=("Arial 10 bold"))
    Label(regw, text="/", font=("Arial", 10)).place(x=110, y=220)
    Label(regw, text="/", font=("Arial", 10)).place(x=150, y=220)
    ldayin = Entry(regw, textvariable=ldayv, font=("Arial", 10), width=3)
    lmonthin = Entry(regw, textvariable=lmonthv, font=("Arial", 10), width=3)
    lyearin = Entry(regw, textvariable=lyearv, font=("Arial", 10), width=5)

    ldtlb.place(x=80, y=200)
    ldayin.place(x=80, y=220)
    lmonthin.place(x=120, y=220)
    lyearin.place(x=160, y=220)

    Label(regw, text="Detalles", font=("Arial 10 bold")).place(x=80, y=250)
    detin = Entry(regw, textvariable=detv, font=("Arial", 10), width=45, justify=LEFT)

    detin.place(x=80, y=270)

    lx1 = 450
    lx2 = 650
    lx3 = 850

    Label(regw, text="Phantom", font=("Arial 10 bold")).place(x=lx1, y=100)
    Radiobutton(regw, text='Phantom 4', variable=model, value=1).place(x=lx1, y=120)
    Radiobutton(regw, text='Phantom 4 Pro', variable=model, value=2).place(x=lx1, y=140)
    Radiobutton(regw, text='Phantom 4 Advanced', variable=model, value=3).place(x=lx1, y=160)
    Radiobutton(regw, text='Phantom 4 Pro V2', variable=model, value=4).place(x=lx1, y=180)
    Radiobutton(regw, text='Phantom 4 RTK', variable=model, value=5).place(x=lx1, y=200)

    Label(regw, text="Spark", font=("Arial 10 bold")).place(x=lx1, y=230)
    Radiobutton(regw, text='Spark', variable=model, value=6).place(x=lx1, y=250)

    Label(regw, text="Mavic", font=("Arial 10 bold")).place(x=lx1, y=280)
    Radiobutton(regw, text='Mavic Pro', variable=model, value=7).place(x=lx1, y=300)
    Radiobutton(regw, text='Mavic Air', variable=model, value=8).place(x=lx1, y=320)
    Radiobutton(regw, text='Mavic Air 2', variable=model, value=9).place(x=lx1, y=340)
    Radiobutton(regw, text='Mavic Air 2s', variable=model, value=10).place(x=lx1, y=360)
    Radiobutton(regw, text='Mavic 2 Pro', variable=model, value=11).place(x=lx1, y=380)
    Radiobutton(regw, text='Mavic 2 Enterprise', variable=model, value=12).place(x=lx1, y=400)
    Radiobutton(regw, text='Mavic 3', variable=model, value=13).place(x=lx1, y=420)
    Radiobutton(regw, text='Mavic 3 Cine', variable=model, value=14).place(x=lx1, y=440)
    Radiobutton(regw, text='Mavic 3 Pro', variable=model, value=15).place(x=lx1, y=460)
    Radiobutton(regw, text='Mavic 3 Classic', variable=model, value=16).place(x=lx1, y=480)

    Label(regw, text="Mavic Mini", font=("Arial 10 bold")).place(x=lx2, y=100)
    Radiobutton(regw, text='Mini', variable=model, value=17).place(x=lx2, y=120)
    Radiobutton(regw, text='Mini SE', variable=model, value=18).place(x=lx2, y=140)
    Radiobutton(regw, text='Mini 2', variable=model, value=19).place(x=lx2, y=160)
    Radiobutton(regw, text='Mini 3', variable=model, value=20).place(x=lx2, y=180)
    Radiobutton(regw, text='Mini 3 Pro', variable=model, value=21).place(x=lx2, y=200)
    Radiobutton(regw, text='Mini 4 Pro', variable=model, value=22).place(x=lx2, y=220)

    Label(regw, text="Inspire", font=("Arial 10 bold")).place(x=lx2, y=250)
    Radiobutton(regw, text='Inspire', variable=model, value=23).place(x=lx2, y=270)

    Label(regw, text="FPV", font=("Arial 10 bold")).place(x=lx2, y=300)
    Radiobutton(regw, text='FPV', variable=model, value=24).place(x=lx2, y=320)
    Radiobutton(regw, text='Avata', variable=model, value=25).place(x=lx2, y=340)
    Radiobutton(regw, text='Avata 2', variable=model, value=26).place(x=lx2, y=360)

    Label(regw, text="Matrice", font=("Arial 10 bold")).place(x=lx2, y=390)
    Radiobutton(regw, text='Matrice 300 RTK', variable=model, value=27).place(x=lx2, y=410)
    Radiobutton(regw, text='Matrice 350 RTK', variable=model, value=28).place(x=lx2, y=430)
    Radiobutton(regw, text='Matrice 30', variable=model, value=29).place(x=lx2, y=450)

    Label(regw, text="Agras", font=("Arial 10 bold")).place(x=lx3, y=100)
    Radiobutton(regw, text='Agras T20', variable=model, value=30).place(x=lx3, y=120)
    Radiobutton(regw, text='Agras T30', variable=model, value=31).place(x=lx3, y=140)
    Radiobutton(regw, text='Agras T40', variable=model, value=32).place(x=lx3, y=160)
    Radiobutton(regw, text='Agras T50', variable=model, value=33).place(x=lx3, y=180)

    regw.mainloop()

    #window

    return

def showlist(): #Muestra la lista de drones

    return

def message(): #Muestra una ventana de indicaciones o un mensaje

    return


#Procesos internos

def init(): #Inicializa todos los módulos necesarios para el funcionamiento

    return

def upload(): #Sube los datos a la nube

    return

def download(): #Descarga los datos de la nube

    return

state = True

while state:
    init()

    mainmenu()

    state = False


