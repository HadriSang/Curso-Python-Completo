def conversor(valor, pais):
     cantidad_moneda= float(input(f'Ingrese la cantidad de {pais}: '))
     dolares = cantidad_moneda / valor
     dolares = round(dolares,2) #esto me redondea los decimales a 2 valores o los que yo le indique
     print(f'Tienes ${dolares}')
print(' Lista Disponible: \n 0-Colombia \n 1- Peru \n 2- Uruguay \n 3-Paraguay \n 4-Mexico')


def main(n):
    i=False 

    while i==False:
     
     if n ==  0:
        pais = 'Colombia'
        conversor(3.61, pais)
        i = True
        return i 
      


     elif n ==  1:
        pais = 'Peru'
        conversor(3.61, pais)
        i = True
        return i
     elif n ==  2:
        pais = 'Uruguay'
        conversor(3.61, pais)
        i = True
        return i
     elif n ==  3:
        pais = 'Paraguay'
        conversor(3.61, pais)
        i = True
        return i
     elif n ==  4:
        pais = 'Mexico'
        conversor(3.61, pais)
        i = True
        return i
     elif n == 5 or n >5:
        
        print('Ingrese un valor valido')
        main(int(input('Ingrese el valor Deseado: ')))
        i=False
        return i  

if __name__ == '__main__':
 main(int(input('Ingrese el valor Deseado: ')))


# Hasta el momento el profesor lo trabaja de manera similar
# pero declara el menu asi

# menu = """ 
# 1- col
# 2-para
# 3- tal
# Ingrese Opcion 


# """

# opcion = input(menu)


# la triple " es para textos granses