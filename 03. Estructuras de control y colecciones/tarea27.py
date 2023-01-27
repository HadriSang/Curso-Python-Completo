
n1 = int(input(' Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))
mul = int(input('Ingresa el multiplos: '))
n2 += 1
cant = 0
for numeros in range(n1,n2):
    if numeros % mul == 0:
     cant += 1
print(f'La cantidad de multiplos es: {cant}')