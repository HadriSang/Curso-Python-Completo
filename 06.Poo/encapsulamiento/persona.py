class Persona:
    __nombre = None # Al colocar __ estamos diciento que el elemto
    __edad = None # es privado
    def __init__(self,nombre,edad):
      self.__nombre = nombre
      self.__edad = edad

    def __metodoprivado(self):
        print('Estes es un metodo privado')

# Con los metodos get y set lo que estamos haciendo es tomar la variable
# que va a modificar la ya creada y luego la reemplaza por la ya creadad
# ya que al ser metodos privados una vez creados con las variables, para ser
# modificados es necesario usar estos metodos

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self,edad):
        self.__edad = edad
    
    
    def __str__(self):
        return f'Nombre {self.__nombre} \nEdad: {self.__edad}'