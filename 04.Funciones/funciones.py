def saludo():
    nombre = 'johandry'
    # Si usamos global antes de la variable, esta se puede usar aun fuera
    # metodo declarado
    global nombre2
    nombre2 ='johandry'
saludo()
print(nombre2)

def retorno():
    global saludo
    saludo = 'hola como estas'
    edad = 21
    msj = 'hello'
    # Return lo que hace es devolver un valor para almacenar en una 
    # variable y declarar el final de un metodo

    return saludo, edad, msj #si se declara asi lo devuelve como tupla

# tenemos que ponerla dentro de un print para visualizar el return
print(retorno())
# la otra manera es almacenarlo en una variable
valorvar = retorno()
print(valorvar)
# para recuperar cada valor por separado se declaran las variables
# en el orden que quieres almacenar EJ

saludor, edadr,msjr = retorno()

print(saludor, edadr, msjr)