"""
MIT License

Copyright (c) 2021 PinaYT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Importaciones

from tkinter import *
import os
import pygame
from pygame import mixer
from pathlib import Path
import webbrowser

def callback(url):
    webbrowser.open_new(url)

# Iniciar sistema de musica

pygame.init()

# Iniciar programa

ventana = Tk()
scrollbar = Scrollbar(ventana)
c = Canvas(ventana,yscrollcommand=scrollbar.set)
scrollbar.config(command = c.yview)
scrollbar.pack(side=RIGHT,fill=Y)
elframe = Frame(c,width="400")
c.pack(side="left", fill="y", expand=True)
c.create_window(0,0,window = elframe, anchor='nw')


# Sistema de musica

mixer.music.load('.music\\freakyMenu.ogg')
mixer.music.play(10000)
mixer.music.pause()

Button(ventana, text="Reanudar musica", command=lambda: musica(False)).place(x=100)
Button(ventana, text="Pausar musica", command=lambda: musica(True)).place(x=100, y=30)


# Cambiar musica

def musica(pausado):
    if pausado:
        print("Esta pausado")
        mixer.music.pause()
    elif not pausado:
        print("Esta despausado")
        mixer.music.unpause()


# Fondo

fond = PhotoImage(file=".logo\\logo.png")
lblFondo = Label(elframe, image=fond).place(x=350, y=0)
title = Label(elframe, text="Mlauncher, Creado por PinaYT", font="Arial 15", bg="cyan", borderwidth=2, relief="groove").pack()
espacio = Label(elframe, text="",font="Arial 2").pack()
bton = Button(elframe, text="Abrir pagina del proyecto", font="arial 12", bg="cyan", borderwidth=2, relief="groove", command= lambda: callback("https://github.com/PinaYTTT/Mlauncher")).pack()
espacio = Label(elframe, text="",font="Arial 2").pack()
bton2 = Button(elframe, text="Como instalar mods?", font="arial 12", bg="cyan", borderwidth=2, relief="groove", command= lambda: ayuda()).pack()
espacio = Label(elframe, text="",font="Arial 2").pack()                  

# Carga de mods

mods = os.listdir(".mods")


for i in mods:
    boton = Button(elframe, text=f"{i}", font="Helvetica 15",
                   command=lambda i=i: startMod(i)).pack()
    espacio = Label(elframe, text="", font="Arial 1").pack()


def startMod(i):
    __dirname = os.path.dirname(__file__)
    print(f".mods\\{i}")
    os.system(f'cd .mods\\{i} && start Game.exe')

def ayuda():
    window = Tk()

    label1 = Label(window, text="Como instalar mods?", font="Helvetica 15").pack()
    label2 = Label(window, text="Primero, presiona en la parte de abajo de este texto: 'Abrir carpeta de mods'. \nLuego busca la carpeta del mod que quieres instalar y entra,\n Renombra el archivo .exe del juego a Game.exe,\n Esto es muy importante, si no haces esto el mod no funcionara. \nLuego mueve la carpeta del mod a la carpeta de mods. \nMas informacion en mi tiktok @PinaYT").pack()
    espacio2 = Label(window, text="", font="Helvetica 2").pack()
    botond = Button(window, text="Abrir carpeta de mods", font="Arial 12", command=lambda:os.system("start .mods")).pack()
    window.geometry("500x200")
    window.title("Ayuda de instalacion de mods - MLauncher")
    window.iconbitmap('.ico\\icon.ico')
    window.resizable(False,False)
    window.mainloop()
# Arranque

ventana.update()
c.config(scrollregion=c.bbox("all"))
ventana.title("MLauncher - PinaYT")
ventana.resizable(False, False)
ventana.iconbitmap('.ico\\icon.ico')
ventana.geometry("1500x720")
ventana.mainloop()
