number_to_guess=33

user_number=int(input("number one"))

if user_number==number_to_guess:
    ganar
else:
    print("intenta otra vez")
    user_number_two=int(input("number two"))
    if user_number_two==number_to_guess:
        ganar
    else:
        user_number_three=int(input("number three"))
        if user_number_three==number_to_guess:
            ganar
        else:
            print("try again")


