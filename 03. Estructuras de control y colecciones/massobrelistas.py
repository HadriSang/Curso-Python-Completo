datos = ['hello', 'world', 2023]

datos.extend(datos) #lo que hace es combinar la lista con otra

print(datos)

datos.insert(0, 100) # aca el insert sirve para ingresar el dato
# donde el primer dato es la posicion y el segundo es el dato o valor a ingresar

datos.remove(100) #sirve para remover el elemnto de la lista

datos.pop() #Elimina el ultimo elemento de la lista

datos.clear() #Elimina todos los elementos de la lista

datos.index('world')# te devuelve la posicion del dato

datos.count('world') #Te devuelve la cantidad de los valores iguales a lo de dentro de los parencesis

datos.sort() #sirve para ordenar las listas a a z 

datos.reverse() #Invierte los datos de la lista

datos.copy()#copia la lista