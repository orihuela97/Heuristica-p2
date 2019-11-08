from constraint import *

def out_file(solution, solution2):
	archivo = open("output.txt", "w")
	frase = "Solucion al problema 1 obtenida correctamente.\n"
	archivo.write(frase)
	frase = "La asigancion obtenida para cada hora de clase es:\n"
	archivo.write(frase)
	frase = "L1 ---> " + solution.get("L1") + "\n"
	archivo.write(frase)
	frase = "L2 ---> " + solution.get("L2") + "\n"
	archivo.write(frase)
	frase = "L3 ---> " + solution.get("L3") + "\n"
	archivo.write(frase)
	frase = "M1 ---> " + solution.get("M1") + "\n"
	archivo.write(frase)
	frase = "M2 ---> " + solution.get("M2") + "\n"
	archivo.write(frase)
	frase = "M3 ---> " + solution.get("M3") + "\n"
	archivo.write(frase)
	frase = "X1 ---> " + solution.get("X1") + "\n"
	archivo.write(frase)
	frase = "X2 ---> " + solution.get("X2") + "\n"
	archivo.write(frase)
	frase = "X3 ---> " + solution.get("X3") + "\n"
	archivo.write(frase)
	frase = "J1 ---> " + solution.get("J1") + "\n"
	archivo.write(frase)
	frase = "J2 ---> " + solution.get("J2") + "\n"
	archivo.write(frase)
	frase = "----------------------------------------------------------------------------------------\n"
	archivo.write(frase)
	frase = "Solucion al problema 2 obtenida correctamente.\nLa asignacion de un profesor para cada asignatura es:\n"
	archivo.write(frase)
	frase = "N ---> " + solution2.get("N") + "\n"
	archivo.write(frase)
	frase = "S ---> " + solution2.get("S") + "\n"
	archivo.write(frase)
	frase = "L ---> " + solution2.get("L") + "\n"
	archivo.write(frase)
	frase = "M ---> " + solution2.get("M") + "\n"
	archivo.write(frase)
	frase = "I ---> " + solution2.get("I") + "\n"
	archivo.write(frase)
	frase = "F ---> " + solution2.get("F") + "\n"
	archivo.write(frase)
	archivo.close()

def two_perTeacher(*args):
	juan = 0
	andrea = 0
	lucia = 0
	juanList = []
	andreaList = []
	luciaList = []
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
def juan_NaturalesSociales(*args):
	acepta = 0
	if args[0] == 'J':
		if args[1] != 'N' and args[2] != 'N':
			acepta = 1
	if acepta == 1:
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
	hayNaturales = 0
	contadorNaturales = 0
	for i in args:
		if i == 'N':
			hayNaturales = 1
	if hayNaturales == 1:
		for i in args:
			if i == 'N':
				contadorNaturales += 1
		if contadorNaturales == 2:
			return True
	else:
		return True
problem = Problem()
# Variables para el primer problema
problem.addVariables(["L1", "L2", "L3","M1","M2","M3","X1","X2","X3","J1","J2"], ['N','S','L','M','I','F'])
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
#sSolucion al problema 1
solution = problem.getSolution()
#-------------------------------------------------------------------------PROBLEMA2-----------------------------
problem2 = Problem()
problem2.addVariables(['N','S','L','M','I','F'],['J', 'A', 'L'])
problem2.addConstraint(juan_NaturalesSociales, ('N', solution.get("L1"), solution.get("J1")))
problem2.addConstraint(lucia_Sociales, ('S', 'F'))
problem2.addConstraint(two_perTeacher, ('N','S','L','M','I','F'))
solution2 = problem2.getSolution()
#------------------------------------------------SALIDA A UN ARCHIVO DE TEXTO--------------------------------
out_file(solution, solution2)
