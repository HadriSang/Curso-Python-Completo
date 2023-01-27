# para definir los parametros requeridos para la ejecucion del metodo
# se realiza dentro de los parentesis del def
def retorno(nombre):

    saludo = 'hola como estas'
    return f'{saludo},{nombre}'

# aca estamos solocitando el valor del parametro nombre y el return 
# se almacena en la variable saludo


saludo = retorno(input('ingrese su nombre por favor: ')) 

# aca imprime el return
print(saludo)


def sumar(a,b): #los argumentos son los datos que se envian a los parametros
    return a+b

suma = sumar(int(input('ingrese el primer numero: ')), int(input('ingrese el segundo numero: ')))
print(f'La suma es: {suma}')

def restar(a=None,b=None): #tambien en esete caso se pueden colocar valores por defecto, en este caso none
    if b == None or a == None:
        print('Error debe ingresar un numero valido')
        return
    return a-b

# tambien se puede especificar los valores a los cuales
# se les quiere asignar un argumanto

resta = restar( b=10,a=40)
print(f'La resta es: {resta}')