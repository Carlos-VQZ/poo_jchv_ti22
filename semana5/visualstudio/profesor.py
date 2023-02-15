from persona import Persona  #  Importa la clase persona del archivo persona.py

class Profesor(Persona):  #  Crea la clase Profesor que hereda la clase Persona
    def __init__(self) -> None: #  Constructor de la clase
        super().__init__()  #  Llama al constructor de la clase
        print("Profesor")  #  Imprime el texto Profesor

objeto_profesor = Profesor()  #  crea un objeto de la clase Profesor