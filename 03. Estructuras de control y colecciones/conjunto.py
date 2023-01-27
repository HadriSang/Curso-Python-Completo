# un conjunto no pude almacenar un valor que se repita
# para definir un conjunto se hace asi:

con = set()

con= {'a','b','c'}

# tambien se puede transformar un string en un conjunto
# cada caracter se convierte en un elemento

a = set('hello world') # todo el elemento que se repitan solo se suman al 
# conjunto una sola vez
print(a)

b = set('this is an example')
print(a-b) #aca me va a mostrar los datos que esten en a pero no estan en b

a | b # aca me devuelves lertsa en a o en b

a & b #aca me devuelve las letras en comun 

a^b# aca me devuelve las letra en a o en b pero no en las 2


a.add('d') #El add se usa para agregar un elemento al conjunto

a.discard('d') #Este se usa para eliminar el elemento especifico

a.clear() #Este se usa para eliminar todos los datos dentro del conjunto
