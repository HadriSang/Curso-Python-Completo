class Persona(object):
    # constructor
    def __init__(self,nombre):
        self.nombre = nombre

    def moverse(self):
        print(f'{self.nombre} Ando caminando')


class Atleta(Persona):
    def moverse(self):
     print('Ando Corriendo')


class Ciclista(Persona):
    def moverse(self):
        print('Ando en bici')




# El polimorfismo nos permite reescribir elementos de la clase padre
