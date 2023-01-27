import sys

# el sys argv lo que hace es tomar los datos que se ingresan desde
# el script y lo almacena en una lista
# en las variables lo que hacemos es decir que en el indice 1
# se almacena el texto y en el indice 2 se almacena la cantidad de 
# veces a imprimir el texto
if len(sys.argv)==3:
 texto = sys.argv[1]
 cantidad = int(sys.argv[2])

 c=0
 while c< cantidad:
    print(texto)
    c+=1
else:
    print('Eror ingrese los datos correctamente')