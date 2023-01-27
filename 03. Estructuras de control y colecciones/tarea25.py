def numAmigos():
    n1 = int(input('Ingrese el primer numero: '))
    n2 = int(input('Ingrese el segundo numero: '))
    sum1 = 0
    sum2 = 0

    for numeros in range(1,n1):
      if n1 % numeros == 0:
       sum1+= numeros
      
    for numeros2 in range(1,n2):
     if n2 % numeros2 == 0:
      sum2+= numeros2
    if n1 == sum2 or n2 == sum1:
      print(f'Los numeros {n1} y {n2} son amigos ')
    else:
      print(f'Los numeros {n1} y {n2} no son amigos ') 
     

numAmigos()