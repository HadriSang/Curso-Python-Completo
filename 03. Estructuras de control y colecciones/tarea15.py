def numLetras():
    i = True
    
    while i == True:
     n = int(input('Ingrese un numero del 0 al 9: '))
     if n >= 0 and n <= 9:
        if n == 0:
            print(f'El numero {n} es CERO')
            i = False 
        elif n == 1:
            print(f'El numero {n} es UNO') 
            i = False 
        elif n == 2:
            print(f'El numero {n} es DOS')
            i = False 
        elif n == 3:
            print(f'El numero {n} es TRES') 
            i = False 
        elif n == 4:
            print(f'El numero {n} es CUATRO') 
            i = False 
        elif n == 5:
            print(f'El numero {n} es CINCO')
            i = False 
        elif n == 6:
            print(f'El numero {n} es SEIS') 
            i = False     
        elif n == 7:
            print(f'El numero {n} es SIETE') 
            i = False 
        elif n == 8:
            print(f'El numero {n} es OCHO')
            i = False   
        elif n == 9:
            print(f'El numero {n} es NUEVE')  
            i = False 
     else:
        i = True
        print('Ingrese un numero Valido')

numLetras()


# SOLUCION DE UN ALUMNO; TENER EN CUENTA Y ANALIZAR 
# A LA HORA DE AHORRAR RECURSOS

# numeros = {

#     '1':'UNO',

#     '2':'DOS',

#     '3':'TRES',

#     '4':'CUATRO',

#     '5':'CINCO',

#     '6':'SEIS',

#     '7':'SIETE',

#     '8':'OCHO',

#     '9':'NUEVE'

# }



# numero = input("Ingrese el numero del 0-9: ")

# print(numeros.get(numero))