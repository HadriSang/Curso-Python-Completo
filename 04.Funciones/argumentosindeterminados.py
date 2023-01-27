def sumar(*args, **kwargs): #el asterisco es para declarar argumentos indefinidos por posicion
# el nombre args puede ser cualquiera pero es lo mas comun de usar
# para declarar argumentos indefinidos con cualquier nombre se usa el 
# doble ** y es comun usar kwargs
    suma=0
    for n in args:
        suma +=n
    return suma, kwargs
 
#Los argumentos por posicion se convierten en tupla 
# y los argumentos por nombres se convierten en dicciionarios
suma_total,datos= sumar(1,2,3,4,5, nombre='hello', edad= 'world')
print('La suma total es: ', suma_total)

print(datos)