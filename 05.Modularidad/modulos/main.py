import fibonacci
from fibonacci import fibo, fibo2 # si usamos , podemos llamar mas funciones.
from fibonacci import * # esta se usa para importar todo lo que esta
# dentro de un paquete 

import sys

# import fibonacci as f 
# Este nos permite llamar al modulo con un nombre definido ejemplo f
# from fibonacci import fibo as fi
# Tambien se puede aplicar a las funciones

# #fibonacci.fibo(100) haciendo el import de arriba con el from ya no se llama asi si no asi:

# fibo(100) # esto es para funciones especificas
# print(fibo2(100))

print(dir(sys)) # el dir nos ta una informacion de un modulo

print(dir())# aca nos da la informacion actual que esta dentro del archivo
