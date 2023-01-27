n = int(input('Ingrese el numero del mes: '))

verano = (1,2,3)
otoño = (4,5,6)
invierno = (7,8,9)
primavera = (10,11,12)

if n <= 12 and n> 0:
 if n in verano:
  print(f'El numero {n} es Verano')
 elif n in otoño:
   print(f'El numero {n} es Otoño')
 elif  n in invierno:
   print(f'El numero {n} es Invierno')
 elif n in primavera:
   print(f'El numero {n} es Primavera')
else:
 print('Ingrese un numero del 1 al 12')

#  Solucion del profesor

#  n = int(input('Ingrese el numero del mes: '))

# verano = (1,2,3)
# otoño = (4,5,6)
# invierno = (7,8,9)
# primavera = (10,11,12)

# if n <= 12 and n> 0:
#  if n in verano:
#   print(f'El numero {n} es Verano')
#  elif n in otoño:
#    print(f'El numero {n} es Otoño')
#  elif  n in invierno:
#    print(f'El numero {n} es Invierno')
#  elif n in primavera:
#    print(f'El numero {n} es Primavera')
# else:
#  print('Ingrese un numero del 1 al 12')