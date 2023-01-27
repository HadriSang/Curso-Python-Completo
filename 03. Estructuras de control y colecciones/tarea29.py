def num():
    list1=[]
    list2=[]
    list3=[]
    cont=0
    for i in range(4):
        cont +=1 
        list1.append(int(input(f'Ingrese el numero {cont}: ')))
        
        
        
    for i in range(4):
        cont +=1 
        list2.append(int(input(f'Ingrese el numero {cont}: ')))

    for i in range(4):
        cont +=1 
        list3.append(int(input(f'Ingrese el numero {cont}: ')))

    sum1 = list1[0] +list1[1]+list1[2]+list1[3]
    # otra manera de hacer la suma:
    sum1=0
    for a in list1: #esta ahorra mas recurso
     sum1+=a
    #  ___________________________________________
    sum2 = list2[0] +list2[1]+list2[2]+list2[3]
    sum3 = list3[0] +list3[1]+list3[2]+list3[3]
    
    print(f'La suma del 1 al 4 es: {sum1}')
    print(f'La suma del 5 al 8 es: {sum2}')
    print(f'La suma del 9 al 12 es: {sum3}')

num()