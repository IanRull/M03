#V1.1##
#coding:utf-8##
numero = int(input("Ponga un numero:"))
if(numero >= 0):
    print("Es positivo")
else:
    print("Es negativo")
#V1.2##
###########################################################################################
#                                     JOC DE PROVES                                       #                                                #
#              ENTRADA                                                SORTIDA             #                                                                  #
#                 3                                                  'POSITIU'            #
#                -2                                                  'NEGATIU'            #       
#                 0                                                  'POSITIU'            #       
#                                                                                         #
#                                                                                         #
###########################################################################################

#coding:utf-8##
numero = int(input("Ponga un numero:"))
if(numero ==0):
    print("Es positivo")
elif(numero > 0):
    print("Es negativo")
else:
    print("Es positivo")
         
        
#V1.3##
###########################################################################################
#                                     JOC DE PROVES                                       #                                                #
#              ENTRADA                                                SORTIDA             #                                                                  #
#                 1  8      7                                          1      8         #
#                -2  -3     4                                           -3    -2         #       
#                 7   0    0                                            0      7         #       
#                 0   0   0                                            0      0         #
#                                                                                         #
###########################################################################################
#coding:utf-8##
numeros=list(eval(input("Posa tres numeros separats per comes: ")))
numeros.sort()
print(numeros)

