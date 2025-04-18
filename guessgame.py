import random as rand

def start_game():
    global number, attempts
    number = rand.randint(1,100)
    attempts = 0
    print("\nGenerating Number...")
    print("\n--NEW GAME--")

def end_game():
    global playing
    decision = input("\nPlay new game? (yes/no): ").lower()
    if decision == "yes":
        playing = True
        start_game()
    elif decision == "no":
        playing = False
        print("Thank you for playing!")
    else:
        print("Invalid input")
        end_game()


playing = True
print("\n--Welcome to the number guessing game--")
start_game()

while playing:
    guess = int(input("\nEnter your guess from 1 to 100: "))
    if 0 < guess < 101:
        attempts +=1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("!CORRECT!")
            print(f"You guessed in {attempts} attempts.")
            end_game()
    else:
        print("Enter a valid number.")
    