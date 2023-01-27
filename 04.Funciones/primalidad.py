def es_primo(n):
    contador = 0
    for i in range(1, n+1):
     if i == 1 or i == n:
        continue
     if n % i == 0:
        contador+=1
    if contador == 0:
        return True
    else: 
        return False

def main():
    n = int(input('Ingrese un numero: '))
    if es_primo(n):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
 main()
