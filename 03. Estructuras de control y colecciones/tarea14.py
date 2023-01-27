n = int(input('Ingrese el numero: '))

verano = 1
otoño = 2
invierno = 3
primavera = 4 

if n <= 4:
 if n == verano:
  print(f'El numero {n} es Verano')
 elif n== otoño:
   print(f'El numero {n} es Otoño')
 elif n== invierno:
   print(f'El numero {n} es Invierno')
 elif n== primavera:
   print(f'El numero {n} es Primavera')
else:
 print('Ingrese un numero del 1 al 4')