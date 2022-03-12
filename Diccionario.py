#un diccionario no se escribe en plural

estudiante={
    'nombre': 'Diego',
    'edad': 18,
    'esProgramador': True
}
#imprimir/acceder a todas las llaves
#atributos de mi diccionario
print(estudiante)
#acceder a un atributo o llave del diccionario
print(estudiante['nombre'])
print(estudiante.get('edad'))#otra manera de acceder al atributo


#recorrer un diccionario y obtener sus valores
for valor in estudiante.values():
    print(valor)

for llave,valor in estudiante.items():
    print(llave,valor)#manera imprimir el valor junto a la llave