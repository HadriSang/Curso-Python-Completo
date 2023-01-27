c=0
suma= 0
while c <3:
    try: #Debemos encerrar el metodo a ejecutar en el try
       n = int(input(f'Ingrese el numero {c+1}: '))
       suma += n
       c +=1
    except: # y el mensaje a mostrar despues del exept
        print('Ingrese solo numeros enteros')
    else: #Esto se le coloca para que se ejecute despues de que todo funcione
        print('Todo funciono bien')

    finally: #esta se ejecuta al final independientemente de si 
        #fue exitosa o fallida, se puede colocar despues del else o exept
        print('fin de la ejecucion')

print(f'La suma total es: {suma}')
