import tkinter
from tkinter import *
from ArbolBinario import ArbolBinario
from tkinter import messagebox

#Logica del codigo construido por Diego Muñoz y Esteban Cossio
#Finalización del proyecto 4/10/2021 para la materia de Logica y Representación III [2021-1]

class VentanaRecorridos:
    def __init__(self):

        # Se consiguen y se muestran todas las caracteristicas requeridos para el nodo enviado por el usuario
        def informacionNodo():
            # Se obtiene el valor del nodo enviado
            charNodo.set(text_nodo.get())
            # Se hacen todos los procesos para buscar las caracteristicas del nodo enviado por el usuario
            flag = arbol.buscarNodo(arbol.root, charNodo)
            hijos = arbol.buscarHijos(arbol.root, charNodo)#Encuentra los hijos del nodo
            papa = arbol.buscarPapa(arbol.root, charNodo) #Encuentra el papá del nodo
            hermano = arbol.buscarHermano(arbol.root, charNodo) #Encuentra el hermano del nodo
            ancestros = arbol.buscarAncestros(arbol.root, charNodo)[:-1] #Encuentra los ancestros del Nodo
            abuelo = arbol.buscarAbuelo(arbol.root,charNodo) #Encuentra el abuelo del nodo
            tio = arbol.buscarTio(arbol.root, charNodo) #Encuentra el tio del nodo
            posicion = arbol.buscarDerechoIzquierdo(arbol.root, charNodo)#Encuentra si es hijo izquierdo o derecho
            nodoPosicion = 'No es hijo izquierdo ni hijo derecho'
            if posicion == 1:#Si la posicion es 1 es hijo derecho
                nodoPosicion = 'Es hijo derecho'
            if posicion == 0:#Si la posicion es 0 es hijo izquierdo
                nodoPosicion = 'Es hijo izquierdo'

            if flag:#Si el nodo está en el árbol o simplemente existe se arroja una ventana de mensaje con sus caracteristicas
                messagebox._show(title="Información del Nodo " + charNodo.get(),
                                    message= "La información del Nodo " + charNodo.get()+" es: "+
                                             "\n\nNúmero de hijos: "+str(len(hijos))+" | Hijos: "+','.join(hijos)+
                                             "\nPapá: "+','.join(papa)+"\nHermano:  "+','.join(hermano)+"\nTio: "+','.join(tio)+
                                             "\nAncestros: "+','.join(ancestros)+"\nAbuelos: "+','.join(abuelo)+
                                             "\nEs hijo: " + nodoPosicion)
            else:#Si el nodo enviado no está en el árbol
                messagebox.showinfo(title="ERROR", message="No se encontró el nodo")

        # Se contruye el arbol a partir de los recorridos ingresados por el usuario
        def buildTree():
            #Obtiene la cadena de los árboles para crear el árbol binario a partir de los recorridos elegidos por el Usuario
            cadenaInOrder.set(text_Inorden.get())
            cadenaPosOrder.set(text_Postorden.get())
            cadenaPreOrder.set(text_Preorden.get())
            InOrder = cadenaInOrder.get().split(',') #Separa los nombres de los nodos por comas
            flag = False
            flag2 = True
            def validarRecorridos(recorrido1, recorrido2):
                if len(recorrido1) != len(recorrido2):
                    return False
                if len(recorrido1) == 0:
                    return False
                for char in recorrido1:
                    if char not in recorrido2:
                        return False
                return True
            #Para saber con que recorridos estamos trabajando
            if cadenaPreOrder.get() != '' and cadenaInOrder.get() != '':
                PreOrder = cadenaPreOrder.get().split(',')
                if validarRecorridos(InOrder, PreOrder):
                    arbol.ConstruirArbolPre(InOrder, PreOrder, len(InOrder))
                    flag = True
                    iniciarComponentesAR(flag)
                else: flag2 = False
            elif cadenaInOrder.get() != '' and cadenaPosOrder != '':
                PosOrder = cadenaPosOrder.get().split(',')
                if validarRecorridos(InOrder, PosOrder) :
                    arbol.ConstruirArbolPos(InOrder, PosOrder, len(InOrder))
                    iniciarComponentesAR(flag)
                else: flag2 = False
            if not flag2:
                messagebox.showinfo(title="Error Message", message="Ingrese datos correctos")

        # Se inician todas las componentes que conforman la ventana actual
        def iniciarComponentesAR(flag):
            if flag: #Muestra todas las caracteristicas del árbol construido
                result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura(arbol.root))+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            else: #Muestra todas las caracteristicas del árbol construido
                result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura(arbol.root))+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            #Componentes para la información del nodo
            text_nodo.place(x=12, y=615)
            button_nodo = Button(windowRecTree, text="Enviar", font=("Consolas", 10),
                                 bg="#005e35", fg="#ffffff", width="14", height="2",command = informacionNodo)
            button_nodo.place(x=90, y=600)

        #Se actualizan las cajas de texto y botones de los recorridos
        def buildInPre():
            # Método para activar o desactivar las cajas de texto de los recorridos después de presionar el botón In/Pre
            if (text_Postorden != "" or text_Preorden != "" or text_Inorden != ""):
                #Actualiza la caja de texto, borra lo que está escrito
                text_Postorden.delete("0","end")
                text_Inorden.delete("0","end")
                text_Preorden.delete("0", "end")
            text_Postorden.config(state=tkinter.DISABLED)
            text_Inorden.config(state=tkinter.NORMAL)
            text_Preorden.config(state=tkinter.NORMAL)
            button_Send.config(state=tkinter.NORMAL,command=buildTree)

        # Se actualizan las cajas de texto y botones de los recorridos
        def buildInPos():
            #Método para activar o desactivar las cajas de texto de los recorridos después de presionar el botón In/Pos
            if(text_Postorden != "" or text_Preorden != "" or text_Inorden != ""):
                text_Postorden.delete("0", "end")
                text_Inorden.delete("0", "end")
                text_Preorden.delete("0", "end")
            text_Postorden.config(state=tkinter.NORMAL)
            text_Inorden.config(state=tkinter.NORMAL)
            text_Preorden.config(state=tkinter.DISABLED)
            button_Send.config(state=tkinter.NORMAL,command=buildTree)

        #Variables
        arbol = ArbolBinario()
        charNodo = StringVar()
        cadenaInOrder = StringVar()
        cadenaPreOrder  = StringVar()
        cadenaPosOrder = StringVar()
        # Propiedades de la ventana
        windowRecTree = Tk()
        windowRecTree.resizable(False, False) #La ventana no puede cambiar de tamaño
        windowRecTree.geometry("850x650")
        windowRecTree.title("Ingreso de Árbol por recorridos")
        windowRecTree.config(background="#757574")

        # Propiedades del Label
        label_title = Label(windowRecTree, text="Use los botones para elegir los recorridos que quiere ingresar y una vez ingresados los recorridos, click en Crear",
                      font=("Consolas", 9), bg="#005e35", fg="#ffffff", width="117", height="3")
        label_title.place(x=12, y=10)
        label_Inorden = Label(windowRecTree, text="Recorrido Inorden",font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Inorden.place(x=380, y=110)
        label_Preorden = Label(windowRecTree, text="Recorrido Preorden", font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Preorden.place(x=380, y=170)
        label_Postorden = Label(windowRecTree, text="Recorrido Postorden", font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Postorden.place(x=380, y=230)
        result_box = Label(windowRecTree, font=("Consolas", 18),bg="#005e35", fg="#ffffff", width="63", height="7")
        result_box.place(x=12, y=350)

        # Propiedades de la caja de texto
        text_Inorden = Entry(windowRecTree, font=("Consolas", 12) ,textvariable = cadenaInOrder, width="20",state=tkinter.DISABLED,justify=tkinter.CENTER)
        text_Inorden.place(x=350, y=140)
        text_Preorden = Entry(windowRecTree, font=("Consolas", 12), textvariable = cadenaPreOrder, width="20",state=tkinter.DISABLED, justify=tkinter.CENTER)
        text_Preorden.place(x=350, y=200)
        text_Postorden = Entry(windowRecTree, font=("Consolas", 12), textvariable = cadenaPosOrder, width="20",state=tkinter.DISABLED, justify=tkinter.CENTER)
        text_Postorden.place(x=350, y=260)
        text_nodo = Entry(windowRecTree, font=("Consolas", 12), width="8", justify=tkinter.CENTER, textvariable = charNodo)

        # Propiedades de los botones
        button_InPre = Button(windowRecTree, text="In/Pre", command=buildInPre, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_InPre.place(x=290, y=60)
        button_InPost = Button(windowRecTree, text="In/Post", command=buildInPos, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_InPost.place(x=485, y=60)
        button_Send = Button(windowRecTree, text="Crear",command = buildTree ,font=("Consolas", 10),bg="#005e35", fg="#ffffff",
                             width="14", height="2",state=tkinter.DISABLED)
        button_Send.place(x=390, y=300)
        button_end = Button(windowRecTree, text="Cerrar", font=("Consolas", 10), command=windowRecTree.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
        button_end.place(x=730, y=600)

        #Se inicia la ventana con las componentes iniciales
        windowRecTree.mainloop()