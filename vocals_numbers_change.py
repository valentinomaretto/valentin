
user_phrase = input("a phrase created:")

phrase=[]

large = len(user_phrase)
start = 0
vocal_number = 0

while start < large:
    if user_phrase[start] in "aeiou":
        vocal_number += 1
        start += 1
        phrase.append(str(vocal_number))
    else:
        phrase.append(user_phrase[start])
        start += 1

user_phrase_final = "".join(phrase)


print(user_phrase)
print(phrase)
print(user_phrase_final)

