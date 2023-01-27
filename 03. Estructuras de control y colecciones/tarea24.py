n = int(input('Ingrese el numero: '))

sum = 0

for numeros in range(1,n):
    if n % numeros == 0:
     sum+= numeros

if n == sum:
    print(f'El numero {n} es perfecto')
else:
    print(f'El numero {n} no es perfecto')