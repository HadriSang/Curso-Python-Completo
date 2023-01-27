import my_paquete.aritmetica as a

def main():
  suma = a.sumar(4,54,5,5,5)
  resta = a.restar(10,5)
  potencia = a.potencia(3,3)

  print('La suma es: ', suma)
  print('La resta es: ', resta)
  print('La potencia es: ', potencia)

if __name__ == '__main__':
    main()


    #aca estamos trabajando un paquete propio
    # donde my_paquete es la carpeta que almacena el paquete aritmetica
    # que dentro tiene los metodos suma resta y potencia