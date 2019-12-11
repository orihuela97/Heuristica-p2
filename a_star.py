from parserDatos import *



arguments = reader("input.txt")



def compararEstados(estado1,estado2): #devuelve True si son iguales
    pBus1=estado1[0]
    pBus2=estado2[0]
    listAlumSub1=estado1[1].copy()
    listAlumSub2=estado2[1].copy()
    listAlumPend1=estado1[2].copy()
    listAlumPend2=estado2[2].copy()
    if(pBus1!=pBus2):
        return False

    encontrado = True
    while len(listAlumSub1)>0 and encontrado:
        alumno=listAlumSub1.pop(0)
        encontrado=False
        for i in range(len(listAlumSub2)):
            if alumno==listAlumSub2[i]:
                encontrado=True
                listAlumSub2.pop(i)
                break
    if not encontrado:
        return False
    while len(listAlumPend1)>0 and encontrado:
        alumno=listAlumPend1.pop(0)
        encontrado=False
        for i in range(len(listAlumPend2)):
            if alumno==listAlumPend2[i]:
                encontrado=True
                listAlumPend2.pop(i)
                break
    if not encontrado or len(listAlumSub2)!=0 or len(listAlumPend2)!=0:
        return False
    return True


def cambiarColegiosPorParadas(listaColegios,listaAlumnosPendientes):
    aux=listaAlumnosPendientes

    for i in aux:
        for j in listaColegios:
            if i[0]==j[0]:

                i[0]=j[1]
                break
    return aux

def divideVencerasOrdenar(sucesores):
    if len(sucesores)>1:
        lMitad=len(sucesores)//2
        izq=sucesores[:lMitad]
        der=sucesores[lMitad:]

        divideVencerasOrdenar(izq)
        divideVencerasOrdenar(der)

        i=0
        j=0
        k=0

        while i<len(izq) and j<len(der):
            if izq[i][3]<der[j][3]:
                sucesores[k]=izq[i]
                i+=1
            else:
                sucesores[k]=der[j]
                j+=1
            k+=1
        while j<len(der):
            sucesores[k]=der[j]
            j+=1
            k+=1
        while i<len(izq):
            sucesores[k]=izq[i]
            i+=1
            k+=1



#Configuracion
matrizCostes=arguments[3]
capacidadBus=arguments[0].get("capacidad")
listaColegios=arguments[1]
costeCargaPorAlumno=1
costeDescargaPorAlumno=1

#nodo inicial
estadoInicial = [arguments[0].get("parada"),[],cambiarColegiosPorParadas(listaColegios,arguments[2])] #posicionBus, listaAlumnosSubidos, listaAlumnosPendientes
#nodo meta
estadoFinal = [arguments[0].get("parada"),[],[]]

#funcion heuristica
def funcionHeuristica(estado):
    return 0


#acciones
def operadores(nodo):
    sucesores=[]
    pBus=nodo[1][0]

    #desplazamiento
    filaCostes = matrizCostes[pBus-1]
    for i in range(len(filaCostes)):
        if(filaCostes[i]!=-1):
            listaAlumnosSubidos=nodo[1][1].copy()
            listaAlumnosPendientes=nodo[1][2].copy()
            estadoGenerado=[i+1,listaAlumnosSubidos,listaAlumnosPendientes]
            coste = nodo[2]+filaCostes[i]
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
            sucesores.append(nodoGenerado)
    #cargar
    for i in range(len(listaAlumnosPendientes)):
        if pBus==listaAlumnosPendientes[i][1]: # en 0 se encuntra la parda al colegio que va, y en 1 la parada del alumno
            auxListaAlumnosSubidos=nodo[1][1].copy()
            auxListaAlumnosPendientes=nodo[1][2].copy()
            auxListaAlumnosSubidos.append(auxListaAlumnosPendientes.pop(i))
            estadoGenerado=[pBus,auxListaAlumnosSubidos,auxListaAlumnosPendientes]
            coste = nodo[2]+costeCargaPorAlumno
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
            sucesores.append(nodoGenerado)

    #descargar
    for i in range(len(listaAlumnosSubidos)):
        if pBus==listaAlumnosSubidos[i][0]: # en 0 se encuntra el id del colegio al que va, y en 1 la parada del alumno
            auxListaAlumnosSubidos=nodo[1][1].copy()
            auxListaAlumnosSubidos.pop(i)
            estadoGenerado=[pBus,auxListaAlumnosSubidos,listaAlumnosPendientes]
            coste = nodo[2]+costeDescargaPorAlumno
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
            sucesores.append(nodoGenerado)

    return sucesores


#algoritmo A estrella

listaAbierta=[]
listaCerrada=[]
exito=False
nodoInicial=[[],estadoInicial,0,funcionHeuristica(estadoInicial)]
listaAbierta.append([[],estadoInicial,0,funcionHeuristica(estadoInicial)]) #estadoNodoPadre, estadoNodo, coste, funcionEvaluacion


while len(listaAbierta)!=0 and not exito:
    nodoAExpandir=listaAbierta.pop(0)
    print(nodoAExpandir)
    nodoEncontrado=False
    for i in listaCerrada:
            nodoEncontrado=compararEstados(i[1],nodoAExpandir[1])
            if nodoEncontrado:
                break

    if(not nodoEncontrado):
        if compararEstados(nodoAExpandir[1],estadoFinal):
            exito=True
        else:
            #inserta el nodo a expandir en cerrada
            listaCerrada.append(nodoAExpandir)
            #expande generando S sucesores
            sucesores=operadores(nodoAExpandir)
            #insertar de forma ordenada

            #ordeno los sucesores por su función de funcionEvaluacion cambiar burbuja a divide y venceras
            divideVencerasOrdenar(sucesores)


            #inserto de forma ordenada los sucesores en la lista abierta
            contadorListaAbierta=0
            contadorSucesores=0
            aux=[]
            while contadorListaAbierta<len(listaAbierta) and contadorSucesores<len(sucesores):
                if sucesores[contadorSucesores][3]<listaAbierta[contadorListaAbierta][3]:
                    aux.append(sucesores[contadorSucesores])
                    contadorSucesores+=1
                else:
                    aux.append(listaAbierta[contadorListaAbierta])
                    contadorListaAbierta+=1
            while contadorListaAbierta<len(listaAbierta):
                aux.append(listaAbierta[contadorListaAbierta])
                contadorListaAbierta+=1

            while contadorSucesores<len(sucesores):
                aux.append(sucesores[contadorSucesores])
                contadorSucesores+=1
            listaAbierta=aux


print(exito)
