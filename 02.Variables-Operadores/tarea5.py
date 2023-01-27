
cap = int(input('Ingrese el monto de la capital: '))
ti = int(input('Ingrese el monto de la tasa de interese: '))
t = int(input('Ingrese el tiempo: '))


m = ((1+ti/100)**t)*cap
i = m -cap

print('El interes es: ', i)
print('El monto es: ', m)



