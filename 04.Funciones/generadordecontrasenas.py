import random

def generar_contrasena():
    mayus = ['A','B','C','D','E']
    minus = ['a','b','c','d','e']
    simb= ['#','?','{','}']
    nume= [1,2,3,4,5,6,7,8,9]
    caracteres = mayus + minus + simb + nume
    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
# Esto convierte la contraseña de lista a str
    contrasena = ''.join(map(str, contrasena)) # al principio dejando
    #Solo el join fallaba por que el join solo permite ingresar valores
    # de tipo str para lo que se debe cambiar los numeros a str
    # o usar el metodo map y declarar que todo valor pase a se str
    return contrasena

def main():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es: ', contrasena)

if __name__ == '__main__':
    main()

    # REVISAR