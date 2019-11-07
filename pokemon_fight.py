pikachu_life=100
enemy_life=0

print("POKEMON FIGHT!!")
wanna_play=int(input("Put one to start: "))
if wanna_play==1:
    print("Starting")
    character=input("Chose a character to fight: (Bulbasur/goku/Homero)").upper()
    if character=="BULBASUR":
        enemy_life += 90
        print("TIME TO PLAY")
        while pikachu_life > 0 and enemy_life > 0:
            print("your life", pikachu_life, "enemy life", enemy_life)
            attack = input("choose an attack (xray -10/volta -12)").upper()
            if attack == "XRAY":
                enemy_life -= 10
                print("Attack -10 ☻")
            elif attack == "VOLTA":
                enemy_life -= 12
                print("Attack -12 ☻")
            print("Taken -9 ♥")
            pikachu_life -= 9
        if pikachu_life>enemy_life:
            print("you win")
        elif enemy_life>pikachu_life:
            print("you lose")
    elif character=="GOKU":
        enemy_life += 80
        print("TIME TO PLAY")
        while pikachu_life > 0 and enemy_life > 0:
            print("your life", pikachu_life, "enemy life", enemy_life)
            attack = input("choose an attack (xray/volta)").upper()
            if attack == "XRAY":
                enemy_life -= 10
                print("Attack -10 ☻")
            elif attack == "VOLTA":
                enemy_life -= 12
                print("Attack -12 ☻")
            print("-17 ♥")
            pikachu_life -= 17
        if pikachu_life>enemy_life:
            print("you win")
        elif enemy_life>pikachu_life:
            print("you lose")
    elif character=="HOMERO":
        enemy_life += 100
        print("TIME TO PLAY")
        while pikachu_life>0 and enemy_life>0:
            print("your life",pikachu_life,"enemy life",enemy_life)
            attack=input("choose an attack (xray/volta)").upper()
            if attack=="XRAY":
                enemy_life-=10
                print("Attack -10 ☻")
            elif attack=="VOLTA":
                enemy_life-=12
                print("Attack -12 ☻")
            print("-11 ♥")
            pikachu_life-=11
        if pikachu_life>enemy_life:
            print("you win")
        elif enemy_life>pikachu_life:
            print("you lose")


print("bye king")

