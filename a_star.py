from parserDatos import *



arguments = reader("input.txt")



def compararEstados(estado1,estado2): #devuelve True si son iguales
    pBus1=estado1[0]
    pBus2=estado2[0]
    listAlumSub1=estado1[1]
    listAlumSub2=estado2[1]
    listAlumPend1=estado1[2]
    listAlumPend2=estado2[2]
    if(pBus1!=pBus2 or len(listAlumSub1)!=len(listAlumSub2) or len(listAlumPend1)!=len(listAlumPend2)):
        return False;
    for i in listAlumSub1:
        if (i in listAlumSub2)==False:
            return False
    for i in listAlumPend1:
        if (i in listAlumPend2)==False:
            return False
    return True


#Configuracion
matrizCostes=arguments[3]
capacidadBus=arguments[0].get("capacidad")
listaColegios=arguments[1]
costeCargaPorAlumno=1
costeDescargaPorAlumno=1

#nodo inicial
estadoInicial = [arguments[0].get("parada"),[],arguments[2]] #posicionBus, listaAlumnosSubidos, listaAlumnosPendientes

#nodo meta
estadoFinal = [arguments[0].get("parada"),[],[]]

#funcion heuristica
def funcionHeuristica(estado):
    return 0


#acciones
def operadores(nodo,listaAbierta,listaCerrada):
    sucesores=[]
    #desplazamiento
    filaCostes = matrizCostes[nodo[1][0]-1]
    for i in range(len(filaCostes)):
        if(filaCostes[i]!=-1):
            estadoGenerado=[i+1,nodo[1][1],nodo[1][2]]
            coste = nodo[2]+filaCostes[i]
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
            sucesores.append(nodoGenerado)
    #cargar
    

    #descargar




#algoritmo A estrella

listaAbierta=[]
listaCerrada=[]
exito=False
nodoInicial=[[],estadoInicial,0,funcionHeuristica(estadoInicial)]
listaAbierta.append([[],estadoInicial,0,funcionHeuristica(estadoInicial)]) #estadoNodoPadre, estadoNodo, coste, funcionEvaluacion


while len(listaAbierta)!=0 and not exito:
    nodoAExpandir=listaAbierta.pop(0)
    nodoEncontrado=False
    for i in listaCerrada and not nodoEncontrado:
            nodoEncontrado=compararEstados(i[1],nodoAExpandir[1])

    if(not nodoEncontrado):
        if compararEstados(nodoAExpandir[1],estadoFinal):
            exito=True
        else:
            operadores(nodoAExpandir,listaAbierta,listaCerrada)
