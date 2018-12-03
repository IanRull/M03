VERSION SIN ACABAR



#python 3.6#i#
#coding:utf-8#a#
#Gasolinera#n#
print('Buenos dias')
opcion = int(input('si desea comprar gasolina normal ponga 1, ponga 2 si quiere diesel y 3 si quiere sin plomo :'))
if(opcion == 1):
    print('Has escohido gasolina normal')
    mega = 1,18
    ocho = 1,4
    opcion1 =int(input('Pulse 1 para la megafast que son 1,18 y pulse 2 para la 98 que son 1,4'))
    litros1 =int(input('Ponga los litros que quiere : '))
    if(opcion1 == 1):
        print(nove*litros1)
elif(opcion == 2):
    print('Has escohido  diesel')
    normal = 1,19
    eplus = 1,4
    opcion2 =int(input('Pulse 1 para diesel normal que son 1,19 y  pulse 2 si quiere eplus que son : 1,4'))
    litros2 =int(input('Ponga los litros que quiere : '))
    if(opcion2 == 1):
        print(nove*litros2)
elif(opcion == 3):
    print('Has escohido sin plomo')
    nove = 1,5
    extra = 1,4
    opcion3 =int(input('Pulse 1 si quiere 95 que son: 1,5 y 2 si quiere extraplus que son 1,4'))
    litros3 =int(input('Ponga los litros que quiere : '))
    if(opcion3 == 1):
        print(nove*litros3)
