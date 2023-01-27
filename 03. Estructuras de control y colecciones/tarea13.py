def nAscendentes():
    n1 = int(input('Ingrese el Numero 1: '))
    n2 = int(input('Ingrese el Numero 2: '))
    n3 = int(input('Ingrese el Numero 3: '))
    val = True
    numMay = 0
    numMen = 0
    numInt = 0
    if n1 > n2 and n1> n3:
     numMay = n1
     if n2<n3:
      numMen = n2
     else:
      numMen = n3
    elif n2 > n1 and n2> n3:
         numMay  = n2
         if n1<n3:
          numMen = n1
         else:
          numMen = n3
    elif n3 > n1 and n3> n2:
         numMay = n3
         if n2<n1:
           numMen = n2
         else:
           numMen = n1
    else:
          val = False
          print('2 Numeros o mas son iguales')
    if val == True:
     numInt = (n1+n2+n3) - (numMay + numMen)
     print(f'El numero mayor es: {numMay}')
     print(f'El numero intermedio es: {numInt}')
     print(f'El numero menor es: {numMen}')
    

nAscendentes()
