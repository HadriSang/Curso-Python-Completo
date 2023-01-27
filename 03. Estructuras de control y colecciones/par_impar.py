# if False:
#     print('se cumple la condicion')
# else:
#     print('No se cumple la condicion')

#     n= int(input('Ingrese el numero '))

#     if n>5:
#         print('El numero es mayor que 5')
#     else:
#         print('El numero es menor o igual que 5')





n2= int(input('Ingrese el numero entero '))

if n2 != 0:
    if n2 >0:
        if n2 % 2 == 0:
          print(f'El numero {n2} es PAR POSITIVO')
        else:
          print(f'El numero {n2} es IMPAR POSITIVO')
    else:
        if n2 % 2 == 0:
          print(f'El numero {n2} es PAR NEGATIVO')
        else:
          print(f'El numero {n2} es IMPAR NEGATIVO')

else:
    print(f'El numero {n2} es neutro ')
