from tkinter import *
import tkinter as tk
from tkinter import messagebox
from VentanaNuevoArbol import VentanaArbol
from VentanaArbolAle import VentanaArbolAle
from VentanaArbolRecorridos import VentanaRecorridos

#Logica del codigo construido por Diego Muñoz y Esteban Cossio
#Finalización del proyecto 4/10/2021 para la materia de Logica y Representación III [2021-1]

#Función para generar mensaje de información
def openInfoUser():
    messagebox.showinfo(title="Información proyecto", message="|Programa para la construir de árbol binario|"+
                                                              "\n\n•Porfavor siga las instrucciones que se enseñan en el manual de usuario"+
                                                              "\n•Finalización de la práctica 4/10/2021"+
                                                              "\n•Se pueden crear árboles binario por cadena o ingresando el tamaño"+
                                                              "\n•Utilice el teclado y el mouse para navegar por el programa")

#Propiedades de la ventana Principal
window = Tk()
window.resizable(False,False) #La ventana no puede cambiar de tamaño
window.geometry("520x340")
window.title("Práctica #2 - LyR III")
window.config(background = "#757574")

#Label que se muestra en mitad de la ventana
back_Title = tk.Label(text="Segunda práctica de Lógica y Representanción III\n\n Hecho por: Diego Muñoz y Esteban Cossio",
                      font=("Consolas",14), bg="#005e35", fg="#ffffff", width="52",height="8")
back_Title.place(x = 0, y = 80)

#Botón de cerrar la ventana actual
button_end = Button(window, text="Cerrar", font=("Consolas", 10),command=window.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
button_end.place(x=400, y=290)

#Creando la barra de Menú
barMenu = Menu(window)
mnuTree = Menu(barMenu)
mnuInformation = Menu(barMenu)
#Añadiendo los botones para Árboles Binarios en la barra de Menú
mnuTree.add_command(label="Nuevo Árbol", command=VentanaArbol)
mnuTree.add_command(label="Árbol aleatorio", command=VentanaArbolAle)
mnuTree.add_command(label="Árbol a partir de recorridos", command=VentanaRecorridos)
#Añadiendo los botones para Información del Programa
mnuInformation.add_command(label="Info. programa", command=openInfoUser)
#La barra de menú es tipo cascada
barMenu.add_cascade(label="Árboles",menu=mnuTree)
barMenu.add_cascade(label="Información",menu=mnuInformation)
window.config(menu=barMenu)

window.mainloop()