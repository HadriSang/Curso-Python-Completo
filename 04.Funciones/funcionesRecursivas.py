# Se considera una funcion recursiva por que se usa dentro de si misma
# para su correcta ejecucion
def factorial(n):
    print(f'Valor inicial -->{n}')
    if  n >1:

        n= n* factorial(n-1)
    print(f'valor final ..>{n}')
    return n

f = factorial(int(input('ingrese numero: ')))
print(f'Su factorial es: {f}')