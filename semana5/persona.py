""" (Programa13) persona.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 13/02/2023
    Descripcion: Se definio la clase alumno  mediante "class" y se agregaron atributos 
    privados y publicos (__nombre/nombre) y se definieron metodos mediante la fucnion "def"  
    y la función self que es la llamada a la clase
"""


class Persona:    #  se define la clase usando pascal case
	__nombre = None  #__nombre variable privada 
	__email = None  #__clase variable privada
	def __init__(self):  #  se crea una fucion de inicializacion de clase 
		print("Persona")  #  se ejecuta este print al ejecutarse la funcion
	def setNombre(self,nombre):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__nombre  #  asigna un valor a la variable privada

	def setEmail(self,email):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__email = email  #  asigna un valor a la variable privada
	def getEmail(self):   #  se define una funcion para poder acceder a la variable privada
		return self.__email  #  retorna el valor asigando de la variable privada
		
	
dejha = Persona()  #  asigna a un variable una clase
dejha.setNombre("Dejha")  #  llama a un objeto junto a una funcion ademas da un valor
print(dejha.getNombre())  #  imprime un objeto y llama una funcion
dejha.setEmail("dejha@utec.edu.mx")  #  llama a un objeto junto a una funcion ademas da un valor
print(dejha.getEmail())  #  imprime un objeto y el objeto llama una funcion
