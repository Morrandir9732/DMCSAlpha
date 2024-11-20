from site import ENABLE_USER_SITE

import pylab as p
#Módulos de comunicación con la nube
from google.cloud import storage

#Módulos para las interfaces gráficas
import tkinter
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog

#Módulos adicionales
import os
import datetime as dt
import shutil
from PIL import Image, ImageTk


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

        btn3.config(bg='sky blue')
        btn4.config(bg='green2')

        return

    def folderL():
        lib = 0

        btn3.config(bg='green2')
        btn4.config(bg='sky blue')

        return

    tl = Label(menu, text="Bienvenido a Drone Manuals Cloud Service", font=("Arial 20 bold"))
    tl.place(x=20, y=20)

    txt1 = Label(menu, text="Búsqueda local o en la nube", font=("Arial 10 bold"))
    txt1.place(x=80, y=500)

    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    img1 = Label(menu, image=img, background="black")
    img1.place(x=500, y=100)

    menu.iconphoto(False, img)

    btn1 = Button(menu, text="Buscar", font=("Arial",30), bg="sky blue", command=search)
    btn2 = Button(menu, text="Registrar", font=("Arial", 30), bg="sky blue", command=register)
    btn1.place(x=150, y=120, width=250, height=140)
    btn2.place(x=150, y=320, width=250, height=140)

    btn3 = Button(menu, text="Local", font=("Arial", 15), bg="green2", command=folderL)
    btn4 = Button(menu, text="Nube", font=("Arial", 15), bg="sky blue", command=folderC)
    btn3.place(x=90, y=530, width=80, height=40)
    btn4.place(x=190, y=530, width=80, height=40)

    btn5 = Button(menu, text="Salir", font=("Arial", 15), bg="brown1", command=menu.destroy)
    btn5.place(x=880, y=530, width=80, height=40)

    menu.mainloop()

    # window

    return

