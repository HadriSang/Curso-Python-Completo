import random
mensaje= """El juego consiste en adivinar el numero
El numero que tienes que adivinar va del 1 al 100
Tienes 10 vidas    """
print(mensaje)
def jugar(vidas):
    numero_random =random.randint(1, 100)
    numero_elegido = None
    while numero_random != numero_elegido:
      numero_elegido = int(input('Ingrese el numero elegido: '))

      if numero_random < numero_elegido:
        print('Prueba un numero mas pequeño')
        vidas -= 1
      elif numero_random > numero_elegido:
        print('Prueba un numero mas grande')
        vidas -=1
    
      if vidas == 0:
         print('Game Over')
         break
      
      print(f'Te quedan {vidas} vidas')
    if numero_elegido == numero_random:
        print('Felicidades Ganaste el Juego')

def main():
    while True:
        menu = """ Adivina el numero
        1 - Nivel Facil
        2 - Nivel Intermedio
        3 - Nivel Dificil
        4 - Salir
         Ingrese una Opcion: """

        opcion = int(input(menu))

        if opcion == 1:
            jugar(10)
        elif opcion == 2:
            jugar(7)
        elif opcion ==3:
            jugar(5)
        elif opcion == 4:
            print('Cerrando Juego')
            break
        else:
            print('Ingrese una opcion valida')

if __name__ == '__main__':
    main()