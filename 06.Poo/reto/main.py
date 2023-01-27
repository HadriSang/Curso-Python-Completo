from figuras import *
f = True
while True:
    print('Ingrese la opcion deseada')
    i = int(input('1-Rectangulo \n2-Circulo \n3-Salir \n'))
    if i >0 and i<=2:
     if i == 1:
        b = float(input('Ingrese la base del rectangulo: '))
        a = float(input('Ingrese la altura del rectangulo: '))
        rectangulo1 =Rectangulo('Rectangulo',b , a)
        rectangulo1.probar_figura()
     elif i == 2:
        r = float(input('Ingrese el radio del circulo: '))
        circulo1 = Circulo('Circulo', r)
        circulo1.probar_figura()
     elif i ==3:
        f = False
    elif i == 3:
        print('Cerrando Programa')
        break
    else:
        print('Ingrese una Opcion valida')
    