n1 = int(input('Ingrese el Primer numero: '))
n2 = int(input('Ingrese el Segundo numero: '))

# V1
# if n1> n2:
#     print(f'el numero {n1} es mayor')
# else:
#     print(f'Eñ numero {n2} es mayor')

if n1> n2:
    print(f'El primer numero: {n1} es mayor')
elif n2>n1: 
 print(f'El Segundo numero: {n2} es mayor')
else:
    print(f'el numero 1: {n1} y el numero 2: {n2} son iguales')