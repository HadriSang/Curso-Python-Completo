t= int(input('Ingrese la cantidad de tiempo en segundos: '))
m = t / 60
h= t/3600
print(f'{t} segundos en minutos es igual a: {m}')
print(f'{t} segundos en horas es igual a: {h}')

t= int(input('Ingrese la cantidad de tiempo en minutos: '))
s = t * 60
h= t/60
print(f'{t} minutos en segundos es igual a: {s}')
print(f'{t} minutos en horas es igual a: {h}')






# SOUUCION PROFESOR


# # Variables / Ingresar Datos
# tiempoSegundos = input('Tiempo en Segundos: ')
# HORA = 3600
# MINUTO = 60

# # Convertir de str a int
# tiempoSegundos = int(tiempoSegundos)

# # Solución 
# h = tiempoSegundos // HORA
# tiempoSegundos = tiempoSegundos % HORA
# m = tiempoSegundos // MINUTO
# s = tiempoSegundos % MINUTO

# # Mostrar datos en pantalla 
# print('Horas: ', h)
# print('Minutos: ', m)
# print('Segundos: ', s)