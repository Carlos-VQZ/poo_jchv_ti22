""" Programa10
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 08/02/2023
    Descripcion:Comparar 2 numeros enteros en 
    imprimir el numero mayor mediante 
    Definiciones de la forma pythonic
"""

def mayor(numero1:int , numero2:int)->int:  #  Define la funcion "mayor" en la cual hay 2 variables las cuales son declaradas de tipo entero
    mayor = None  #  Se asigna el valor None a mayor
    if numero1>numero2:  #  Concidion "if" que compara 2 variables
        mayor = numero1  #  si la condicion "if" es verdadera se asinga el valor de numero1 a la variable mayor
    elif numero2>numero1:  #  si la condicion "if" es falsa se ejecuta "elif", la cual asinga el valor de numero2 a la variable mayor
        mayor = numero2
    else:  #  si ambas condiciones "if" y "elif" son falsas se ejecuta "else"
        mayor = None  #  Se le asigna "None" a la variable mayor
    return mayor  #  regresa a la funcion mayor 

print(mayor(3,2))  #  Llamada a la definicion mayor, la cual se imprime el resultado de la definicion 
print(mayor(2,3))  #  Llamada a la definicion mayor, la cual se imprime el resultado de la definicion 
print(mayor(3,3))  #  Llamada a la definicion mayor, la cual se imprime el resultado de la definicion 