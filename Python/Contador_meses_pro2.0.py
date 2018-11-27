#python 3.6#i#
#coding:utf-8#a#
#Contador meses#n#
anyo = str(input('Indique poniendo :normal: si es un año no bisiesto y ponga bisiesto si lo es :'))
if(anyo.lower() == 'normal')or(anyo.lower() == 'bisiesto'):
    if(anyo.lower() == 'normal'):
        for x in range(0,30):
            print(x + 1)
        if(x > 0)and((x +1 )<= 30):
            print('ENERO')
        for x in range(30 ,59):
            print(x + +1)
        if(x > 30)and((x +1 )<= 59):
            print('FEBRERO')
        for x in range(59 ,90):
            print(x + 1)
        if(x > 59)and((x +1 )<= 90):
            print('MARZO')
        for x in range(90 ,120):
            print(x + 1)
        if(x > 90)and((x +1 )<= 120):
            print('ABRIL')
        for x in range(120 ,151):
            print(x + 1)
        if(x > 120)and(x <= 151):
            print('MAYO')
        for x in range(151 ,181):
            print(x + 1)
        if(x > 151)and(x <= 181):
            print('JUNIO')
        for x in range(181 ,212):
            print(x + 1)
        if(x > 181)and(x <= 212):
            print('JULIO')
        for x in range(212 ,243):
            print(x + 1)
        if(x > 212)and(x <= 243):
            print('AGOSTO')
        for x in range(243 ,273):
            print(x + 1)
        if(x > 243)and(x <= 273):
            print('SEPTIEMBRE')
        for x in range(273 ,304):
            print(x + 1)
        if(x > 273)and(x <= 304):
            print('OCTUBRE')
        for x in range(304 ,334):
            print(x + 1)
        if(x > 304)and(x <= 334):
            print('NOVIEMBRE')
        for x in range(334 ,365):
            print(x + 1)
        if(x > 334)and(x <= 365):
            print('DICIEMBRE')  
    elif(anyo.lower() == 'bisiesto'):
        for x in range(0,30):
            print(x + 1)
        if(x > 0)and((x +1 )<= 30):
            print('ENERO')
        for x in range(30 ,59):
            print(x + +1)
        if(x > 30)and((x +1 )<= 59):
            print('FEBRERO')
        for x in range(59 ,91):
            print(x + 1)
        if(x > 59)and((x +1 )<= 91):
            print('MARZO')
        for x in range(91 ,121):
            print(x + 1)
        if(x > 91)and((x +1 )<= 121):
            print('ABRIL')
        for x in range(121 ,152):
            print(x + 1)
        if(x > 121)and(x <= 152):
            print('MAYO')
        for x in range(152 ,182):
            print(x + 1)
        if(x > 152)and(x <= 182):
            print('JUNIO')
        for x in range(182 ,213):
            print(x + 1)
        if(x > 182)and(x <= 213):
            print('JULIO')
        for x in range(213 ,244):
            print(x + 1)
        if(x > 213)and(x <= 244):
            print('AGOSTO')
        for x in range(244 ,274):
            print(x + 1)
        if(x > 244)and(x <= 274):
            print('SEPTIEMBRE')
        for x in range(274 ,305):
            print(x + 1)
        if(x > 274)and(x <= 305):
            print('OCTUBRE')
        for x in range(305 ,335):
            print(x + 1)
        if(x > 305)and(x <= 335):
            print('NOVIEMBRE')
        for x in range(335 ,366):
            print(x + 1)
        if(x > 334)and(x <= 365):
            print('DICIEMBRE')
else:
    print('Te equivocaste en poner el nombre :|')
    
