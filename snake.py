import random

snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}

def play_game():
    pos = 0
    active = False
    
    print("Welcome! Roll a 1 to start your game.")
    
    while pos < 100:
        input("\nPress Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}")
        
        if not active:
            if roll == 1:
                active = True
                print("You're in the game!")
            else:
                print("Need a 1 to start!")
                continue
        
        if pos + roll <= 100:
            pos += roll
            if pos in ladders:
                print(f"Climbed a ladder to {ladders[pos]}")
                pos = ladders[pos]
            elif pos in snakes:
                print(f"Snake bit you! Back at {snakes[pos]}")
                pos = snakes[pos]
        
        print(f"You're currently at {pos}")
        
    print("\nYou reached 100 and won!")

if __name__ == "__main__":
    play_game()