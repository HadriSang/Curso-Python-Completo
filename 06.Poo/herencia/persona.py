class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')
    def __str__(self):
        return f'Nombre {self.nombre} \nEdad: {self.edad}'    

# Aca estamos creando una sub clase donde decimos 
# que la clase cliente hereda de la clase principal persona
class Cliente(Persona):
    pass

# Al heredar no es necesario crear los metodos dentro de esta clase
# ya que cliente esta heredando y usando los metodos ya definidos en 
# la clase Persona

#Clase empleado que hereda de persona USANDO SUPER

# class Empleado(Persona):
#     def __init__(self, nombre, edad,sueldo):
#         super().__init__(nombre, edad) #Al usar super, lo que hacemos es llamar
#         #Al metodo en especifico y añadir o modificar su condicion
#         self.sueldo = sueldo
#     def detalle_empleado(self):
#         super().detalle_persona()
#         print('Sueldo: ',self.sueldo)
#     def __str__(self):
#         return super().__str__() + f'\n Sueldo: {self.sueldo}'

# Herendando sin SUPER
class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo):
       Persona.__init__(self, nombre, edad)
       self.sueldo = sueldo
    def detalle_empleado(self):
         Persona.detalle_persona(self)
         print('Sueldo: ',self.sueldo)
    def __str__(self):
         return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'