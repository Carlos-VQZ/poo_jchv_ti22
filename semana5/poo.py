""" (Programa14) poo.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 14/02/2023
    Descripcion:En este programa se observa las caracteristicas de la programacion orientada a objetos
"""

class Persona:
	__nombre = None
	__edad = None
	def __init__(self): 
		print("Persona")
        
    def setNombre(self,nombre):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__nombre  #  retorna el valor a de la variable privada

    def setEdad(self,edad):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__edad = edad  #  asigna un valor a la variable privada
	def getEdad(self):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__edad  #  retorna el valor de la variable privada


class Alumno(Persona):
	__nombre = None
	__matricula = None
	
	def __init__(self):  #  hace referencia a la clase / llamada a la clase
		super().__init__()  #  hace una llamada a la super clase ej. "alumno(persona)
		print("Alumno")

    def setNombre(self,nombre):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):    #  se define una funcion para poder acceder a la variable privada 
		return self.__nombre  #  retorna el valor asigando de la variable privada

	def setMatricula(self,matricula):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__matricula = matricula  #  asigna un valor a la variable privada
	def getMatricula(self):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__matricula  #  retorna el valor asigando de la variable privada


class Profesor(Persona):
    __nonomina = None
    def __init__(self):  # 
        print("Profesor")

    def def setNonomina(self,nonomina):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__Nonomina = nonomina  #  asigna un valor a la variable privada
	def getNonomina(self):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__nonomina  #  retorna el valor asigando de la variable privada
        
class Coordinador(Persona):
    __nomina = None
    __carreracordinada = None
    def ___init__(self):
            print(Cordinador)
    
    def setNomina(self,nomina):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nomina = nonomina  #  asigna un valor a la variable privada
	def getNomina(self):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__nomina  #  retorna el valor asigando de la variable privada

    def setCarreracordinada(self,carreracordinada):
        self.__carreracordinada = carreracordinada
    def getCarreracordinada(self):
        return self.__carreracordinada

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.nombre="Dejha Thoris"
print(objeto_persona.nombre)

objeto_alumno.nombre="John carter"
print(objeto_alumno.nombre)

objeto_alumno.email = "elpepe@gmail.com"
print(objeto_alumno.email)

print(dir(objeto_persona))  #  La funcion dir muestra una lista ordenada de los métodos y propiedades de algún objeto. 

print(dir(objeto_persona))