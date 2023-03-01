""" (Programa12) poo.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 14/02/2023
    Descripcion:En este programa se observa las caracteristica herencia en programacion orientada objetos
"""
class Persona:  #  se define la clase usando pascal case
	__nombre = None  # se crean variables privadas
	__email = None  # se crean variables privadas
	def __init__(self):    #  se crea una fucion de inicializacion de clase 
		print("Persona")  #  se ejecuta este print al ejecutarse la funcion

class Alumno(Persona):
	__nombre = None
	__matricula = None
	__carrera = None 
	def __init__(self):  #  hace referencia a la clase / llamada a la clase
		super().__init__()  #  hace una llamada a la super clase ej. "alumno(persona)
		print("Alumno")

objeto_persona = Persona()  #  asigna a un variable una clase  
objeto_alumno = Alumno()  #  asigna a un variable una clase  

objeto_persona.nombre="Dejha Thoris"  #  asigna una valor a una variable de una clase
print(objeto_persona.nombre)  #  imprime el valor de una varibale de una clase

objeto_alumno.nombre="John carter"  #  asigna una valor a una variable de una clase
print(objeto_alumno.nombre)   #  imprime el valor de una varibale de una clase

objeto_alumno.email = "elpepe@gmail.com"  #  asigna una valor a una variable de una clase
print(objeto_alumno.email)  #  imprime el valor de una varibale de una clase

print(dir(objeto_persona))  #  La funcion dir muestra una lista ordenada de los métodos y propiedades de algún objeto. 

print(dir(objeto_persona))  #  La funcion dir muestra una lista ordenada de los métodos y propiedades de algún objeto. 