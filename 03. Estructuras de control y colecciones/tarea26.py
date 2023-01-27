ni = int(input('Ingrese el numero inicial: '))
nf = int(input('Ingrese el numero final: '))
nf +=1
contPos=0
contNeg=0

for numeros in range(ni, nf):
    if numeros > 0:
        contPos += 1
    elif numeros < 0:
        contNeg += 1

print(f'La cantidad de mueros Positivos es: {contPos}')
print(f'La cantidad de mueros Negativos es: {contNeg}')

