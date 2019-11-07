frase=input("Escribi tu frase:")

vocales=["a","e","i","o","u"]

vocales_usuario=[]

vocals=0

for letter in frase:
    if letter in vocales:
        vocales_usuario.append(letter)
print("vocales:{}".format(vocales_usuario))

