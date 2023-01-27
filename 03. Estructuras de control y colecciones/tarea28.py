# numeros = []

# numeros.append(int(input('Ingrese el Primer numero: ')))
# numeros.append(int(input('Ingrese el Segundo numero: ')))
# numeros.append(int(input('Ingrese el Tercer numero: ')))
# numeros.append(int(input('Ingrese el Cuarto numero: ')))
# numeros.append(int(input('Ingrese el Quinto numero: ')))
# numeros.append(int(input('Ingrese el Sexto numero: ')))

# numeros.sort()
# print(f'El numero menor es {numeros[0]}')
# print(f'El numero mayor es {numeros[5]}')

def numMM():
    numeros=[]
    cont = 0
    while cont < 6:
      cont += 1
      numeros.append(int(input(f'Ingrese el numero {cont}:')))
    numeros.sort()
    print(f'El numero menor es {numeros[0]}')
    print(f'El numero mayor es {numeros[5]}')
numMM()

