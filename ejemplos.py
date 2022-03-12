multiplos=[]
#multiplos=[1] para iniciuar con un valor (el 1 es un ejemplo)

longitudLista=int(input("Digite el tamaño de la lista: "))

for i in range(longitudLista):
    #multiplos.append(i * 7)
    multiplos.append((i+1) * 7)

print(multiplos) 