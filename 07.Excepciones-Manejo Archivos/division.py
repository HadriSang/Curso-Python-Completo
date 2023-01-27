divi = 0
try:
 a =int(input('Ingrese el dividendo: '))
 b =int(input('Ingrese el divisor: '))
 divi = a/ b
except ZeroDivisionError:
    print('No se puede dividir entre 0') # aca al colocar el tipo de error al momento de que aparezca mostrara un mensaje especifico para este
except ValueError:
    print('Ingrese valores numericos')
except Exception as error: # aca capturamos el error  en la variable error para impirmirla despues
    print('A ocurrido un error', type(error).__name__) #El __name__ se puede usar para extraer el nombre de una clase o en este caso de un error

print('La division es: ', divi)