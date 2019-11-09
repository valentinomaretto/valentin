def par(list):
    pares=[]
    for number in list:
        if number % 2 == 0:
            pares.append(number)
    return pares

numeros=[1,2,3,4,5,6,7,8,9,11,15,62,95,35,64,894,78,32,15,1133]

print(par(numeros))