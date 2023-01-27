 
def numMayor():
     n1 = int(input('Ingrese el Numero 1: '))
     n2 = int(input('Ingrese el Numero 2: '))
     n3 = int(input('Ingrese el Numero 3: '))

     if n1 > n2 and n1> n3:
        print(f'El numero 1 {n1} es mayor')
     elif n2 > n1 and n2> n3:
         print(f'El numero 2 {n2} es mayor')    
     elif n3 > n1 and n3> n2:
         print(f'El numero 3 {n3} es mayor')
     else:
          print('2 Numeros o mas son iguales')


numMayor()

def solProf():
 numero1 = int(input('Número 1: '))
 numero2 = int(input('Número 2: '))
 numero3 = int(input('Número 3: '))

 # Solución

 if numero1 > numero2:
     if numero1 > numero3:
        mayor = numero1
     else:
        mayor = numero3
 else:
     if numero2 > numero3:
        mayor = numero2
     else:
         mayor = numero3

# Mostrar Datos45 
 print(f'MAYOR: {mayor}')

solProf()