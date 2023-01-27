from math import pi
class Figura():
    def __init__(self,nombre):
        self.nombre = nombre
    
    def probar_figura(self):
        if self.nombre == 'Rectangulo':
           self.area = self.base * self.altura
           print(f'el area del Rectangulo es: {self.area}')
        elif self.nombre == 'Circulo':
            self.area = pi*(self.radio**2)
            self.perimetro = 2*pi*self.radio
            print(f'El area del Circulo es: {self.area}')
            print(f'El perimetro del Circulo es: {self.perimetro}')
        
class Rectangulo(Figura):
    def __init__(self, nombre,base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    
class Circulo(Figura):
     def __init__(self,nombre,radio):
        super().__init__(nombre)
        self.radio = radio
    




   