def search(): #Muestra la ventana de búsqueda y se encarga de realizar este proceso

    global menu,lib, regw, serw, rn, Ex

    menu.destroy()

    #print(lib)

    # window

    serw = Tk()
    serw.title("DMCSAlpha")
    serw.geometry("1000x850")
    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    serw.iconphoto(False, img)

    def ret():
        serw.destroy()
        mainmenu()

    # window 1

    def look():

        global sproc

        tl = Label(serw, text="Lista de Registros", font=("Arial 20 bold"))
        tl.place(x=20, y=20)

        files = os.listdir('Files')

        emp = False
        if files == []:
            emp = True

        scroll = Scrollbar(serw)
        ls = Listbox(serw, yscrollcommand=scroll.set)

        i = -1
        frns = []
        fcns = []
        ftns = []
        fphs = []
        fmods = []
        ffdates = []
        fldates = []
        nls = []
        ftext1s = []
        ftext2s = []
        pnames = []
        pdescs = []
        pimgs = []

        for file in files:
            i = i + 1

            src = 'Files/'+file+'/Data.txt'
            data = open(src,'r+')
            lines = data.readlines()

            end1 = 0
            end2 = 0
            endpass=False
            count = 0
            for line in lines:
                count += 1
                if count == 1:
                    frn = line.strip()
                elif count == 2:
                    fcn = line.strip()
                elif count == 3:
                    ftn = line.strip()
                elif count == 4:
                    fph = line.strip()
                elif count == 5:
                    ffd = line.strip()
                elif count == 6:
                    ffm = line.strip()
                elif count == 7:
                    ffy = line.strip()
                elif count == 8:
                    fld = line.strip()
                elif count == 9:
                    flm = line.strip()
                elif count == 10:
                    fly = line.strip()
                elif count == 11:
                    fmod = int(line.strip())
                    fmod = getmodel(fmod)

                if line.strip()=='@':
                    if endpass:
                        end2 = count
                    else:
                        end1 = count
                        endpass = True

            count = 0
            ftext1 = ''
            ftext2 = ''
            for line in lines:
                count += 1
                if (count > 11) and (count < end1):
                    ftext1 = ftext1 + line.strip()
                    if end1 - count != 1:
                         ftext1 = ftext1 + '\n'
                elif (count > end1) and (count < end2):
                    ftext2 = ftext2 + line.strip()
                    if end2 - count != 1:
                        ftext2 = ftext2 + '\n'

            data.close()

            nls.append(i+1)
            frns.append(frn)
            fcns.append(fcn)
            ftns.append(ftn)
            fphs.append(fph)
            ffdate = ffd + '/' + ffm + '/' + ffy
            fldate = fld + '/' + flm + '/' + fly
            ffdates.append(ffdate)
            fldates.append(fldate)
            fmods.append(fmod)
            ftext1s.append(ftext1)
            ftext2s.append(ftext2)

            ls.insert(END, (' ' + str(i+1) + ' - ' + fmods[i] + ' - Fecha de llegada: ' + ffdates[i] + ' - Fecha de salida: ' + fldates[i]))

            infiles = os.listdir('Files/' + file)
            infiles.remove('Data.txt')

            nproc = 0
            pname = []
            pdesc = []
            pimg = []

            for object in infiles:
                ext = os.path.splitext(object)
                ext = ext[1]
                if ext == '.txt':
                    nproc = nproc + 1

            for j in range(nproc):
                pimg.append('')

            for object in infiles:
                ext = os.path.splitext(object)
                ext = ext[1]
                if ext == '.txt':
                    proc = open('Files/'+file+'/'+object, 'r+')
                    lines = proc.readlines()
                    end = 0
                    count = 0
                    for line in lines:
                        if line.strip() == '@':
                            end = count
                        count = count + 1
                        if count == 2:
                            pname.append(line.strip())
                    text = ''
                    count = 0
                    for line in lines:
                        count += 1
                        if (count > 2) and (count < end):
                            text = text + line.strip()
                            if end - count != 1:
                                text = text + '\n'
                    pdesc.append(text)

                elif (ext == '.jpg') or (ext == '.png') or (ext == '.jpeg'):
                    nimg = os.path.splitext(object)
                    nimg = int(nimg[0])-1
                    pimg.insert(nimg,object)

            for k in range(len(pimg)):
                if k>(nproc-1):
                    pimg.pop(nproc)

            pnames.append(pname)
            pdescs.append(pdesc)
            pimgs.append(pimg)

        ls.config(height=13, width=70)
        scroll.config(orient=VERTICAL, command=ls.yview)
        ls.place(x=40, y=60)
        scroll.place(x=465, y=60, height=210)

        bck = Button(serw, text="Atrás", font=("Arial", 15), bg="brown1", command=ret)
        bck.place(x=880, y=770, width=80, height=40)

        unit = 0
        sproc = ''
        rn = ''
        cn = ''
        tn = ''
        ph = ''
        ffdate = '--/--/--'
        fldate = '--/--/--'
        fmod = ''
        fdet = ''
        fobs = ''
        pn = ''
        pd = ''

        lx0 = 500

        Label(serw, text='Archivo a observar: ', font='Arial 10 bold').place(x=lx0, y=40)
        unitls = Combobox(serw, width=5)
        unitls['values'] = nls
        if not emp:
            unitls.current(0)
        unitls.place(x=lx0+140, y=40)

        Label(serw, text='Número de registro: ', font='Arial 10 bold').place(x=lx0, y=70)
        Label(serw, text='Nombre del cliente: ', font='Arial 10 bold').place(x=lx0, y=100)
        Label(serw, text='Nombre del técnico: ', font='Arial 10 bold').place(x=lx0, y=130)
        Label(serw, text='Teléfono de contacto: ', font='Arial 10 bold').place(x=lx0, y=160)
        Label(serw, text='Fecha de llegada: ', font='Arial 10 bold').place(x=lx0, y=190)
        Label(serw, text='Fecha de salida: ', font='Arial 10 bold').place(x=lx0, y=220)
        Label(serw, text='Modelo: ', font='Arial 10 bold').place(x=lx0, y=250)
        Label(serw, text='Detalles:', font='Arial 10 bold').place(x=40, y=280)
        Label(serw, text='Observaciones:', font='Arial 10 bold').place(x=lx0, y=280)
        Label(serw, text='Procedimientos/Fallas:', font='Arial 11 bold').place(x=40, y=420)
        Label(serw, text='Elija el procedimiento/falla:', font='Arial 10 bold').place(x=40, y=450)
        Label(serw, text='Procedimiento/falla: ', font='Arial 10 bold').place(x=300, y=450)
        Label(serw, text='Descripción: ', font='Arial 10 bold').place(x=300,y=480)

        procedls = Combobox(serw, width=5)
        procedls['values'] = []
        procedls.place(x=40, y=480)

        rnlb = Label(serw, text=rn, font='Arial 10')
        cnlb = Label(serw, text=cn, font='Arial 10')
        tnlb = Label(serw, text=tn, font='Arial 10')
        phlb = Label(serw, text=ph, font='Arial 10')
        ffdatelb = Label(serw, text=ffdate, font='Arial 10')
        fldatelb = Label(serw, text=fldate, font='Arial 10')
        fmodlb = Label(serw, text=fmod, font='Arial 10')
        fdetlb = Text(serw, height=6, width=40, padx=2, pady=2, wrap=WORD)
        scroll1 = Scrollbar(serw, orient=VERTICAL,command=fdetlb.yview)
        fobslb = Text(serw, height=6, width=40, padx=2, pady=2, wrap=WORD, state=DISABLED)
        scroll2 = Scrollbar(serw, orient=VERTICAL, command=fobslb.yview)
        pnlb = Label(serw, text=pn, font='Arial 10')
        pdlb = Text(serw, height=6, width=40, padx=2, pady=2, wrap=WORD, state=DISABLED)
        scroll3 = Scrollbar(serw, orient=VERTICAL, command=pdlb.yview)

        rnlb.place(x=lx0 + 150, y=70)
        cnlb.place(x=lx0 + 150, y=100)
        tnlb.place(x=lx0 + 150, y=130)
        phlb.place(x=lx0 + 150, y=160)
        ffdatelb.place(x=lx0 + 150, y=190)
        fldatelb.place(x=lx0 + 150, y=220)
        fmodlb.place(x=lx0 + 150, y=250)
        fdetlb.place(x=40, y=310)
        scroll1.place(x=40 + 325, y=310, height=110)
        fobslb.place(x=lx0, y=310)
        scroll2.place(x=lx0 + 325, y=310, height=110)
        pnlb.place(x=450, y=450)
        pdlb.place(x=450, y=480)
        scroll3.place(x=450 + 325, y=480, height=110)

        def showi():
            global unit, rn, sproc
            if sproc=='':
                return
            else:
                pimgn = pimgs[unit-1][sproc-1]
                if pimgn != '':
                    imgsrc = 'Files/' + str(rn) + '/' + pimgn
                else:
                    imgsrc = 'Resources/Icons/noimage.png'
                imgs = Image.open(imgsrc)
                imgrs = imgs.resize((416, 234))
                pimg = ImageTk.PhotoImage(imgrs)
                imglb = Label(image=pimg, background="black")
                imglb.image = pimg
                imglb.place(x=270, y=590)

        def selp():
            global unit, sproc
            sproc = procedls.get()
            if sproc == '':
                return
            else:
                sproc = int(sproc)
                pn = pnames[unit-1][sproc-1]
                pd = pdescs[unit-1][sproc-1]

                pnlb.config(text = pn)
                pdlb.config(state=NORMAL)
                pdlb.delete(1.0, "end-1c")
                pdlb.insert(tk.END, pd)
                pdlb.config(state=DISABLED)

        def sel():
            global unit, rn
            if emp:
                return
            unit = int(unitls.get())
            rn = frns[unit-1]
            cn = fcns[unit-1]
            tn = ftns[unit-1]
            ph = fphs[unit-1]
            ffdate = ffdates[unit-1]
            fldate = fldates[unit-1]
            fmod = fmods[unit-1]
            ftext1 = ftext1s[unit-1]
            ftext2 = ftext2s[unit-1]

            rnlb.config(text = rn)
            cnlb.config(text = cn)
            tnlb.config(text = tn)
            phlb.config(text = ph )
            ffdatelb.config(text = ffdate)
            fldatelb.config(text = fldate)
            fmodlb.config(text = fmod)

            fdetlb.config(state=NORMAL)
            fdetlb.delete(1.0, "end-1c")
            fdetlb.insert(tk.END, ftext1)
            fdetlb.config(state=DISABLED)

            fobslb.config(state=NORMAL)
            fobslb.delete(1.0, "end-1c")
            fobslb.insert(tk.END, ftext2)
            fobslb.config(state=DISABLED)

            np = []
            for i in range(len(pnames[unit-1])):
                np.append(i+1)

            procedls['values'] = np
            procedls.current(0)

            noproced = False
            if np == []:
                noproced = True

        Button(serw, text='Seleccionar', font=("Arial", 10), bg="sky blue", command=sel).place(x=lx0+210, y=35)
        Button(serw, text='Seleccionar', font=("Arial", 10), bg="sky blue", command=selp).place(x=100, y=480)
        Button(serw, text='Ver imagen', font=("Arial", 10), bg="sky blue", command=showi).place(x=300, y=510)

        serw.mainloop()

        return

    look()

    return

