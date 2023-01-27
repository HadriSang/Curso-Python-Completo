import random
par = []
impar = []
tup1 = (1,2,3,4,5,6,7,8,9)

for t in tup1:

 valr = random.randint(1,100)
 r = t * valr
 if r % 2 == 0:
    print(f'El resultado de {t} x {valr} es {r} Que es un numero par')
    par.append(r)
 else:
    print(f'El resultado de {t} x {valr} es {r} Que es un numero impar')

    impar.append(r)

print(f'La lista de resultados pares es: {par}')

print(f'La lista de resultados impares es: {impar}')