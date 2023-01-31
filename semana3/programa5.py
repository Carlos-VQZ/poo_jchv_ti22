""" Programa5
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 30/01/2023
    Descripcion: Programa para calcular area y perimetro de un triangulo cualquiera"""

ladoa = float(input("Escribe el lado base: "))  #  funcion imput para introducir y casteo para introducir datos tipo float
ladob = float(input("Escribe el segundo lado: "))  #  funcion imput para introducir y casteo para introducir datos tipo float
ladoc = float(input("Escribe el tercer lado: "))  #  funcion imput para introducir y casteo para introducir datos tipo float

perimetro = (ladoa+ladob+ladoc)  #  calculo de perimetro de un triangulo
print("El perímetro es: ",perimetro," cm")  #  funcion print en la cual se imprime el resultado del perimetro
altura = float(input("Escribe la altura : "))  #  funcion print en la cual se imprime el resultado del area
area = (ladoa*altura/2)  #  calculo de perimetro de un triangulo
print("El area es: " ,area," cm2")  #  funcion print en la cual se imprime el resultado del area