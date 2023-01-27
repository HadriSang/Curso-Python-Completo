def cantDigitos():
 ne = int(input('Ingrese el numero entero: '))
 var = 0 

 count = 0
 
 while ne > 0: 
    var = ne % 10

    if var % 2 == 0:
     count += 1
    ne //=10
    
    
       


 print(f'La cantidad de digitos pares es {count}')

cantDigitos()
