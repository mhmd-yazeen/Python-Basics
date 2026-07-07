# Player Vs Enemy
import random
player = input("Enter your name :- ").lower()
enemy = random.choice(["dragon","goblin","monstor"])
playerhp = 100 
enemyhp = 100 
turn = 1
while playerhp > 0 and enemyhp > 0:
    print(f"Life{turn}")
    print(f'{enemy} Attack enemy')
    playerhp = playerhp - random.randint(0,20)
    print(f"player hp {playerhp}")
    print(f"{player} stikes back")
    enemyhp = enemyhp - random.randint(0,20)
    print(f"enemy hp {enemyhp}")
    turn = turn + 1
    if playerhp <= 0:
        print(f"{enemy} won")
        break
    elif enemyhp <= 0:
        print(f"{player} won")
  



