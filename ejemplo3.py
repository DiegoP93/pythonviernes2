listaNumeros = []
for i in range(0,5,1):
    numeroIngreso = int(input('Digite el numero: '))
    listaNumeros.append(numeroIngreso)

buscarNumero = int(input('¿Que numero buscas?: '))

if(buscarNumero in listaNumeros):
    print('si esta en la lista')
else:
    print('No esta en la lista')


#manera 2 de hacer el ejercicio

numeros = []

tamaño= int (input("Digite el tamaño: "))

for i in range(tamaño):
    numero = int(input("Digite un numero: "))
    numeros.append(numero)

buscar = int(input("ingrese el numero que busca: "))
if(numero in numeros):
    print(f"el numero: {buscar} si esta")
else:
    print(f"el numero: {buscar} no esta")
    