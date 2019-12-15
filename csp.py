from constraint import *
import time

def out_file(solution,numeroSoluciones, tiempo):
	archivo = open("Scheduling.txt", "w")
	frase = "Solucion al subproblema 1 obtenida correctamente.\n"
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
	frase = "Solucion al subproblema 2 obtenida correctamente.\n\nLa asignacion de un profesor para cada asignatura es:\n"
	archivo.write(frase)
	frase = "\nNATURALES     SOCIALES     MATEMATICAS     LENGUA     INGLES     GIMNASIA\n"
	archivo.write(frase)
	frase = "-------------------------------------------------------------------------\n"
	archivo.write(frase)
	frase = solution.get("Naturales") + "             " + solution.get("Sociales") + "             " + solution.get("Mates") +  "              " + solution.get("Lengua") + "              " + solution.get("Ingles")+ "              " + solution.get("Gimnasia") + "\n"
	archivo.write(frase)
	frase = "El numero de soluciones obtenidas es: " + str(numeroSoluciones) + "\n"
	archivo.write(frase)
	frase = "El tiempo de ejecucion es : " + str(tiempoEjecucion) + " Segundos "+"\n"
	archivo.write(frase)
	archivo.close()


def totalHoras(*args):
	switcher = {'Naturales':0,'Sociales':0,'Lengua':0,'Ingles':0,'Mates':0,'Gimnasia':0}
	for i in args:
		switcher[i]=switcher[i]+1;
	if switcher['Naturales'] == 2 and switcher['Sociales'] == 2 and switcher['Lengua'] == 2 and switcher['Mates'] == 2 and switcher['Ingles'] == 2 and switcher['Gimnasia'] == 1:
		return True

def naturalesSameDay(*args):
	for i in range(len(args)):
		if(args[i]=='Naturales'):
			if(i+1>=len(args) or args[i+1]!='Naturales'):
				return False
			else:
				return True
	return True

def Math_NatIngles(*args):
	hayMates = 0
	hayNaturales_o_Ingles = 0
	for i in args:
		if i == 'Mates':
			hayMates = 1
		if i=='Naturales' or i=='Ingles':
			hayNaturales_o_Ingles = 1
	if hayMates+hayNaturales_o_Ingles == 2:
			return False
	return True

def two_perTeacher(*args):
	switcher = {'Juan':0,'Andrea':0,'Lucia':0}
	for i in args:
		switcher[i] = switcher[i]+1;
	if switcher['Juan'] == 2 and switcher['Andrea'] == 2 and switcher['Lucia'] == 2:
		return True

def lucia_Sociales(*args):
	if args[0] == 'Lucia':
		if args [1] == 'Andrea':
			return True
	else:
		return True

def juan_Lun_Jue_PrimeraNaturales(*args):
	if args[0] == 'Juan' and (args[1]=='Naturales' or args[2]=='Naturales'):
		return False
	return True
def juan_Lun_Jue_PrimeraSociales(*args):
	if args[0] == 'Juan' and (args[1]=='Sociales' or args[2]=='Sociales'):
		return False
	return True
tiempoComiezo = time.time()
problem = Problem()
# Variables para el primer problema y cubro la restriccion mates solo a primera y sociales solo a segunda con el dominio
problem.addVariables(["L1","M1","X1","J1"], ['Naturales','Lengua','Mates','Ingles','Gimnasia'])
problem.addVariables(["L2","M2","X2"], ['Naturales','Lengua','Ingles','Gimnasia'])
problem.addVariables(["L3","M3","X3","J2"], ['Naturales','Sociales','Lengua','Ingles','Gimnasia'])
# Variables para el segundo problema
problem.addVariables(['Naturales','Lengua','Mates','Ingles','Gimnasia','Sociales'],['Juan', 'Andrea', 'Lucia'])
# Restricciones
problem.addConstraint(totalHoras,('L1', 'L2', 'L3','M1','M2','M3','X1','X2','X3','J1','J2'))
problem.addConstraint(naturalesSameDay, ('L1', 'L2', 'L3'))
problem.addConstraint(naturalesSameDay, ('M1', 'M2', 'M3'))
problem.addConstraint(naturalesSameDay, ('X1', 'X2', 'X3'))
problem.addConstraint(naturalesSameDay, ('J1', 'J2'))
problem.addConstraint(Math_NatIngles, ('L1', 'L2', 'L3'))
problem.addConstraint(Math_NatIngles, ('M1', 'M2', 'M3'))
problem.addConstraint(Math_NatIngles, ('X1', 'X2', 'X3'))
problem.addConstraint(Math_NatIngles, ('J1', 'J2'))
problem.addConstraint(two_perTeacher, ('Naturales','Lengua','Mates','Ingles','Gimnasia','Sociales'))
problem.addConstraint(lucia_Sociales, ('Sociales', 'Gimnasia'))
problem.addConstraint(juan_Lun_Jue_PrimeraNaturales, ('Naturales', 'L1', 'J1'))
problem.addConstraint(juan_Lun_Jue_PrimeraSociales, ('Sociales', 'L1', 'J1'))

#Solucion
solution = problem.getSolutions()
tiempoFin = time.time()
tiempoEjecucion = tiempoFin - tiempoComiezo
print("Exito, consulta los datos y una solucion en el fichero Scheduling.txt")
#------------------------------------------------SALIDA A UN ARCHIVO DE TEXTO--------------------------------
out_file(solution[0], len(solution), tiempoEjecucion)
