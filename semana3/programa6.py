""" Programa6
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 31/01/2023
    Descripcion: Programa para calcular area y perimetro de un circulo"""

print("Calcular el perimetro y area de un circulo en centimetros")  
radio = float(input("Ingrese el radio del circulo: "))    #  funcion imput para introducir y casteo para introducir datos 
diametro = 2*radio   #   Calculo del area del circulo
pi = 3.1416  #  Declaracón de la funcion PI
perimetro = (pi*diametro)  #  calculo de perimetro del circulo
print("El perimetro es: ",perimetro)  #  funcion print para imprimir el calculo de perimetro 
area = (pi*(radio**2))  #  Calculo del area del circulo
print("El area es: ",area)  #  Funcion print para imprimir el calculo del area del circulo

print("calcular el perimetro y area de un cuadrado en centimertros")  #  Función print para imprimi el titulo
lados = float(input("Escribe la medida de los lados : "))  #  funcion imput para introducir y casteo para introducir datos 
cuadradoperimetro = (lados+lados+lados+lados)  #  calculo de perimetro del cuadrado
cuadradoarea = (lados*lados)  #  calculo de area del circulo
print("El perimetro es:",cuadradoperimetro," cm")  #  Funcion print para imprimir el calculo del perimetro del cuadrado
print("El area es:",cuadradoarea," cm2")  #  Funcion print para imprimir el calculo del area del cuadrado





