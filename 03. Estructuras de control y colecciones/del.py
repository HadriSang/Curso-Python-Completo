# la instruccion del se usa para eliminar elementos de una lista  o diccionario
# tambien se usa para borrar todo lo que este dentro

list = ['a','b','c','d']

del list[0] #esto lo que haria seria borrar el elemento a
list = ['a','b','c','d']

del list[:3] # esto borraria desde el 0= a jasta 2 = c dejando solo 3 = d

del list[:]#Borra todo

del a # no solo borra lo que esta dentro de la lista si no que tambien 
# borra la variable declarada

d= {'uno':1,'dos':2,'tres':3}
del d['dos'] # me borra el elemento con nombre dos
