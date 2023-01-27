dic = {'v1': 1,'v2':2,'v3':3,'v4':4}
print(dic['v1']) #aca se puede llamar al valor por le nombre
# Para agregar un elemento nuevo al diccionario:

dic['v5'] = 5


# para buscar un valor por la clave o el nombre es:

dic.get('v4', 'No se eccontro') # este mensaje sale si el valor no esta

dic.keys() #Esto nos devuelve todas las claves o nombres 
dic.values() # Esto nos devielve los items o valores
dic.items() # esto nos devuelve todos los elementos completo clave+ valor

dic.pop('v4', 'No se ecnontro') # con este se usa para eliminar el elemeto
# del primer campo y el mensaje se muestra si no existe

dic.clear() # Borra todos los elementos del diccionario

for d in dic:
    print(d) #esto imprimiria solo las claves dentro del diccionario

for di in dic.values():
    print(d) # Aca nos devolvera los valores que hay dentro del diccionario

for clave, valor in numero.items():
    print(clave+ valor) # aca imprimiria todos los datos clave+valor