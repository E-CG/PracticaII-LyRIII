from Nodo import Nodo
import random
from tkinter import *

#Logica del codigo construido por Diego Muñoz y Esteban Cossio
#Finalización del proyecto 4/10/2021 para la materia de Logica y Representación III [2021-1]
class ArbolBinario:

    #Funciones privadas
    def __init__(self, dato = None):
        self.root = Nodo(dato)

    #Contruye el árbol
    def buildTree(self, cadenaTexto):
        #Variables
        aleatorio = random
        vectorCaracteres = cadenaTexto.get().split(',') #Crea un vector con los nombres de los nodos

        vectorNodos = [] #Crea un vector de Nodos

        #Creación vector de nodos
        for char in vectorCaracteres:
            vectorNodos.append(Nodo(char))#Agrega al vectorNodos los nodos

        #El tamaño del árbol
        arbol = [None]*(2**(len(vectorNodos))-1)
        espaciosDisponibles = [0] #Vector de espacios disponibles para ubicar los nodos aleatoriamente

        #Creación de los espacios disponibles para la ubicación de los nodos
        for nodo in vectorNodos:
            #Se genera un número dentro del rango del árbol
            numero = aleatorio.randint(0, len(espaciosDisponibles) - 1)
            #Se ubica en nodo en la poscion generada
            arbol[espaciosDisponibles[numero]] = nodo
            # Se agregan dos opciones para el nodo ubicado
            espaciosDisponibles.append(espaciosDisponibles[numero]*2 + 1)
            espaciosDisponibles.append(espaciosDisponibles[numero] * 2 + 2)
            #Se borra la pocisión ocupada
            del espaciosDisponibles[numero]

        #Posicionando los Nodos en el árbol con base en los espacios que salieron anteriormente
        for i in range(len(arbol)):
            #Si el arbol no es Nulo
            if arbol[i] is not None and (i*2+2) < len(arbol):
                #Se le asignan los hijos izquierdos o derechos al nodo
                arbol[i].left = arbol[i*2 + 1]
                arbol[i].right = arbol[i*2 + 2]
        #Se asigna la raíz al árbol
        self.root = arbol[0]

    #Imprime el recorrido PreOrder del árbol
    def PreOrder(self, root):
        result = []
        if root is not None:
            result.append(str(root))
            result += self.PreOrder(root.left)
            result += self.PreOrder(root.right)
        return result

    #Imprime el recorrido InOrder del árbol
    def InOrder(self,root):
        result = []
        if root is not None:
            result += self.PreOrder(root.left)
            result.append(str(root))
            result += self.PreOrder(root.right)
        return result

    #Imprime el recorrido PosOrder del árbol
    def PosOrder(self, root):
        result = []
        if root is not None:
            result += self.PosOrder(root.left)
            result += self.PosOrder(root.right)
            result.append(str(root))
        return result

    #Se utiliza para la creación del árbol binario a partir de recorridos Inorder y Posorder
    def auxiliarPos(self,In, post, inStrt, inEnd, pIndex):
        #Caso base
        if (inStrt > inEnd): #Si el comienzo es mayor al final del recorrido inorder
            return None

        #Se obtiene el nodo
        node = Nodo(post[pIndex[0]])
        pIndex[0] -= 1

        #Si llego a la posición final del recorrido inorder
        if (inStrt == inEnd):
            return node

        #Busca si está la raíz en los dos recorridos Inorden y Posorder
        iIndex = self.search(In, inStrt, inEnd, node.dato)

        #Recursividad para construir el arbol
        node.right = self.auxiliarPos(In, post, iIndex + 1,
                            inEnd, pIndex)
        node.left = self.auxiliarPos(In, post, inStrt,
                          iIndex - 1, pIndex)
        return node

    #Construye arbol binario dados los arreglos inorden y postorden
    def ConstruirArbolPos(self,In, post, n):
        pIndex = [n - 1] #Posicion de la raíz en un recorrido Posorder (Ultima)
        #Invoca el método de construir arbol con recorrido Inorder y Posorder
        self.root = self.auxiliarPos(In, post, 0, n - 1, pIndex)

    #Busqueda de la raiz en el recorrido inorder o posorder
    def search(self,arr, strt, end, value):
        i = 0
        for i in range(strt, end + 1):
            if (arr[i] == value):
                break
        return i

    #Se utiliza para la creación del árbol binario a partir de recorridos Inorder y Preorder
    def auxiliarPre(self, In, pre, inStrt, inEnd, pIndex):
            # Caso base
            if (inStrt > inEnd): #Si el comienzo es mayor al final del recorrido inorder
                return None

            # Se obtiene el nodo
            node = Nodo(pre[pIndex[0]])
            pIndex[0] += 1

            # Si llego a la posición final del recorrido inorder
            if (inStrt == inEnd):
                return node

            # Busca si está la raíz en los recorridos PreOrder e Inorder
            iIndex = self.search(In, inStrt, inEnd, node.dato)

            #Recursividad para construir el arbol
            node.left = self.auxiliarPre(In, pre, inStrt,
                                       iIndex - 1, pIndex)
            node.right = self.auxiliarPre(In, pre, iIndex + 1,
                                        inEnd, pIndex)
            return node

    #Construye arbol binario dados los recorridos Inorden y Posorden
    def ConstruirArbolPre(self, In, pre, n):
            pIndex = [0] #Posición de la raíz en un recorrido Preorder (Primera)
            # Invoca el método de construir arbol con recorrido Inorder y Posorder
            self.root = self.auxiliarPre(In, pre, 0, n - 1, pIndex)

    #Encuentra la altura del árbol binario
    def hallarAltura(self,root):
        #Caso Base
        if root is None: #Si la raíz es nula
            return 0
        else:
            #Hallando la altura de la rama izquierda
            alturaIz = self.hallarAltura(root.left)
            #Hallando la altura de la rama derecha
            alturaDe = self.hallarAltura(root.right)

            #Si la altura de la rama izquierda es mayor a la de la derecha
            if(alturaIz>alturaDe):
                return alturaIz+1 #Retorne el valor de la rama izquierda + 1
            else:
                return alturaDe+1 #Retorne el valor de la rama derecha + 1

    #Encuentra las hojas del árbol binario, hay un problema con el retorno de la hoja
    def encontrarHoja(self,root):
        # Si la raíz es nula, retorna
        if (root is None):
            return "El árbol está vacío"
        Hojas = []
        # Si el nodo es una hoja escribe el dato del nodo
        if (root.left is None and root.right is None):
            Hojas.append(str(root))

        # Si tiene hijo izquierdo revisa los otros nodos recursivamente
        if root.left:
            Hojas += self.encontrarHoja(root.left)

        # Si el hijo derecho existe revisa otros nodos recursivamente
        if root.right:
            Hojas += self.encontrarHoja(root.right)
        return Hojas

    #Determinar grado del árbol binario
    def grado(self, root):
        #El mayor grado que puede tener un árbol binario es 2.
        g = 0
        #Caso base
        if root is None: #Si la raíz es nula es grado del árbol es 0
            return 0
        if root.left is not None and root.right is not None:
            #Si algún nodo tiene hijo izquierdo e hijo derecho el mayor grado del arbol es 2
            return 2
        if root.left is not None or root.right is not None:
            #Si todos nodo tiene solo hijo izquierdo o hijo derecho el mayor grado del arbol es 1
            g = 1
        #Recorre el árbol recursivamente
        g = max(g, self.grado(root.left))
        if g == 2:
            return 2
        g = max(g, self.grado(root.right))
        return g

    #Verifica si el nodo existe en el árbol o no
    def buscarNodo(self, root, dato):
        #Caso Base
        if root is None:
            return False
        #Si la raíz actual es igual al dato que se está buscando, si existe.
        if root.dato == dato.get():
            return True
        #Recorre el árbol recursivamente
        result1 = self.buscarNodo(root.left, dato)
        if result1:
            return True
        result2 = self.buscarNodo(root.right, dato)
        return result2

    #Busca el número y los hijos del dato enviado
    def buscarHijos(self,root, dato):
        #Lista de hijos del nodo enviado
        hijos = []
        #Caso base
        if root is None: #Si la raíz actual es nula retorne la lista vacia
            return []

        #Si la raíz actual es igual al dato
        if root.dato == dato.get():
            #Si el hijo izquierdo de la raíz actual no es nulo
            if root.left:
                #Agrega el hijo izquierdo a la lista de hijos
                hijos.append(str(root.left))
            # Si el hijo derecho de la raíz actual no es nulo
            if root.right:
                #Agrega el hijo derecho a la lista de hijos
                hijos.append(str(root.right))
            #Luego de agregarlos retorna la lista de hijos
            return hijos

        #Recorre el árbol recursivamente
        hijos += self.buscarHijos(root.left, dato)
        if hijos:
            return hijos
        hijos += self.buscarHijos(root.right, dato)
        return hijos

    #Busca el padre del dato enviado
    def buscarPapa(self,root, dato):
        # Lista de padre del nodo enviado
        papa = []
        # Caso base
        if root is None:#Si la raíz actual es nula retorne la lista vacia
            return []

        # Si el hijo izquierdo de la raíz actual no es nulo
        if root.left:
            #Si el hijo izquierdo de la raíz actual es igual al dato enviado
            if root.left.dato == dato.get():
                #Agrega el padre a la lista papa
                papa.append(root.dato)
                return papa
        # Si el hijo derecho de la raíz actual no es nulo
        if root.right:
            # Si el hijo derecho de la raíz actual es igual al dato enviado
            if root.right.dato == dato.get():
                # Agrega el padre a la lista papa
                papa.append(root.dato)
                return papa

        #Recorre el árbol recursivamente en preorder
        papa += self.buscarPapa(root.left, dato)
        if papa:
            return papa
        papa += self.buscarPapa(root.right, dato)
        return papa

    # Busca el Hermano del dato enviado
    def buscarHermano(self, root, dato):
        # Lista de hermano del nodo enviado
        hermano = []
        #Caso base
        if root is None:#Si la raíz actual es nula retorne la lista vacia
            return []

        #Si el hijo izquierdo y derecho de la raíz actual no son nulos
        if root.left is not None and root.right is not None:
            #Si el hijo izquierdo de la raíz actual es igual al dato enviado
            if root.left.dato == dato.get():
                #Agrega el hijo derecho de la raíz actual [El contrario]
                hermano.append(root.right.dato)
                return hermano
            # Si el hijo derecho de la raíz actual es igual al dato enviado
            if root.right.dato == dato.get():
                # Agrega el hijo izquierdo de la raíz actual [El contrario]
                hermano.append(root.left.dato)
                return hermano

        #Recorre el árbol recursivamente en Preorder
        hermano += self.buscarHermano(root.left, dato)
        if hermano:
            return hermano
        hermano += self.buscarHermano(root.right, dato)
        return hermano

    #Busca los ancestros del dato enviado
    def buscarAncestros(self, root, dato):
        #Lista de ancestros del nodo enviado
        ancestros = []
        #Caso base
        if root is None: #Si la raíz actual es nula retorne la lista vacia
            return []

        #Agregue la raíz actual
        ancestros.append(root.dato)

        #Si la raíz actual es igual al dato enviado no lo agrega a la lista ancestros
        if root.dato == dato.get():
            #Retorne la lista ancestros sin el dato que se envio
            return ancestros

        #Recorre el arbol recursivamente en preorder
        ancestros += self.buscarAncestros(root.left, dato)
        #Si en la posición final de la lista de ancestros está el dato enviado después de recorrer la rama izquierda del árbol
        if ancestros[-1] == dato.get():
            #retorne la lista sin el dato enviado
            return ancestros
        ancestros += self.buscarAncestros(root.right, dato)
        # Si en la posición final de la lista de ancestros está el dato enviado después de recorrer la rama derecha del árbol
        if ancestros[-1] == dato.get():
            return ancestros
        #Borra el ultimo dato de la lista ancestros
        ancestros.pop()
        return ancestros

    def buscarTio(self,root, dato):
        #Variable StringVar porque el dato enviado es un StringVar
        papa = StringVar()
        #Intente
        try:
            #busca el papá del dato enviado
            papa.set(self.buscarPapa(root, dato)[0])
        except IndexError: #Por si se sale de los limites o si es la raíz del árbol
            papa.set('')
        #Retorna el hermano del papá del nodo enviado.
        return self.buscarHermano(root, papa)

    def buscarAbuelo(self, root, dato):
        # Variable StringVar porque el dato enviado es un StringVar
        papa = StringVar()
        try:
            # busca el papá del dato enviado
            papa.set(self.buscarPapa(root, dato)[0])
        except IndexError: #Por si se sale de los limites o si es la raíz del árbol
            papa.set('')
        #Retorna el papá del papá del nodo enviado.
        return self.buscarPapa(root, papa)

    def buscarDerechoIzquierdo(self, root, dato):
        #Variable bandera para saber si es izquierdo, derecho o ninguno
        flag = -1
        #Caso base
        if root is None:
            return -1
        #Si el hijo izquierdo de la raíz actual no es nulo
        if root.left:
            #Si el hijo izquierdo de la raíz actual es el nodo enviado
            if root.left.dato == dato.get():
                #Retorna 0 que significa que es hijo izquierdo el nodo enviado
                return 0
        # Si el hijo derecho de la raíz actual no es nulo
        if root.right:
            # Si el hijo derecho de la raíz actual es el nodo enviado
            if root.right.dato == dato.get():
                # Retorna 1 que significa que es hijo derecho el nodo enviado
                return 1

        #Recorre recursivamente en preorder el árbol
        flag = self.buscarDerechoIzquierdo(root.left, dato)
        #Si la bandera es diferente de -1 retorne el valor de la bandera
        if flag != -1:
            return flag
        flag = self.buscarDerechoIzquierdo(root.right, dato)
        return flag