
lista_a=[65,96,"asd",",eq34za",9,6,"e"]
lista_int=[]
lista_str=[]

for dato in lista_a:
    if type(dato)== str:
        lista_str.append(dato)
    elif type(dato)== int:
        lista_int.append(dato)
print("INT:{}".format(lista_int))
print("STR:{}".format(lista_str))



