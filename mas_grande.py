
list_bug = [9,4,26,62,33,245,665,9,256,482]

menor=list_bug[0]
mayor=0

for number in range(len(list_bug)):
    if list_bug[number] > menor:
        menor = list_bug[number]

print(menor)