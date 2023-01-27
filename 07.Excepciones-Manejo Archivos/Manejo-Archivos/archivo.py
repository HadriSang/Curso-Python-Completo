from io import open
from os import path
def escribir_archivo():
    archivo = open('texto.txt','w') #en el primero va el nombre del archivo y en el segundo despues de la coma va la maenra en la que se quiere abrir ya sea para editar, etc
    archivo.write('hola como estas')
    archivo.close()

def leerArchivo():
    if path.isfile('texto.txt'):
      archivo = open('texto.txt', 'r')
     # textos = archivo.read()
      textos = archivo.readlines()
      archivo.close()
      print(textos)
    else:
        print('no existe el archivo')
       
        
def agregarDatos():
    if path.isfile('texto.txt'):
    
     archivo = open('texto.txt','a')
     archivo.write('\n aaaa')
     archivo.close()
     
    else:
        print('no existe el archivo')

def modificarDatos():
    if path.isfile('texto.txt'):
    
     archivo = open('texto.txt','r+')
     textos = archivo.readlines()
     print(textos)
     textos[1] = 'hola es una edicion' #este es para trabajar o modificar el elemento en la linea indicada

     print(textos)
     archivo.seek(0) #seek es para trabajar o modificar en la posicion del puntero
     archivo.writelines(textos) # es para escribir cantidades grandes de datos
     print(textos)
     archivo.close()
     
    else:
        print('no existe el archivo')

def eliminarDatos():
    if path.isfile('texto.txt'):
    
     archivo = open('texto.txt','w') # se puede usar el metodo w para abir el archivo reescribiendo su contenido a nada
     archivo.close()
     
    else:
        print('no existe el archivo')

eliminarDatos()