def register(): #Muestra la ventana de registro y se encarga de realizar este proceso

    global menu, lib, regw, serw, rn, Ex

    menu.destroy()

    #print(lib)

    # window

    regw = Tk()
    regw.title("DMCSAlpha")
    regw.geometry("1000x600")
    img = tk.PhotoImage(file="Resources/Icons/logo.png")
    regw.iconphoto(False, img)

    def ret():
        regw.destroy()
        mainmenu()

    # window 1

    def getdata():
        global rn,Ex

        nmv = StringVar()
        tnv = StringVar()

        fdayv = IntVar()
        fmonthv = IntVar()
        fyearv = IntVar()

        phv = StringVar()

        ldayv = IntVar()
        lmonthv = IntVar()
        lyearv = IntVar()

        model = IntVar()

        date = dt.datetime.now()

        rn = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second)
        rnt = "N# de registro: " + rn

        tl = Label(regw, text="Registro de Datos", font=("Arial 20 bold"))
        tl.place(x=20, y=20)

        bck = Button(regw, text="Atrás", font=("Arial", 15), bg="brown1", command=ret)
        bck.place(x=880, y=530, width=80, height=40)

        rnlb = Label(regw, text=rnt, font=("Arial 10 bold"))
        molb = Label(regw, text='Modelos:', font=("Arial 10 bold")).place(x=440, y=70)
        nmlb = Label(regw, text="Nombre del cliente", font=("Arial 10 bold"))
        nmin = Entry(regw, textvariable=nmv, font=("Arial", 10))

        tnlb = Label(regw, text="Nombre del técnico", font=("Arial 10 bold"))
        tnin = Entry(regw, textvariable=tnv, font=("Arial", 10))

        lx0 = 40

        rnlb.place(x=440, y=30)
        nmlb.place(x=lx0, y=60)
        nmin.place(x=lx0, y=80, width=300)

        tnlb.place(x=lx0, y=100)
        tnin.place(x=lx0, y=120,width=300)

        phlb = Label(regw, text="Teléfono del cliente", font=("Arial 10 bold"))
        phin = Entry(regw, textvariable=phv, font=("Arial", 10))

        phlb.place(x=lx0 + 220, y=150)
        phin.place(x=lx0 + 220, y=170)

        fdtlb = Label(regw, text="Fecha de entrada (día/mes/año)", font=("Arial 10 bold"))
        Label(regw, text="/", font=("Arial", 10)).place(x=lx0+40, y=170)
        Label(regw, text="/", font=("Arial", 10)).place(x=lx0+90, y=170)

        fdayin = Combobox(regw, width=3, textvariable=fdayv)
        fmonthin = Combobox(regw, width=3, textvariable=fmonthv)
        fyearin = Combobox(regw, width=3, textvariable=fyearv)

        fdayin['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
        fmonthin['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        fyearin['values'] = (24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)

        fdayin.current(0)
        fmonthin.current(0)
        fyearin.current(0)

        fdtlb.place(x=lx0, y=150)
        fdayin.place(x=lx0, y=170)
        fmonthin.place(x=lx0+50, y=170)
        fyearin.place(x=lx0+100, y=170)

        ldtlb = Label(regw, text="Fecha de salida (día/mes/año)", font=("Arial 10 bold"))
        Label(regw, text="/", font=("Arial", 10)).place(x=lx0+40, y=220)
        Label(regw, text="/", font=("Arial", 10)).place(x=lx0+90, y=220)

        ldayin = Combobox(regw, width=3, textvariable=ldayv)
        lmonthin = Combobox(regw, width=3, textvariable=lmonthv)
        lyearin = Combobox(regw, width=3, textvariable=lyearv)

        ldayin['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        lmonthin['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
        lyearin['values'] = (24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)

        ldayin.current(0)
        lmonthin.current(0)
        lyearin.current(0)

        ldtlb.place(x=lx0, y=200)
        ldayin.place(x=lx0, y=220)
        lmonthin.place(x=lx0+50, y=220)
        lyearin.place(x=lx0+100, y=220)

        Label(regw, text="Detalles", font=("Arial 10 bold")).place(x=lx0, y=250)
        detin = Text(regw, height=6, width=40, padx=2, pady=2, wrap=WORD)
        scroll1 = Scrollbar(regw, orient=VERTICAL,command=detin.yview)

        detin.place(x=lx0, y=270)
        scroll1.place(x=lx0+325, y=260, height=110)

        Label(regw, text="Observaciones", font=("Arial 10 bold")).place(x=lx0, y=380)
        obsin = Text(regw, height=6, width=40, padx=2, pady=2, wrap=WORD)
        scroll2 = Scrollbar(regw, orient=VERTICAL, command=obsin.yview)

        obsin.place(x=lx0, y=400)
        scroll2.place(x=lx0 + 325, y=390, height=110)

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

        def partone():
            global rn,Ex

            nm = nmin.get()
            tn = tnin.get()
            ph = phin.get()

            fday = fdayin.get()
            fmonth = fmonthin.get()
            fyear = fyearin.get()

            lday = ldayin.get()
            lmonth = lmonthin.get()
            lyear = lyearin.get()

            det = detin.get(1.0, "end-1c")
            obs = obsin.get(1.0, "end-1c")

            modn = model.get()
            drone = getmodel(modn)

            print("Numero de registro: " + str(rn))
            print("Nombre del cliente: " + str(nm))
            print("Nombre del tecnico: " + str(tn))
            print("Telefono del cliente: " + str(ph))
            print("Fecha de entrada: " + str(fday) + "/" + str(fmonth) + "/" + str(fyear))
            print("Fecha de salida: " + str(lday) + "/" + str(lmonth) + "/" + str(lyear))
            print("Modelo: " + drone)
            print(det)
            print(obs)
            print()

            Ex = False
            for folders in os.listdir('Files'):
                if folders == str(rn):
                    Ex = True
                    msg('El registro ya existe',2)
                    break

            if not Ex:
                os.makedirs('Files/'+str(rn))
                rep = open('Files/'+str(rn)+'/Data.txt','w')
                rep.writelines([str(rn)+'\n',str(nm)+'\n',str(tn)+'\n',str(ph)+'\n',str(fday)+'\n',str(fmonth)+'\n',str(fyear)+'\n',str(lday)+'\n',str(lmonth)+'\n',str(lyear)+'\n',str(model.get())+'\n',det+'\n','@\n',obs+'\n','@\n'])
                rep.close()
                msg('Datos guardados',0)
                getprocedures(1)

        def elim():
            date = dt.datetime.now()
            rn = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second)
            rnt = "N# de registro: " + rn
            rnlb.config(text=rnt)

            tnin.delete(0, 100)

            nmin.delete(0,100)

            detin.delete(1.0,"end-1c")
            obsin.delete(1.0,"end-1c")


        vbtn = Button(regw,text="Registrar datos", font=("Arial", 15), bg="green2", command=partone)
        cbtn = Button(regw, text="Limpiar datos", font=("Arial", 15), bg="sky blue", command=elim)

        vbtn.place(x=200, y=530, width=200, height=40)
        cbtn.place(x=450, y=530, width=200, height=40)

        regw.mainloop()

    # window 1

    # window 2

    def getprocedures(N):
        global regw, rn
        regw.destroy()

        regw = Tk()
        regw.title("DMCSAlpha")
        regw.geometry("400x570")
        img = tk.PhotoImage(file="Resources/Icons/logo.png")
        regw.iconphoto(False, img)

        tl = Label(regw, text="Registro de Procedimientos", font=("Arial 20 bold"))
        tl.place(x=10, y=20)

        pclb = Label(regw, text="Procedimiento/Falla:", font=("Arial 10 bold"))
        pclb.place(x=40, y=60)

        pcv = StringVar()
        pcin = Entry(regw, textvariable=pcv, font="Arial 10 normal")
        pcin.place(x=40, y=80, width=200)

        Label(regw, text="Descripción/Solución", font=("Arial 10 bold")).place(x=40, y=100)
        pdin = Text(regw, height=3, width=40, padx=2, pady=2, wrap=WORD)
        pdin.place(x=40, y=120)
        scroll1 = Scrollbar(regw, orient=VERTICAL, command=pdin.yview)
        scroll1.place(x=370, y=120, height=60)

        def insertimg():
            imgsrc = tk.filedialog.askopenfilename()
            imgn = os.path.basename(imgsrc)
            ext = os.path.splitext(imgn)
            ext = ext[1]
            dest = 'Files/' + str(rn)
            pc = pcin.get()
            imgsrc2 = 'Files/' + str(rn) + '/' + str(N) + ext
            if pc == '':
                msg('Sin Procedimiento/Falla',2)
                return
            else:
                if imgsrc != '':
                    shutil.copy(imgsrc,dest)
                    os.rename(dest+'/'+imgn,imgsrc2)
                    imgs = Image.open(imgsrc2)
                    imgrs = imgs.resize((320,180))
                    pimg = ImageTk.PhotoImage(imgrs)
                    imglb = Label(image=pimg, background="black")
                    imglb.image = pimg
                    imglb.place(x=40,y=230)

        def endregister():
            msg('Registro finalizado', 0)
            ret()

        def savregister():
            pc = pcin.get()
            if pc=='':
                msg('Sin Procedimiento/Falla', 2)
                return
            else:
                pd = pdin.get(1.0, "end-1c")
                proc = open('Files/' + str(rn) + '/' + str(N) + '.txt', 'w')
                proc.writelines([str(rn) + '\n', pc + '\n', pd + '\n', '@'])
                proc.close()
                ch = messagebox.askquestion(title='Atención', message='¿Desea registrar un nuevo procedimiento/falla?')
                if ch == 'yes':
                    getprocedures(N+1)
                else:
                    endregister()

        def canregister():
            dest = 'Files/' + str(rn)
            msg('Registro eliminado', 1)
            shutil.rmtree(dest)
            ret()

        imgbtn = Button(regw, text="Insertar imagen", font=("Arial 10 bold"), bg="sky blue", command=insertimg)
        imgbtn.place(x=125, y=185, width=150, height=40)

        savbtn = Button(regw, text="Guardar", font=("Arial 10 bold"), bg="green2", command=savregister)
        savbtn.place(x=125, y=420, width=150, height=40)

        retbtn = Button(regw, text="Cancelar", font=("Arial 10 bold"), bg="brown1", command=canregister)
        retbtn.place(x=125, y=470, width=150, height=40)

        endbtn = Button(regw, text="Finalizar", font=("Arial 10 bold"), bg="sky blue", command=endregister)
        endbtn.place(x=125, y=520, width=150, height=40)

    getdata()

def msg(txt,n):
    if n==0:
        tk.messagebox.showinfo('Mensaje', txt)
    elif n==1:
        tk.messagebox.showwarning('Atención', txt)
    elif n==2:
        tk.messagebox.showerror('Error', txt)

#Procesos internos

def getmodel(model):
    if (model == 1):
        drone = "Phantom 4"
    elif (model == 2):
        drone = "Phantom 4 Pro"
    elif (model == 3):
        drone = "Phantom 4 Advanced"
    elif (model == 4):
        drone = "Phantom 4 Pro V2"
    elif (model == 5):
        drone = "Phantom 4 RTK"
    elif (model == 6):
        drone = "Spark"
    elif (model == 7):
        drone = "Mavic Pro"
    elif (model == 8):
        drone = "Mavic Air"
    elif (model == 9):
        drone = "Mavic Air 2"
    elif (model == 10):
        drone = "Mavic Air 2S"
    elif (model == 11):
        drone = "Mavic 2 Pro"
    elif (model == 12):
        drone = "Mavic 2 Enterprise"
    elif (model == 13):
        drone = "Mavic 3"
    elif (model == 14):
        drone = "Mavic 3 Cine"
    elif (model == 15):
        drone = "Mavic 3 Pro"
    elif (model == 16):
        drone = "Mavic 3 Classic"
    elif (model == 17):
        drone = "Mini"
    elif (model == 18):
        drone = "Mini SE"
    elif (model == 19):
        drone = "Mini 2"
    elif (model == 20):
        drone = "Mini 3"
    elif (model == 21):
        drone = "Mini 3 Pro"
    elif (model == 22):
        drone = "Mini 4 Pro"
    elif (model == 23):
        drone = "Inspire"
    elif (model == 24):
        drone = "FPV"
    elif (model == 25):
        drone = "Avata"
    elif (model == 26):
        drone = "Avata 2"
    elif (model == 27):
        drone = "Matrice 300 RTK"
    elif (model == 28):
        drone = "Matrice 350 RTK"
    elif (model == 29):
        drone = "Matrice 30"
    elif (model == 30):
        drone = "Agras T20"
    elif (model == 31):
        drone = "Agras T30"
    elif (model == 32):
        drone = "Agras T40"
    elif (model == 33):
        drone = "Agras T50"
    else:
        drone = "NAN"
    return drone

def init(): #Inicializa todos los módulos necesarios para el funcionamiento
    Ex = False
    for folders in os.listdir():
        if folders == 'Files':
            Ex = True
            break
    if not Ex:
        os.mkdir('Files')
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


