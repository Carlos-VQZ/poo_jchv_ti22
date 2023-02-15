from persona import Persona  #  Importa la clase persona del archivo persona.py

class Alumno(Persona):  #  Crea la clase Alumno que hereda la clase Persona
    def __init__(self)-> None:  #  Constructor de la clase
        super().__init__()  #  Llama al constructor de la clase
        print("Alumno")  #  Imprime el texto Alumno

objeto_alumno = Alumno()  #  crea un objeto de la clase Alumno