# las funciones anonimas o lambdas  son aquellas que no tienen nombre
# y se usa par afunciones cortas

sumar = lambda a,b:a+b
var = sumar(a=int(input('valor 1: ')), b=int(input('valor 2: ')))
print(var)

doblar = lambda n:n*2
print(doblar(int(input('Ingrese el valor '))))

par = lambda n: n % 2==0
print(par(int(input('Ingrese el numero '))))

impar = lambda n : n % 2 != 0

print(impar(int(input('Ingrese el numero: '))))

revertir = lambda cadena: cadena[::-1] #esta expresion revierte una cadena

print(revertir('hola como estas'))