# with break 
n= 0
while n < 10: 
 n+=1
 print(n)
 if n == 5:
    print('termina el bucle')
    break
else:
  print('Fin del While')

# with continue 
n= 0
while n < 10: 
 n+=1
 print(n)
 if n == 5:
    print('Salta a la siguiente iteracion')
    continue
# todo lo que esta despues de continue se salta a la siguiente iteracion
 print('despues de continue')
else:
  print('Fin del While')

