
write=str(input("Write something:"))

write=write.replace("a","i")
write=write.replace("e","i")
write=write.replace("u","i")
write=write.replace("o","i")

separate=write.split()

answer=[]

for word in separate:
    answer.append(word)
    answer.append(word)

final_answer=" ".join(answer)

print(final_answer)