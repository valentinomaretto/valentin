print("CALCULATOR")

answer=1

infinito=1
while infinito > 0:
    operation=input("what operation do you want to do? (sum/subtraction/multiplication/division)").upper()
    first_number=float(input("First number:"))
    second_number=float(input("Second number:"))

    if operation=="SUM":
        answer=first_number + second_number
        print("Answer:{}".format(answer))

    elif operation=="SUBTRACTION":
        answer=first_number - second_number
        print("Answer:{}".format(answer))


    elif operation == "MULTIPLICATION":
        answer = first_number * second_number
        print("Answer:{}".format(answer))

    elif operation=="DIVISION":
        answer=first_number / second_number
        print("Answer:{}".format(answer))