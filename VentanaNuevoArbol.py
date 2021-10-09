import tkinter
from tkinter import *
from tkinter import messagebox
from ArbolBinario import ArbolBinario

#Logica del codigo construido por Diego Muñoz y Esteban Cossio
#Finalización del proyecto 4/10/2021 para la materia de Logica y Representación III [2021-1]

class VentanaArbol:
    def __init__(self):

        #Se consiguen y se muestran todas las caracteristicas requeridos para el nodo enviado por el usuario
        def informacionNodo():
            #Se obtiene el valor del nodo enviado
            charNodo.set(text_nodo.get())
            #Se hacen todos los procesos para buscar las caracteristicas del nodo enviado por el usuario
            flag = arbol.buscarNodo(arbol.root, charNodo)

            hijos = arbol.buscarHijos(arbol.root, charNodo) #Encuentra los hijos del nodo
            papa = arbol.buscarPapa(arbol.root, charNodo) #Encuentra el papá del nodo
            hermano = arbol.buscarHermano(arbol.root, charNodo) #Encuentra el hermanos del Nodo
            ancestros = arbol.buscarAncestros(arbol.root, charNodo)[:-1] #Encuentra los ancestros del nodo
            abuelo = arbol.buscarAbuelo(arbol.root,charNodo) #Encuentra el abuelo del nodo
            tio = arbol.buscarTio(arbol.root, charNodo) #Encuentra el tio del nodo
            posicion = arbol.buscarDerechoIzquierdo(arbol.root, charNodo) #Encuentra si es hijo izquierdo o derecho
            nodoPosicion = 'No es hijo izquierdo ni hijo derecho'
            if posicion == 1: #Si la posicion es 1 es hijo derecho
                nodoPosicion = 'Es hijo derecho'
            if posicion == 0: #Si la posicion es 0 es hijo izquierdo
                nodoPosicion = 'Es hijo izquierdo'

            if flag: #Si el nodo está en el árbol o simplemente existe se arroja una ventana de mensaje con sus caracteristicas
                messagebox._show(title="Información del Nodo " + charNodo.get(),
                                    message= "La información del Nodo " + charNodo.get()+" es: "+
                                             "\n\nNúmero de hijos: "+str(len(hijos))+" | Hijos: "+','.join(hijos)+
                                             "\nPapá: "+','.join(papa)+"\nHermano:  "+','.join(hermano)+"\nTio: "+','.join(tio)+
                                             "\nAncestros: "+','.join(ancestros)+"\nAbuelos: "+','.join(abuelo)+
                                             "\nEs hijo: " + nodoPosicion)
            else: #Si el nodo enviado no está en el árbol
                messagebox.showinfo(title="ERROR", message="No se encontró el nodo")

        #Se contruye el arbol a partir de la cadena separada por comas.
        def addTree():
            #Se construye el árbol binario a partir de la cadena ingresada por el usuario
            cadenaArbol.set(text_box.get())
            numeroNodos = len(cadenaArbol.get().split(','))
            def procesarTexto(cadenaTexto):
                cadena = cadenaArbol.get()
                try :

                    if cadena[0] == ',': return False
                except IndexError:
                    return False
                for i in range(len(cadena)):
                    if cadena[i] == ',':
                        try:
                            if cadena[i + 1] == ',':
                                return False
                        except IndexError:
                            return False
                return True
            if 0 < numeroNodos <= 26 and procesarTexto(cadenaArbol):

                arbol.buildTree(cadenaArbol)
                iniciarComponentesAB()
            else:
                messagebox.showinfo(title="Error Message", message="Ingrese datos correctos")
            #Inicia los componentes de la ventana actual


        #Se inician todas las componentes que conforman la ventana actual
        def iniciarComponentesAB():
            # Propiedades sección de Resultados
            result_box = Label(windowBinaryTree, font=("Consolas", 18), bg="#005e35", fg="#ffffff", width="63",
                               height="7")
            #Se muestran todas las caracteristicas del árbol creado
            result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura(arbol.root))+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            result_box.place(x=13, y=145)
            # Propiedades de la caja de texto para nodo
            text_nodo.place(x=14, y=370)
            # Propiedades botón enviar nodo
            button_nodo = Button(windowBinaryTree, text="Enviar", font=("Consolas", 10),
                                 bg="#005e35", fg="#ffffff", width="14", height="2", command = informacionNodo)
            button_nodo.place(x=12, y=400)

        # Propiedades de la ventana
        windowBinaryTree = Tk()
        cadenaArbol = StringVar()
        charNodo = StringVar()
        arbol = ArbolBinario()
        windowBinaryTree.resizable(False, False) #No se permite el cambio de tamaño de la ventana
        windowBinaryTree.geometry("850x450")
        windowBinaryTree.title("Ingreso de Árbol Binario")
        windowBinaryTree.config(background="#757574")

        # Propiedades del Label
        label = Label(windowBinaryTree, text="Escribe el árbol binario en forma de hilera y separe el nombre de los nodos por comas",
                      font=("Consolas", 10), bg="#005e35", fg="#ffffff", width="117", height="2")
        label.place(x=12, y=10)
        # Propiedades de la caja de texto
        text_box = Entry(windowBinaryTree, font=("Consolas", 12), textvariable=cadenaArbol, width="30", justify=tkinter.CENTER)
        text_box.place(x=300, y=60)
        # Propiedades de los botones
        button_send = Button(windowBinaryTree, text="Crear", command= addTree, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_send.place(x=380, y=95)
        button_end = Button(windowBinaryTree, text="Cerrar", font=("Consolas", 10),command=windowBinaryTree.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
        button_end.place(x=730, y=400)
        text_nodo = Entry(windowBinaryTree, font=("Consolas", 12), width="11", justify=tkinter.CENTER,
                          textvariable=charNodo)

        #Se muestra la ventana con sus componentes inciales
        windowBinaryTree.mainloop()