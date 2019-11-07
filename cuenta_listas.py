print("CUENTA LISTAS")

list=[]
lista_usuario="0"
while lista_usuario.isdigit()==True :
    lista_usuario = input("Llena tu lista: [end para terminar]")
    if lista_usuario.isdigit()==True:
        list.append(lista_usuario)
    print("Numero añadido {}".format(lista_usuario))
print(list)
objetos_en_lista=0

for num in list:
    objetos_en_lista += 1
print("Objetos en lista: {}".format(objetos_en_lista))
