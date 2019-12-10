from parser import *

class Node:
    def __init__(self,pBus,listaAlumnosSubidos,listaAlumnosPendientes):
        self.pBus = pBus
        self.listaAlumnosSubidos = listaAlumnosSubidos
        self.listaAlumnosPendientes = listaAlumnosPendientes











arguments = reader("input.txt")
#Configuracion
matrizCostes=arguments[3]
capacidadBus=arguments[0].get("Capacidad")
listaColegios=arguments[1]
id=1
#nodo inicial
estadoInicial = Node(]arguments[0].get("Parada"),[],arguments[2])

#nodo meta
estadoFinal = Node(arguments[0].get("Parada"),[],[])

#funcion heuristica
def heuristica(estado):
    return 0


#acciones
def operadores(nodo,listaAbierta,listaCerrada):
    filaCostes = matrizCostes[nodo[2][0]-1]
    for i in range(len(filaCostes)):
        if(filaCostes[i]!=-1):
            estadoGenerado=[i+1,nodo[2][1],nodo[2][2]]
            id=id+1
            nodoGenerado=[id,nodo[0],estadoGenerado,nodo[3]+filaCostes[i],heuristica(estadoGenerado)]
            listaAbierta.append(nodoGenerado)




#algoritmo A estrella

listaAbierta=[]
listaCerrada=[]
exito=False


listaAbierta.append([id,1,estadoInicial,0,heuristica(estadoInicial)]) #idNodo, idPadre, nodo, coste
while len(listaAbierta)!=0 and exito==False:
    nodoAExpandir=listaAbierta.pop(0)
    nodoEncontrado=False
    for i in listaCerrada and nodoEncontrado==False:
        if i[2]==nodoAExpandir[2]:
            nodoEncontrado=True

    if(nodoEncontrado==False):
        if nodoAExpandir[2]==estadoFinal:
            exito=True
        else:
            print(nodoAExpandir)
            operadores(nodoAExpandir,listaAbierta,listaCerrada)



















print(arguments[0])
print(arguments[1])
print(arguments[2])
print(arguments[3])
