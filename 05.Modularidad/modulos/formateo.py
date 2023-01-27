from sys import argv
if len(argv)==4:
 nombre = argv[1]
 edad = int(argv[2])
 altura = float(argv[3])
#  Otra forma de formatear  a la hora de imprimir es:
#  print('Nombre {} \nEdad: {} \nAltura: {}'.format(nombre,edad,altura))
# # donde despues del format se coloca en el orden 

# # Otra manera es definiendo variables y despues colocarlas en el nombre
#  print('Nombre {n} \nEdad: {e} \nAltura: {a}'.format(n=nombre,e=edad,a=altura))
# Esta era la version antigua de formatear donde se definen con las 
# letras el tipo de dato que ingresa
 print('Nombr: %s \nEdad: %i \nAltura: %f'%(nombre,edad,altura))


else:
    print('Eror ingrese los datos correctamente')
    print('Ejemplo: formateo.py "nombre" 25 1.67')