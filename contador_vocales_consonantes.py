
print("Counting vocals and consonants")
vocals=["a","e","i","o","u"]

phrase=input("Write a phrase:")

vocals_a=0
consonants=0

for letra in phrase:
    if letra in vocals:
        vocals_a += 1
    else:
        consonants += 1

print("Vocals={}".format(vocals_a))
print("Consonants={}".format(consonants))


