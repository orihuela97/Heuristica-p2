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
    Parada = ""
    for i in lista:
        aux1 = ""
        aux = i.split(":")
        for j in aux[0]:
            if j != "C":
                aux1 += j
        idColegio = aux1
        aux1 = ""
        for j in aux[1]:
            if j != "P" and j != " ":
                aux1 += j
        Parada = aux1
        diccionario_aux = dict(Colegio = int(idColegio), numParada = int(Parada))
        colegios.append(diccionario_aux)

    return colegios

def leerAlumnos(lista):
    lista = lista.split(";")

    paradas = []
    alumnos = []
    for i in lista:


        j = 0
        puntero = i[j]
        numParada = ""
        while puntero != ":":
            if puntero != "P":
                numParada += puntero
            j += 1
            puntero = i[j]
        numParada = int(numParada)

        x = i.split(":")
        x.pop(0)
        x = x[0].split(",")
        paradaActual = 0
        for z in x:

            z = z.split("C")
            numAlumnos = int(z[0])
            numColegio = int(z[1])
            for k in range(numAlumnos):
                diccionario_aux = dict(Colegio = numColegio, ParadaOrigen = numParada)
                alumnos.append(diccionario_aux)
        paradaActual += 1
    return alumnos








def reader(fichero):
    arguments = []
    f = open(fichero)
    x = f.read()
    x= x.split("\n")
    y = x.pop(len(x)-2)
    #BUS ES UN DICCIONARIO CON {PARADA,CAPACIDAD}
    bus = leeBusData(y)


    y = x.pop(len(x)-3)
    #COLEGIOS ES UNA LISTA DE DICCIONARIOS, CADA DICCIONARIO TIENE: {IDCOLEGIO,NUMPARADA}
    colegios = leeColegios(y)

    y = x.pop(len(x)-2)
    alumnos = leerAlumnos(y)

    y = x.pop(0)
    y = y.split(" ")
    aux = []
    aux2 = []
    costMatrix = []
    for i in range(len(y)):
        if(y[i] != ''):
            aux.append(y[i])
    nParadas = len(aux)
    for i in range(nParadas):
        aux2=[]
        aux1 = x.pop(0)
        aux1 = aux1.split(" ")
        aux1.pop(0)
        for j in range(len(aux1)):
            if aux1[j] != '':
                if  aux1[j] == '--':
                    aux2.append(-1)
                else:
                    try:
                        aux2.append(int(aux1[j]))

                    except:
                        print("La variable "+ aux1[j]+ " no es un entero")
                        sys.exit()

        costMatrix.append(aux2)


    arguments.append(bus)
    arguments.append(colegios)
    arguments.append(alumnos)
    arguments.append(costMatrix)
    return arguments

arguments = reader("input.txt")

print(arguments[0])
print(arguments[1])
print(arguments[2])
print(arguments[3])
