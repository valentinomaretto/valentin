
numero_de_tabla=int(input("NUMBER:"))

for number in reversed(range(1,11)):
    resultado = numero_de_tabla * number
    if number % 2 == 0:
        print("{}*{}={}".format(numero_de_tabla,number,resultado))
#REVERSED PAR IMPAR CON %