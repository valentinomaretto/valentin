
list=[]
numeros = 6

while len(list) < 10:
    numeros = input("Añada numeros a la lista:")
    while numeros.isdigit()==False:
        numeros = input("Añada numeros a la lista:")
    numero_añadido=print("Se ha añadido {} a la lista".format(numeros))
    list.append(numeros)
print(list)

mas_chico=list[0]

for menor in list:
    mas_chico < menor
    menor=mas_chico
print("El mas chico es: {}".format(mas_chico))

