from parser import *

class Node:
    def __init__(self,pBus,listaAlumnosSubidos,listaAlumnosPendientes):
        self.pBus = pBus
        self.listaAlumnosSubidos = listaAlumnosSubidos
        self.listaAlumnosPendientes = listaAlumnosPendientes

class Problem:
    def __init__(self,Matrix,colegios,alumnos):
         self.Matrix = Matrix
         self.colegios = colegios
         self.alumnos = alumnos

    def adyacentes(self,Pi,Pj):
            adyacentes = False
            j = 0
            for i in self.Matrix[Pi-1]:
                if i > 0 and j == Pj - 1:
                    adyacentes = True
                j += 1
            return adyacentes

    def NodoEnLista(self,Nodo,lista):
        exito = False
        if lista.count(Nodo) > 0:
            exito = True
        return exito

    def operacionMoverBus(self,Pj,father):
        if adyacentes(self.pBus, Pj) == True and Pj <= len(self.Matrix) and Pj >= 1:
            newNodoHijo = Node(Pj,father.listaAlumnosSubidos, father.listaAlumnosPendientes)
            return newNodoHijo



    


    def a_star(self):
        abierta = []
        cerrada = []
        exito = False
        arguments = reader("input.txt")
        capacidadMaxima = arguments[0].get("Capacidad")
        pBus = arguments[0].get("Parada")
        listaAlumnosSubidos = []
        listaAlumnosPendientes = self.alumnos
        start = Node(pBus, listaAlumnosSubidos, listaAlumnosPendientes)
        abierta.append(start)
        longitudAbierta = len(abierta)
        while exito == False and longitudAbierta != 0:
            nodoExpandido = self.NodoEnLista(abierta[0], cerrada)
            #if nodoExpandido == False:







            exito = True





















arguments = reader("input.txt")
Problema1 = Problem(arguments[3],arguments[1],arguments[2])
Problema1.a_star()
