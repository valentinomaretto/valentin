
numero_tabla=int(input("Tabla del numero:"))

for tabla in range(1,16):
    resultado=numero_tabla * tabla
    print("{} * {} = {}".format(numero_tabla,tabla,resultado))

