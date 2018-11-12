#OPCION 1##
#python##
#coding:utf-8##
numero = int(input("Introduzca un numero "))
if(numero >= -10) and (numero <=40):
    print:("Este numero esta entre -10 y 40")
else:
    if(numero <0 ):
        print("Este numero es negativo! ")
    else:
        if(numero %2 == 0):
            print("Este numero es par :D")
        else:
            print("El numero no esta dentro de los parametros optimos .Lo sentimos.")
            
            
            
            
            
#Opcion con solo una condicion##
#Python 3.6##
#coding:utf-8##
numero = int(input("Introduzca un numero "))
if((numero >= -10) and (numero <=40))or(numero <0 )or(numero %2 == 0):
    print:("Este numero esta entre -10 y 40 o es negativo o es un numero par")
else:
    print("El numero no esta dentro de los parametros optimos .Lo sentimos.")
