def tarea():
    n= int(input('Ingrese el Numero entero: '))

    if n<=0:
        print('Ingrese un numero Mayor que 0')
    elif n%2 ==0:
        n *=2
        print(f'Es Par, se Devuelve el Doble: {n}')
    else:
        n*=3
        print(f'Es Impar, se Devuelve el Triple: {n}')

tarea()
