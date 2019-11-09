def mayor_de_tres(a,b,c):
    mas_grande=0
    if a > b and a > c:
        mas_grande = a
    elif b > a and b > c :
        mas_grande = b
    elif c > a and c > b :
        mas_grande = c
    return mas_grande

numero_one=int(input("Numero:"))
numero_two=int(input("Otro:"))
numero_three=int(input("last:"))


print(mayor_de_tres(numero_one,numero_three,numero_two))