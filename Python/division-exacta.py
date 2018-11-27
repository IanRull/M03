#python 3.6##
#coding:utf-8##
#division_exacta.py##
dividen = int(input('Escriba el dividendo: '))
divis = int(input('Escriba el divisor: '))
if (dividen == 0)or(divis == 0):
        print('Cabia el numero, el cero no vale,podrias crear un bucle que destruiria el universo. ')
else:
    modulo = dividen%divis
    print('La division es :',dividen/divis)
    print(modulo)
    if(modulo == 0):
        print('Es exacta :D')
    else:
        print('No es exacta')
