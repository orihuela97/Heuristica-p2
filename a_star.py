from parserDatos import *
import time


arguments = reader(sys.argv[1])
nombreHeuristica=sys.argv[2]


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

def getStrColegio(paradaColegio):
    for i in listaColegios:
        if i[1]==paradaColegio:
            return "C"+str(i[0])


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
    if nombreHeuristica!="heuristicaDefault" and nombreHeuristica!="heuristica1" and nombreHeuristica!="heuristica2":
        print("Nombre de heuristica mal introducido")
        print("Opciones: heuristicaDefault heuristica1 heuristica2")
        sys.exit()
    if nombreHeuristica=="heuristicaDefault":
        return funcionHeuristicaDefault(estado)
    if nombreHeuristica=="heuristica1":
        return funcionHeuristica1(estado)
    if nombreHeuristica=="heuristica2":
        return funcionHeuristica2(estado)

def funcionHeuristicaDefault(estado):
    return 0

def funcionHeuristica1(estado):
    valor=len(estado[1])*costeDescargaPorAlumno
    valor+=len(estado[2])*costeCargaPorAlumno+len(estado[2])*costeDescargaPorAlumno
    return valor
    
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
    listaAlumnosSubidos=nodo[1][1]
    listaAlumnosPendientes=nodo[1][2]

    cargadoDescargado=False
    #cargar
    if len(listaAlumnosSubidos)<capacidadBus:
        for i in range(len(listaAlumnosPendientes)):
            if pBus==listaAlumnosPendientes[i][1]:
                cargadoDescargado=True
                auxListaAlumnosSubidos=listaAlumnosSubidos.copy()
                auxListaAlumnosPendientes=listaAlumnosPendientes.copy()
                alumno=auxListaAlumnosPendientes.pop(i)
                auxListaAlumnosSubidos.append(alumno)
                coste=nodo[2]+costeCargaPorAlumno
                estadoGenerado=[pBus,auxListaAlumnosSubidos,auxListaAlumnosPendientes]
                heuristica = funcionHeuristica(estadoGenerado)
                nodoGenerado=[nodo[1],estadoGenerado,coste,coste+heuristica]
                sucesores.append(nodoGenerado)
                break

    #descargar, nota: lo hace de golpe, en ningún momento le va a interesar tener cargado un nino que podria haber dejado
    if not cargadoDescargado:
        auxListaAlumnosSubidos=nodo[1][1].copy()
        auxListaAlumnosPendientes=nodo[1][2].copy()
        contador=0
        auxCoste=nodo[2]
        while contador<len(auxListaAlumnosSubidos):
            if pBus==auxListaAlumnosSubidos[contador][0]: # en 0 se encuntra el id del colegio al que va, y en 1 la parada del alumno
                cargadoDescargado=True
                auxListaAlumnosSubidos.pop(contador)
                auxCoste+=costeDescargaPorAlumno
            else:
                contador+=1
        if cargadoDescargado:
            estadoGenerado=[pBus,auxListaAlumnosSubidos,auxListaAlumnosPendientes]
            heuristica = funcionHeuristica(estadoGenerado)
            nodoGenerado=[nodo[1],estadoGenerado,auxCoste,auxCoste+heuristica]
            sucesores.append(nodoGenerado)

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

    return sucesores


tiempoComiezo = time.time()
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
if(exito):
    tiempoFin = time.time()
    #obtener el camino
    while not compararEstados(estadoAux,estadoPadreAux):
        recorrido.append(estadoAux)
        for i in listaCerrada:
            if compararEstados(estadoPadreAux,i[1]):
                estadoAux=estadoPadreAux
                estadoPadreAux=i[0]
                break
    recorrido.append(estadoAux)

    #print en un fichero
    fileRecorrido = open("problema.prob.output", "w")
    estadoAux=nodoAExpandir[1]
    fileRecorrido.write("P"+str(recorrido[len(recorrido)-1][0]))
    contador=len(recorrido)-2
    contadorParadas=1
    while contador>=0:
        if(recorrido[contador][0]!=estadoAux[0]):
            fileRecorrido.write(" --> P"+str(recorrido[contador][0]))
            contadorParadas+=1
        else:
            if len(recorrido[contador][1])<len(estadoAux[1]):
                auxListaSubidos1=recorrido[contador][1].copy()
                auxListaSubidos2=estadoAux[1].copy()
                listaBajan=[]
                while(len(auxListaSubidos1)>0):
                    alumno=auxListaSubidos1.pop()
                    for i in range(len(auxListaSubidos2)):
                        if alumno==auxListaSubidos2[i]:
                            auxListaSubidos2.pop(i)
                            break

                for i in auxListaSubidos2:
                    repetido=False
                    for j in listaBajan:
                        if i[0]==j[1]:
                            repetido=True
                            j[0]+=1
                            break
                    if not repetido:
                        listaBajan.append([1,i[0]])
                fileRecorrido.write(" (B: ")
                for i in range(len(listaBajan)-1):
                    fileRecorrido.write(str(listaBajan[i][0])+" "+getStrColegio(listaBajan[i][1])+",")
                if len(listaBajan)>0:
                    fileRecorrido.write(str(listaBajan[len(listaBajan)-1][0])+" "+getStrColegio(listaBajan[len(listaBajan)-1][1])+")")

            if len(recorrido[contador][2])<len(estadoAux[2]):
                auxListaPendientes1=recorrido[contador][2].copy()
                auxListaPendientes2=estadoAux[2].copy()
                listaSuben=[]
                while(len(auxListaPendientes1)>0):
                    alumno=auxListaPendientes1.pop()
                    for i in range(len(auxListaPendientes2)):
                        if alumno==auxListaPendientes2[i]:
                            auxListaPendientes2.pop(i)
                            break

                for i in auxListaPendientes2:
                    repetido=False
                    for j in listaSuben:
                        if i[0]==j[1]:
                            repetido=True
                            j[0]+=1
                            break
                    if not repetido:
                        listaSuben.append([1,i[0]])
                fileRecorrido.write(" (S: ")
                for i in range(len(listaSuben)-1):
                    fileRecorrido.write(str(listaSuben[i][0])+" "+getStrColegio(listaSuben[i][1])+",")
                if len(listaSuben)>0:
                    fileRecorrido.write(str(listaSuben[len(listaSuben)-1][0])+" "+getStrColegio(listaSuben[len(listaSuben)-1][1])+")")


        estadoAux=recorrido[contador]
        contador-=1

    #estadisticas
    fileStats = open("problema.prob.statistics", "w")
    fileStats.write("Tiempo total: "+str(tiempoFin-tiempoComiezo)+" segundos\n")
    fileStats.write("Coste total: "+str(nodoAExpandir[2])+"\n")
    fileStats.write("Paradas visitadas: "+str(contadorParadas)+"\n")
    fileStats.write("Nodos expandidos: "+str(len(listaCerrada)))
    print("Exito, puedes encontrar la solución en problema.prob.output y las estadísticas en problema.prob.statistics")

else:
    print("Sin solución")
