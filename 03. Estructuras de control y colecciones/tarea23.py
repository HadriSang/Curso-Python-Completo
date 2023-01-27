n = int(input('Ingrese el numero: '))
n +=1
np = 0
ni = 0
for numeros in range(1, n):
    
    if numeros % 2 == 0:
        np += numeros
        numeros //=20
    else:
        ni += numeros

print(f'Suma de numeros pares: {np}')
print(f'Suma de numeros impares: {ni}')

