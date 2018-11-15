#coding:utf-8
# Comparador de numeros##
print("Buenas, aqui puedes comparar entre 2 numeros cual es el mas grande :D")
numero1 = int(input("Ponga un numero"))
numero2 = int(input("Ponga un numero :"))
if(numero1 == 0 and numero2 == 0):
    print("No pueden ser 0 los numeros")
else:
    if(numero1 == numero2)or(numero2 == numero1):
        print(" Son el mismo numero! ")
    else:
        if(numero1 == 0):
            print(numero2," ,este es el mas grande")
        else:
            if(numero2 == 0):
                print(numero2," ,este es el mas grande")
            else:
                if(numero1 < numero2):
                    print("el" ,numero2,"es el mas grande")
                else:
                    if(numero1 > numero2):
                        print("el" ,numero1,"es el mas grande")
