from parserDatos import *



arguments = reader(sys.argv[1])



def compararEstados(estado1,estado2): #devuelve True si son iguales
    pBus1=estado1[0]
    pBus2=estado2[0]
    listAlumSub1=estado1[1]
    listAlumSub2=estado2[1]
    listAlumPend1=estado1[2]
    listAlumPend2=estado2[2]
    if(pBus1!=pBus2):
        return False

    if listAlumSub1!=listAlumSub2:
        return False

    if listAlumPend1!=listAlumPend2:
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

def getCosteMinimoMovimiento(matrizCostes):
    if(len(matrizCostes)>0):
        if(len(matrizCostes[0])>0):
            costeMinimo=matrizCostes[0][0]
            for i in matrizCostes:
                for j in i:
                    if (j<costeMinimo and j!=-1) or (costeMinimo==-1):
                        costeMinimo=j
            return costeMinimo
    return 0



#Configuracion
matrizCostes=arguments[3]
capacidadBus=arguments[0].get("capacidad")
listaColegios=arguments[1]
costeCargaPorAlumno=1
costeDescargaPorAlumno=1
costeMinimoMovimiento=getCosteMinimoMovimiento(matrizCostes)
#nodo inicial
estadoInicial = [arguments[0].get("parada"),[],cambiarColegiosPorParadas(listaColegios,arguments[2])] #posicionBus, listaAlumnosSubidos, listaAlumnosPendientes
#nodo meta
estadoFinal = [arguments[0].get("parada"),[],[]]

#funciones heuristica
def funcionHeuristica(estado):
    return funcionHeuristica1(estado)

def funcionHeuristica1(estado):
    return 0

def funcionHeuristica2(estado):
    valor=len(estado[1])*costeDescargaPorAlumno
    valor+=len(estado[2])*costeCargaPorAlumno+len(estado[2])*costeDescargaPorAlumno
    paradasColegiosAVisitar=[]
    paradasAlumnosAVisitar=[]
    for i in estado[1]:
        if i[1]!=estado[0] and not (i[1] in paradasAlumnosAVisitar):
            paradasAlumnosAVisitar.append(i[1])
    for i in estado[2]:
        if i[1]!=estado[0] and not (i[1] in paradasColegiosAVisitar):
            paradasColegiosAVisitar.append(i[1])
    for i in estado[1]:
        if  not (i[0] in paradasColegiosAVisitar):
            paradasColegiosAVisitar.append(i[0])

    valor+=(len(paradasColegiosAVisitar)+len(paradasAlumnosAVisitar))*costeMinimoMovimiento
    return valor


#acciones
def operadores(nodo):
    sucesores=[]
    pBus=nodo[1][0]
    auxListaAlumnosSubidos=nodo[1][1]
    auxAlumnosPendientes=nodo[1][2]

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
    if len(auxListaAlumnosSubidos)<capacidadBus:
        for i in range(len(auxAlumnosPendientes)):
            if pBus==auxAlumnosPendientes[i][1]: # en 0 se encuntra la parda al colegio que va, y en 1 la parada del alumno
                listaAlumnosSubidos=nodo[1][1].copy()
                listaAlumnosPendientes=nodo[1][2].copy()
                alumno=listaAlumnosPendientes.pop(i)
                listaAlumnosSubidos.append(alumno)
                estadoGenerado=[pBus,listaAlumnosSubidos,listaAlumnosPendientes]
                coste=nodo[2]+costeCargaPorAlumno
                heuristica = funcionHeuristica(estadoGenerado)
                nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
                sucesores.append(nodoGenerado)
                break



    #descargar
    for i in range(len(auxListaAlumnosSubidos)):
        if pBus==auxListaAlumnosSubidos[i][0]: # en 0 se encuntra el id del colegio al que va, y en 1 la parada del alumno
            listaAlumnosSubidos=nodo[1][1].copy()
            listaAlumnosPendientes=nodo[1][2].copy()
            listaAlumnosSubidos.pop(i)
            estadoGenerado=[pBus,listaAlumnosSubidos,listaAlumnosPendientes]
            coste=nodo[2]+costeDescargaPorAlumno
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
            sucesores.append(nodoGenerado)
            break

    return sucesores


#algoritmo A estrella

listaAbierta=[]
listaCerrada=[]
exito=False
nodoInicial=[estadoInicial,estadoInicial,0,funcionHeuristica(estadoInicial)]
listaAbierta.append(nodoInicial) #estadoNodoPadre, estadoNodo, coste, funcionEvaluacion
nodoAExpandir=[]

while len(listaAbierta)!=0 and not exito:
    nodoAExpandir=listaAbierta.pop(0)
    #print(nodoAExpandir)
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

estadoAux=nodoAExpandir[1]
estadoPadreAux=nodoAExpandir[0]
recorrido=[]
print(nodoAExpandir[2])
if(exito):
    while not compararEstados(estadoAux,estadoPadreAux):
        recorrido.append(estadoAux)
        for i in listaCerrada:
            if compararEstados(estadoPadreAux,i[1]):
                estadoAux=estadoPadreAux
                estadoPadreAux=i[0]
                break
    recorrido.append(estadoAux)

    for i in recorrido:
        print(i)
    print(len(listaCerrada))
else:
    print("Sin soluciones")
