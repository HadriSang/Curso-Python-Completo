n= int(input('Ingrese el numero inicial: '))
nf = int(input('Ingrese el numero final: '))
var= 0 
count = 0

var = n + 1 
while var < nf:
   
    var+= 1 
    if var % 2 == 0:
     count += 1
    
print(f' La cantidad de pares es: {count}')