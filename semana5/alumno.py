""" (Programa11) alumno.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 13/02/2023
    Descripcion: Se definio la clase alumno mediante "class" y se agregaron atributos  privados y publicos      (__nombre/nombre) y se definieron metodos mediante la fucnion "def"  y la función self que es la     
    llamada a la clase
"""

class Alumno:  #  se define la clase usando pascal case
	__nombre = None  #  __nombre variable privada 

	__matricula = None  #  __matricula variable privada 

	__carrera  = None  #  __matricula variable privada 

	def __init__(self):  #  se crea una fucion de inicializacion de clase 
		print("Alumno")  #  se ejecuta este print al ejecutarse la funcion
 
	def setNombre(self,nombre):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):    #  se define una funcion para poder acceder a la variable privada 
		return self.__nombre  #  retorna el valor asigando de la variable privada

	def setMatricula(self,matricula):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__matricula = matricula  #  asigna un valor a la variable privada
	def getMatricula(self):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__matricula  #  retorna el valor asigando de la variable privada

	
	def setCarrera(self,carrera):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__carrera = carrera  #  asigna un valor a la variable privada
	def getCarrera(self):    #  se define una funcion para poder acceder a la variable privada 
		return self.__carrera  #  retorna el valor asigando de la variable privada
		

carlos = Alumno()  #  asigna a un variable una clase
carlos.setNombre("CarlosPepe")   #  llama a un objeto junto a una funcion ademas da un valor
print(carlos.getNombre())  #  imprime un objeto y llama una funcion
 
carlos.setMatricula("1722110547")  #  llama a un objeto junto a una funcion ademas da un valor
print(carlos.getMatricula())  #  imprime un objeto y llama una funcion

carlos.setCarrera("Ingenieria en gestión y mantenimiento de software")  #  llama a un objeto junto a una funcion ademas da un valor
print(carlos.getCarrera())  #  imprime un objeto y llama una funcion
