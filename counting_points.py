
print("Contador de puntos, comas y espacios")

puntos="."
comas=","
espacios=" "

frase=input("Escribi tu frase:")
coma=0
punto=0
espacio=0

for letra in frase:
    if letra in comas:
        coma += 1
    elif letra in puntos:
        punto += 1
    elif letra.isspace()==True:
        espacio +=1
print("Comas= {}".format(coma))
print("Punto= {}".format(punto))
print("Espacio= {}".format(espacio))
