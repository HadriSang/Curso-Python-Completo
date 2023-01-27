#aca vamos a crear un molde

class Persona:
    
    #lo que esta dentro de los parentesis puede ser cualquier palabra
    # pero para idenficar que el metodo (por que esta dentro de una clase pasa a ser metodo)
    # es de una clase es comun usar la palabra self


 # Aca vamos a iniciar el constructor de esta clase
 #  para simplificar el ingreso de los datos

   def __init__(self,nombre,edad):
      self.nombre = nombre
      self.edad = edad

  

   def mostrarDatos(self):
        # es necesario poner el self antes de usar la variable
        print(f'Su nombre: {self.nombre}')
        print('Su edad: ', self.edad)



   def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
        #Esto nos ayuda que al imprimir la variable nos devuelva los datos 
        # y no la ubicacion en memoria