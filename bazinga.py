
list_to_replace=[1,2,3,4,56,6,67,8,9,0,10,12,13,14,15,16,17,18,19,20,21,22,23,45,2356,45,786,2456,12233]

sustitution=None

for position in range(len(list_to_replace)):
    if list_to_replace[position] % 5 == 0 and list_to_replace[position] % 3 == 0:
        sustitution="bazinga"
    elif list_to_replace[position] % 3 == 0:
        sustitution="fizz"
    elif list_to_replace[position] % 5 == 0:
        sustitution="buzz"
    else:
        sustitution=list_to_replace[position]
    list_to_replace[position]=sustitution


print(list_to_replace)