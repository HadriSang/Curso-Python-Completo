def operacion():
    n1 = int(input('Ingrese el numero 1: '))
    n2 = int(input('Ingrese el numero 2: '))
    i = True
    while i == True: 
     
     op = input('Ingrese el operador: ')

     if op == '+' or op == '-' or op == '*' or op == '/':
        if op == '+':
            r= n1 + n2
            print(f'El Resultado es: {r}')
            i = False
        elif op == '-':
            r= n1 - n2
            print(f'El Resultado es: {r}') 
            i = False
        elif op == '*':
            r= n1 * n2
            print(f'El Resultado es: {r}')
            i = False
        elif op == '/':
            r= n1 / n2
            print(f'El Resultado es: {r}')  
            i = False 
     else:
      i = True
      print('Ingrese un Operador valido')

operacion()