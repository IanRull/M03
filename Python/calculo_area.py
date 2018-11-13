#Python 3.6##
#coding:utf-8##
opcion = str(input("Introduzca C si quiere calcular el area de un circulo y T si quiere calcular el area de un triangulo : "))
if(opcion == "C"):
    radio = int(input("Introduzca el radio de su circulo :"))
    area = (3.1415*(radio*radio))
    print("El area de tu circulo es: ",area)
elif(opcion == "T"):
    base = int(input("Digame la base de el triangulo : "))
    altura = int(input("Digame la altura del triangulo : "))
    areatri = (base*altura/2)
    print("El area de tu triangulo es :",areatri)
else:
    print("Te has equivocado")
