def parimpar():
    list=[]
    cont=0
    sumPar=0
    sumImpar=0
    for i in range(6):
        cont+=1
        list.append(int(input(f'Ingrese el numero {cont}: ')))

    for a in list:
        if a %2 ==0:
            sumPar+=a
        else:
            sumImpar+=a

    print(f'La suma de numeros Pares es: {sumPar}')
    print(f'La suma de numeros Impares es: {sumImpar}')

parimpar()
    
