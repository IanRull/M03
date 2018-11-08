#coding:utf-8
# Comparador de fechas ##
anyo_actual = int(input("Que año es actualmente?"))
anyo_random = int(input("Ponga un año aleatorio:"))
if(anyo_actual == 0 and anyo_random == 0):
    print("No pueden ser 0 los años")
else:
    if(anyo_actual == anyo_random):
        print(" Son el mismo año! ")
    else:
        if(anyo_actual == 0):
            print("Error: el año actual no puede ser igual a cero")
        else:
            if(anyo_random == 0):
                print("Error: el año aleatorio no puede ser igual a 0")
            else:
                if(anyo_actual < anyo_random):
                    print(" Hasta llegar a ",anyo_random," aun faltan ",(anyo_random - anyo_actual)," años ")
                else:
                    if(anyo_random < anyo_actual):
                        print(" Desde el año " ,anyo_random, " hasta ",anyo_actual," han pasado ",(anyo_actual - anyo_random ),)
       
