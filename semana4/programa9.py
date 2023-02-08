""" Programa9
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 08/02/2023
    Descripcion:Comparar dos numeros enteros 
    e imprimir el numero mayor mediante 
    definiciones"""

def mayor(numero1,numero2):  #  Define la funcion "mayor" en la cual hay 2 variables
    if numero1>numero2:  #  funciion if para realizar la condicion > que
        print(numero1)  #  con la funcion print se imprime este proceso si es verdadera
    elif numero2>numero1:  #  funciion elif para realizar otra condicion > que si if fue falsa
        print(numero1)  #  con la funcion print se imprime este proceso si elif es verdadera
    else:  #  Si la funcion if y elif es falsa se ejecuta la condicion else
        print("iguales")  #  proceso que se ejecuta si ambas condiciones if y elif son falsas

mayor(3,2)  #  LLamada a la definición mayor el resultado es:3
mayor(2,3)  #  LLamada a la definición mayor el resultado es:3
mayor(3,3)  #  LLamada a la definición mayor el resultado es:none
