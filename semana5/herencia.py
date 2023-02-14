""" (Programa13) poo.py
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

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.nombre="Dejha Thoris"
print(objeto_persona.nombre)

objeto_alumno.nombre="John carter"
print(objeto_alumno.nombre)

objeto_alumno.email = "elpepe@gmail.com"
print(objeto_alumno.email)

print(dir(objeto_persona))  #  La funcion dir muestra una lista ordenada de los métodos y propiedades de algún objeto. 

print(dir(objeto_persona))  #  La funcion dir muestra una lista ordenada de los métodos y propiedades de algún objeto. 