import sys

def leeBusData(lista):
    lista = lista.split(" ")
    lista.pop(0)
    aux = ""
    for i in lista[0]:
        if i != "P":
            aux += i
    #BUS ES UN DICCIONARIO#
    bus = dict(parada = int(aux),capacidad = int(lista[1]))
    return bus

def leeColegios(lista):
    colegios = []
    lista = lista.split(";")
    aux = []
    aux1 = ""
    idColegio = ""
    parada = ""
    for i in lista:
        aux1 = ""
        aux = i.split(":")
        for j in aux[0]:
            if j != "C" and j != " ":
                aux1 += j
        idColegio = aux1
        aux1 = ""
        for j in aux[1]:
            if j != "P" and j != " ":
                aux1 += j
        parada = aux1
        colegio = [int(idColegio),int(parada)]
        colegios.append(colegio)

    return colegios

def leerAlumnos(lista):
    lista = lista.split(";")
    alumnos = []
    for i in lista:
        j = 0
        puntero = i[j]
        numParada = ""
        while puntero != ":":
            if puntero != "P" and puntero != " ":
                numParada += puntero
            j += 1
            puntero = i[j]
        numParada = int(numParada)

        x = i.split(":")
        x.pop(0)
        x = x[0].split(",")

        for z in x:
            z = z.split("C")
            numAlumnos = int(z[0])
            idColegio = int(z[1])
            for k in range(numAlumnos):
                alumno=[idColegio,numParada]
                alumnos.append(alumno)
    return alumnos




def reader(fichero):
    arguments = []
    f = open(fichero)
    x = f.read()
    x= x.split("\n")
    aux=[]
    for i in range(len(x)):
        if(x[i]!=''):
            aux.append(x[i])
    x=aux
    y = x.pop(0)
    y = y.split(" ")
    aux = []
    costMatrix = []

    for i in range(len(y)):
        if(y[i] != ''):
            aux.append(y[i])
    y=aux
    nParadas = len(y)
    for i in range(nParadas):
        aux=[]
        aux1 = x.pop(0)
        aux1 = aux1.split(" ")
        aux1.pop(0)
        for j in range(len(aux1)):
            if aux1[j] != '':
                if  aux1[j] == '--':
                    aux.append(-1)
                else:
                    try:
                        aux.append(int(aux1[j]))
                    except:
                        print("La variable "+ aux1[j]+ " no es un entero")
                        sys.exit()

        costMatrix.append(aux)
    colegios = leeColegios(x.pop(0))
    alumnos = leerAlumnos(x.pop(0))
    bus = leeBusData(x.pop(0))
    arguments.append(bus)
    arguments.append(colegios)
    arguments.append(alumnos)
    arguments.append(costMatrix)
    return arguments
