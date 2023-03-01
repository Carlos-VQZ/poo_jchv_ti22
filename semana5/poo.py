""" (Programa14) poo.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 14/02/2023
    Descripcion:En este programa se observa las caracteristicas de la programacion orientada a objetos
"""

class Persona:    #  crea la clase Persona
	__nombre = None  #  se crea lavariable privada 
	__edad = None  #  se crea la variable privada
	def __init__(self):  #  Constructor incial de la clase Persona
		print("Persona")  #  Imprime el el texto Persona
        
    def setNombre(self,nombre):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__nombre  #  retorna el valor a de la variable privada

    def setEdad(self,edad):    #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__edad = edad  #  asigna un valor a la variable privada
	def getEdad(self):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		return self.__edad  #  retorna el valor de la variable privada


class Alumno(Persona):  #  crea la clase Alumno que hereda atrubutos de la clase Persona
	__nombre = None  #  se crea lavariable privada
	__matricula = None  #  se crea lavariable privada
	
	def __init__(self):  #  hace referencia a la clase / llamada a la clase
		super().__init__()  #  hace una llamada a la super clase ej. "alumno(persona)
		print("Alumno")  #  Imprime el el texto Alumno

    def setNombre(self,nombre):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):    #  se define una funcion para poder acceder a la variable privada y obtener su valor
		return self.__nombre  #  retorna el valor asigando de la variable privada

	def setMatricula(self,matricula):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__matricula = matricula  #  asigna un valor a la variable privada
	def getMatricula(self):    #  se define una funcion para poder acceder a la variable privada y obtener valor
		return self.__matricula  #  retorna el valor asigando de la variable privada


class Profesor(Persona):  #  crea la clase Profesor que hereda atrubutos de la clase Persona
    __nonomina = None  #  se crea la variable privada
    def __init__(self):  #  hace referencia a la clase / llamada a la clase
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Profesor")   #  Imprime el el texto Profesor

    def def setNonomina(self,nonomina):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__Nonomina = nonomina  #  asigna un valor a la variable privada
	def getNonomina(self):    #  se define una funcion para poder acceder a la variable privada y obtener su valor
		return self.__nonomina  #  retorna el valor asigando de la variable privada
        
class Coordinador(Persona):
    __nomina = None  #  se crea lavariable privada 
    __carreracordinada = None  #  se crea lavariable privada 
    def ___init__(self):  #  hace referencia a la clase / llamada a la clase
        super().__init__()  #  accede a otras clases mediante la funcion super 
            print(Cordinador)   #  Imprime el el texto Coordinador
    
    def setNomina(self,nomina):  #  se define una funcion para poder acceder a la variable privada y darle un valor
		self.__nomina = nonomina  #  asigna un valor a la variable privada
	def getNomina(self):    #  se define una funcion para poder acceder a la variable privada y obtener su valor
		return self.__nomina  #  retorna el valor asigando de la variable privada

    def setCarreracordinada(self,carreracordinada):  #  se define una funcion para poder acceder a la variable privada y darle un valor
        self.__carreracordinada = carreracordinada  #  asigna un valor a la variable privada
    def getCarreracordinada(self):  #  se define una funcion para poder acceder a la variable privada y obtener su valor
        return self.__carreracordinada  #  retorna el valor asigando de la variable privada


objeto_persona = Persona()  #  asigna a un variable una clase  
objeto_alumno = Alumno()  #  asigna a un variable una clase
objeto_profesor = Profesor()   #  asigna a un variable una clase  
objeto_cordinador = Coordinador()  #  asigna a un variable una clase  