print('Suma de dos numeros')

# Entrada de datos
'''
n1 = input('Ingresa el primer numero: ')
n2= input('Ingrese el segundo numero: ')
resultado = n1 + n2
print('El resultado es: ' + resultado)
'''

# aca mostrara el resultado con error, debido a que al ingresar un 
# dato por input es String entonces toca cambiar el dato a numerico

n1 = input('Ingresa el primer numero: ')
n2= input('Ingrese el segundo numero: ')
# Para realizar la conversion se llama al tipo de dato
# y se transforma la variable
n1 = int(n1)
n2 = int(n2)
resultado = n1 + n2
print('El resultado es: ', resultado)

# Lo mismo se haria con int, float y string

# tambien se podria definir directamente en el input
# n1 = int(input('Ingresa el primer numero: '))
# n2= int(input('Ingrese el segundo numero: '))