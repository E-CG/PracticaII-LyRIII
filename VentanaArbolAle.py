import tkinter
from tkinter import messagebox
import string
import random
from ArbolBinario import ArbolBinario
from tkinter import *

#Logica del codigo construido por Diego Muñoz y Esteban Cossio
#Finalización del proyecto 4/10/2021 para la materia de Logica y Representación III [2021-1]

class VentanaArbolAle:
    def __init__(self):

        # Se consiguen y se muestran todas las caracteristicas requeridos para el nodo enviado por el usuario
        def informacionNodo():
            charNodo.set(text_nodo.get())
            flag = arbol.buscarNodo(arbol.root, charNodo)

            hijos = arbol.buscarHijos(arbol.root, charNodo)
            papa = arbol.buscarPapa(arbol.root, charNodo)
            hermano = arbol.buscarHermano(arbol.root, charNodo)
            ancestros = arbol.buscarAncestros(arbol.root, charNodo)[:-1]
            abuelo = arbol.buscarAbuelo(arbol.root,charNodo)
            tio = arbol.buscarTio(arbol.root, charNodo)
            posicion = arbol.buscarDerechoIzquierdo(arbol.root, charNodo)
            nodoPosicion = 'No es izquierdo ni derecho'
            if posicion == 1:
                nodoPosicion = 'derecho'
            if posicion == 0:
                nodoPosicion = 'izquierdo'

            if flag:
                messagebox._show(title="Información del Nodo " + charNodo.get(),
                                 message="La información del Nodo " + charNodo.get() + " es: " +
                                         "\n\nNúmero de hijos: " + str(len(hijos)) + " | Hijos: " + ','.join(hijos) +
                                         "\nPapá: " + ','.join(papa) + "\nHermano:  " + ','.join(hermano) + "\nTio: " + ','.join(tio) +
                                         "\nAncestros: " + ','.join(ancestros) + "\nAbuelos: " + ','.join(abuelo) +
                                         "\nEs hijo: " + nodoPosicion)

            else:
                messagebox.showinfo(title="Manual de Usuario", message="No se encontro el nodo")

        # Se contruye el arbol a partir del número ingresado por el Usuario [MAX: 26 (Abecedario inglés)]
        def buildTree():
            flag = False
            cadenaTamano.set(text_box.get())
            try:
                arbolTamano = int(cadenaTamano.get())
                if arbolTamano > 26:
                    flag = True
            except ValueError:
                flag = True
            if flag:
                return messagebox.showinfo(title="Error message", message="Ingrese datos correctos")
            ListaAbc = [char for char in string.ascii_uppercase]
            cadenaArbol = []
            for _ in range(arbolTamano):
                numeroAleatorio = random.randint(0, len(ListaAbc) - 1)
                cadenaArbol.append(ListaAbc[numeroAleatorio])
                del ListaAbc[numeroAleatorio]
            stringArbol = tkinter.StringVar(None,','.join(cadenaArbol))
            arbol.buildTree(stringArbol)

            iniciarComponentesABA()

        #Se incian todos los componentes que forman la ventana de árbol aleatorio
        def iniciarComponentesABA():
            # Propiedades panel de resultado
            result_box = Label(windowRandomTree, font=("Consolas", 18), bg="#005e35", fg="#ffffff", width="63",
                               height="7")
            result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura(arbol.root))+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            result_box.place(x=12, y=145)
            # Propiedades de la caja de texto nodo

            text_nodo.place(x=14, y=370)
            # Propiedades botón enviar nodo
            button_nodo = Button(windowRandomTree, text="Enviar", font=("Consolas", 10),
                                 bg="#005e35", fg="#ffffff", width="14", height="2", command = informacionNodo)
            button_nodo.place(x=12, y=400)

        #Variables
        charNodo = StringVar()
        cadenaTamano = StringVar()
        arbol = ArbolBinario()
        #Propiedades de la ventana
        windowRandomTree = Tk()
        windowRandomTree.resizable(False,False)
        windowRandomTree.geometry("850x450")
        windowRandomTree.title("Ingreso de Árbol Binario Aleatorio")
        windowRandomTree.config(background="#757574")

        #Propiedades del Label
        label = Label(windowRandomTree, text="Escribe el tamaño del árbol y luego da click al botón 'Crear' [El número máximo es 26]",
                      font=("Consolas", 9), bg="#005e35", fg="#ffffff", width="117", height="3")
        label.place(x=12, y=10)

        # Propiedades de la caja de texto
        text_box = Entry(windowRandomTree, font=("Consolas", 12), width="11",justify=tkinter.CENTER)
        text_box.place(x=392, y=65)
        text_nodo = Entry(windowRandomTree, font=("Consolas", 12), width="11", justify=tkinter.CENTER,
                          textvariable=charNodo)

        #Propiedades de los botones
        button_send = Button(windowRandomTree, text="Crear", command=buildTree, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_send.place(x=390, y=95)
        button_end = Button(windowRandomTree, text="Cerrar", font=("Consolas", 10), command=windowRandomTree.destroy,
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_end.place(x=730, y=400)

        windowRandomTree.mainloop()