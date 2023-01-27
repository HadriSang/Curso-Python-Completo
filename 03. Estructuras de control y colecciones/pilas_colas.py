# Las pilas hacen referencia al ultimo dato que entra 
# es el primero en salir
pila = [1,2,3]
pila.append(4)
pila.append(5)
pila.pop()

# Las colas son diferentes, el primero que entra es el primero que sale

from collections import deque
cola = deque(['hello','world',2023,'uwu'])

cola.popleft() #esto va a quitar el elemnto de la izquierda
# es decir el primer elemento de la lista


