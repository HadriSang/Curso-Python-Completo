# VERSION DEL PROFESOR
# MEJORA EN EL SENTIDO DE QUE SE APLICA MUCHO MEJOR LA LOGICA

def conversor(valor, pais):
     cantidad_moneda= float(input(f'Ingrese la cantidad de {pais}: '))
     dolares = cantidad_moneda / valor
     dolares = round(dolares,2) #esto me redondea los decimales a 2 valores o los que yo le indique
     print(f'Tienes ${dolares}')


def main():
  
    
    while True:
     menu = """Lista Disponible:
     1-Colombia 
     2- Peru 
     3- Uruguay 
     4-Paraguay 
     5-Salir'
     Ingrese la Opcion deseada: """
     n = int(input(menu))
     if n ==  1:
        pais = 'Colombia'
        conversor(3.61, pais) 

     elif n ==  2:
        pais = 'Peru'
        conversor(3.61, pais)
       
     elif n ==  3:
        pais = 'Uruguay'
        conversor(3.61, pais)
        
     elif n ==  4:
        pais = 'Paraguay'
        conversor(3.61, pais)
        
     elif n ==  5:
        print('Cerrando conversor')
        break
        
     else:
        
        print('Ingrese un valor valido')
        main(int(input('Ingrese el valor Deseado: ')))
        

if __name__ == '__main__':
 main()


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