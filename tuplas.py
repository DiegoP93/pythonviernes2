#Creando tuplas en python
estudiantes=('carlos','juan')
print(estudiantes)
#estudiantes.append('martha')  ERROR no es posible agregar o modificar contenido en las tuplas
#print(estudiantes)

#recorriendo tuplas
for estudiante in estudiantes:
    print(estudiante)

#convertir tupla en lista
listaEstudiantes=list(estudiantes)
print(listaEstudiantes)
listaEstudiantes.append("Diego")
newTuple=tuple(listaEstudiantes)
print(newTuple)