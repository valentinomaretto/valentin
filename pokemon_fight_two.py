print("POKEMON FIGHT?")
start_command=int(input("Write 1 to start♠"))
if start_command==1:
    print("Good let´s play with pikachu")
else:
    print("Bye")

enemys=input("write your enemy (goku/homero/bulbasur)").upper()

if enemys=="BULBASUR":
    enemy_life=100
    enemy_damage=16
    enemy_name="Bulbasur"
elif enemys=="GOKU":
    enemy_life=120
    enemy_damage=13
    enemy_name="Goku"
elif enemys=="HOMERO":
    enemy_life=80
    enemy_damage=20
    enemy_name="Homero"

pikachu_life=103
pikachu_damage=18
pikachu_damage_two=19
pikachu_name="Pikachu"

ready=int(input("1 to play/2 for exit"))
if ready==1:
    print("Fight")
elif ready==2:
    exit("bye")

while pikachu_life>0 and enemy_life>0:
    print("Your life {}".format(pikachu_life),"Enemy life {}".format(enemy_life))
    attack=input("Write your attack (Xray/Ak47)").upper()
    if attack=="XRAY":
        enemy_life -= 18
        print("A-18☺")
    elif attack=="AK47":
        enemy_life -= 18
        print("A-19☺")
    print("D-{}♥".format(enemy_damage))
    pikachu_life -= enemy_damage
if pikachu_life <= 0:
   print("YOU LOSE")
if enemy_life <= 0:
  print("YOU WIN")

print("FINISH THANKS FOR PLAYING")


