""" Programa4
    Nombre: Juan Carlos Hernandez Vazquez
    Fecha: 30/01/2023
    Descripcion: Programa para calcular area y perimetro de un triangulo cualquiera"""

ladoa = float(input("Escribe el lado base: "))
ladob = float(input("Escribe el segundo lado: "))
ladoc = float(input("Escribe el tercer lado: "))

perimetro = (ladoa+ladob+ladoc)
print("El perimetro es: ",perimetro)
 
altura = float(input("Escribe la altura : "))
area = (ladoa*altura/2)
print("El area es: " ,area)