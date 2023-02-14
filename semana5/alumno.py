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
		

carlos = Alumno() 
carlos.setNombre("CarlosPepe")
print(carlos.getNombre())
 
carlos.setMatricula("1722110547")
print(carlos.getMatricula())

carlos.setCarrera("Ingenieria en gestión y mantenimiento de software")
print(carlos.getCarrera())
