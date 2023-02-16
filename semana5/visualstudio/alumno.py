""" (Programa12) alumno.py
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 13/02/2023
    Descripcion: Se definio la clase alumno           mediante "class" y se agregaron atributos         privados y publicos (__nombre/nombre) y se        definieron metodos mediante la fucnion "def"      y la función self que es la llamada a la clase
"""


from persona import Persona  #  Importa la clase persona del archivo persona.py

class Alumno(Persona):  #  Crea la clase Alumno que hereda la clase Persona
    def __init__(self)-> None:  #  Constructor de la clase
        super().__init__()  #  Llama al constructor de la clase
        print("Alumno")  #  Imprime el texto Alumno

objeto_alumno = Alumno()  #  crea un objeto de la clase Alumno