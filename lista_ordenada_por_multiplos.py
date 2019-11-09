list=[]
input_usuario=""

while input_usuario != "end":
    input_usuario = input("add to the list numbers:(end to finish)")
    if input_usuario != "end":
        list.append(input_usuario)

list_int=[int(i) for i in list]
list_two=[]
list_three=[]
list_five=[]
list_seven=[]

for numb in list_int:
    if numb % 5 == 0:
        list_five.append(numb)
    if numb % 2 == 0:
        list_two.append(numb)
    if numb % 3 == 0:
        list_three.append(numb)
    if numb % 7 == 0:
        list_seven.append(numb)

print(list_two)
print(list_three)
print(list_five)
print(list_seven)

print(list_int)