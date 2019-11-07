print("La media de tu lista")

lista=[]
lista_de_usuario = "0"

while lista_de_usuario.isdigit() == True:
    lista_de_usuario = input("Numero (escribir otro caracter que no sea numero para salir)")
    if lista_de_usuario.isdigit():
        lista.append(lista_de_usuario)
        print("Has añadido {} a tu lista".format(lista_de_usuario))

print("Lista:{}".format(lista))

cantidad_de_lista=0
lista=[int(i) for i in lista]
for asdd in lista:
    cantidad_de_lista += 1
suma_lista=sum(lista)

answer=suma_lista / cantidad_de_lista
print(answer)





