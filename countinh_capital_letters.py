
print("Counting capital letters")

phrase=input("write your prhase:")

capital_letter=0

for letra in phrase:
    if letra.isupper() == True:
       capital_letter += 1

print("Capital letter:{}".format(capital_letter))
