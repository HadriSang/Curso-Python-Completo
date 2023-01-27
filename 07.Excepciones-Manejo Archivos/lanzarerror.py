def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError('Error: no se puede dividir entre 0') 
        #para lanzar el error se usa el raise, y colocamos el tipo de error
    else:
        return a/b

dividir(int(input('Ingrese el divisor: ')), int(input('Ingrese el dividendo: ')))