from persona import Persona
# Los metodos privados parece que se acceden pero en realidad no se 
# pueden modificar sin el getter an setter

persona1 = Persona('Hadri', 25)
# para modificar el nombre es necesario llamar al metodo set
persona1.set_nombre('Sang')

print(persona1.get_nombre()) #y para visualizar el cambio se llama al get

print(persona1)