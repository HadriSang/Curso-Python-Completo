n1 = int(input('Ingrese un numero de 5 digitos: '))

resi1=n1%10
r1= n1//10
resi2=r1%10
r2= r1//10
resi3= r2%10
r3= r2//10
resi4= r3%10
r4= r3//10
resi5= r4%10

print(' El numero del residuo en orden inverso es: ',resi1,resi2,resi3,resi4,resi5)

# Solucion Prof
# Ingresar datos
# numero = input('Número: ')

# # Convertir 
# numero = int(numero)

# # Solución 

# residuo = numero % 10
# numero = numero // 10
# numeroInverso = residuo * 10

# residuo = numero % 10
# numero = numero // 10 
# numeroInverso = (numeroInverso + residuo) * 10

# residuo = numero % 10
# numero = numero // 10 
# numeroInverso = (numeroInverso + residuo) * 10

# residuo = numero % 10
# numero = numero // 10
# numeroInverso = (numeroInverso + residuo) * 10

# numeroInverso = numeroInverso + numero

# # Salida de datos
# print('Inverso: ', numeroInverso)