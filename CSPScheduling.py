from constraint import *
def out_file2(solution):
	archivo = open("output.txt", "w")
	frase = "Solucion al problema 1 obtenida correctamente.\n"
	archivo.write(frase)
	frase = "\nLa asignacion obtenida para cada hora de clase es:\n"
	archivo.write(frase)
	frase = "\nLUNES     MARTES     MIERCOLES     JUEVES\n"
	archivo.write(frase)
	frase = "----------------------------------------------------------------------\n"
	archivo.write(frase)
	frase = solution.get("L1") + "          " + solution.get("M1") +  "             " + solution.get("X1") + "             " + solution.get("J1") + "\n"
	archivo.write(frase)
	frase = solution.get("L2") + "          " + solution.get("M2") +  "             " + solution.get("X2") + "             " + solution.get("J2") + "\n"
	archivo.write(frase)
	frase = solution.get("L3") + "          " + solution.get("M3") +  "             " + solution.get("X3") + "\n"
	archivo.write(frase)
	frase = "----------------------------------------------------------------------\n"
	archivo.write(frase)
	frase = "Solucion al problema 2 obtenida correctamente.\n\nLa asignacion de un profesor para cada asignatura es:\n"
	archivo.write(frase)
	frase = "\nNATURALES     SOCIALES     MATEMATICAS     LENGUA     INGLES     E.FISICA\n"
	archivo.write(frase)
	frase = "-------------------------------------------------------------------------\n"
	archivo.write(frase)
	frase = solution.get("N") + "             " + solution.get("S") + "             " + solution.get("M") +  "              " + solution.get("L") + "              " + solution.get("I")+ "              " + solution.get("F") + "\n"
	archivo.write(frase)
	archivo.close()


def two_perTeacher(*args):
	juan = 0
	andrea = 0
	lucia = 0
	for i in args:
		if i == 'J':
			juan += 1
		elif i == 'L':
			lucia += 1
		else:
			andrea += 1
	if juan == 2 and andrea == 2 and lucia == 2:
		return True


def lucia_Sociales(*args):
	if args[0] == 'L':
		if args [1] == 'A':
			return True
	else:
		return True


def juan_primera(*args):
	if args[0] == 'J':
		if args[1] == 'N' or args[1] == 'S' or args[2] == 'N' or args[2] == 'S':
			return False
	return True


def totalHours(*args):
	contadorNaturales = 0
	contadorSociales = 0
	contadorLengua = 0
	contadorMatematicas = 0
	contadorIngles = 0
	contadorEfisica = 0
	for i in args:
		if i == 'N':
			contadorNaturales += 1
		if i == 'S':
			contadorSociales += 1
		if i == 'L':
			contadorLengua += 1
		if i == 'M':
			contadorMatematicas += 1
		if i == 'I':
			contadorIngles += 1
		if i == 'F':
			contadorEfisica += 1
	if contadorNaturales == 2 and contadorSociales == 2 and contadorLengua == 2 and contadorMatematicas == 2 and contadorIngles == 2 and contadorEfisica == 1:
		return True


def Math_NatIngles(*args):
	hayMates = 0
	hayNaturales = 0
	hayIngles = 0
	for i in args:
		if i == 'M':
			hayMates = 1
	if hayMates == 1:
		for i in args:
			if i == 'N':
				hayNaturales = 1
			if i == 'I':
				hayIngles = 1
		if hayNaturales == 0 and hayIngles == 0:
			return True
	else:
	 return True

def MathFirstHours(*args):
	hayMates = 0
	for i in args:
		if i == 'M':
			hayMates = 1
	if hayMates == 0:
		return True

def socialesLastHours(*args):
	haySociales = 0
	for i in args:
		if i == 'S':
			haySociales = 1
	if haySociales == 0:
		return True


def naturalesSameDay(*args):
	true = 0
	hayNaturales = 0
	for i in args:
		if i == 'N':
			hayNaturales = 1
	if hayNaturales == 1:
		for i in range(len(args)):
			if args[i] == 'N' and ((i + 1) < len(args)):
				if args[i+1] == 'N':
					true = 1
		if true == 1:
			return True
	else:
		return True
problem = Problem()
# Variables para el primer problema
problem.addVariables(["L1", "L2", "L3","M1","M2","M3","X1","X2","X3","J1","J2"], ['N','S','L','M','I','F'])
problem.addVariables(['N','S','L','M','I','F'],['J', 'A', 'L'])
# Restricciones para el problema 1
problem.addConstraint(naturalesSameDay, ('L1', 'L2', 'L3'))
problem.addConstraint(naturalesSameDay, ('M1', 'M2', 'M3'))
problem.addConstraint(naturalesSameDay, ('X1', 'X2', 'X3'))
problem.addConstraint(naturalesSameDay, ('J1', 'J2'))
problem.addConstraint(socialesLastHours,("L1", "L2","M1","M2","X1","X2","J1"))
problem.addConstraint(MathFirstHours, ("L2", "L3","M2","M3","X2","X3","J2"))
problem.addConstraint(Math_NatIngles, ('L1', 'L2', 'L3'))
problem.addConstraint(Math_NatIngles, ('M1', 'M2', 'M3'))
problem.addConstraint(Math_NatIngles, ('X1', 'X2', 'X3'))
problem.addConstraint(Math_NatIngles, ('J1', 'J2'))
problem.addConstraint(totalHours, ('L1', 'L2', 'L3','M1','M2','M3','X1','X2','X3','J1','J2'))
problem.addConstraint(juan_primera, ('N', 'L1', "J1"))
problem.addConstraint(juan_primera, ('S', 'L1', "J1"))
problem.addConstraint(lucia_Sociales, ('S', 'F'))
problem.addConstraint(two_perTeacher, ('N','S','L','M','I','F'))
#sSolucion al problema 1
solution = problem.getSolution()
#------------------------------------------------SALIDA A UN ARCHIVO DE TEXTO--------------------------------
#out_file(solution, solution2)
out_file2(solution)
