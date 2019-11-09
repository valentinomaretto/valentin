def entre(a,b,c):
    if a >= b and a <= c :
        answer = True
    else:
        answer = False
    return answer
numero_intermedio = int(input("numero medio:"))
numero_min = int(input("numero minimo:"))
numero_max = int(input("numero maximo:"))

print(entre(numero_intermedio,numero_min,numero_max))

