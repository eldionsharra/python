import random

def game_start_end():
    end = input("Do you want to continue? (yes/no) ").lower()
    if end == "yes":
        play = True
    elif end == "no":
        play = False
    else:
        print("Please enter a valid answer!")
        game_start_end()

    return play


print("\nLet's play |Python| -- Rock Paper Scissors --")
user_score = 0
pc_score = 0
game_count = 0
play = True

while play:
    user_choice = input("\nEnter your choice [rock, paper, scissors] ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("!Invalid choice!")
        continue

    pc_choice = random.choice(["rock", "paper", "scissors"])
    print("You chose:", user_choice)
    print("Computer chose:", pc_choice)

    if user_choice == pc_choice:
        print("It is a tie!!")
        game_count += 1
        play = game_start_end()
    
    elif user_choice == "rock" and pc_choice == "scissors":
        print("User wins!!")
        user_score += 1
        game_count += 1
        play = game_start_end()
    elif user_choice == "paper" and pc_choice == "rock":
        print("User wins!!")
        user_score += 1
        game_count += 1
        play = game_start_end()
    elif user_choice == "scissors" and pc_choice == "paper":
        print("User wins!!")
        user_score += 1
        game_count += 1
        play = game_start_end()
    else:
        print("Computer wins.")
        pc_score +=1
        game_count += 1
        play = game_start_end()
    


print(f"\nThank you for playing {game_count} games!")
print(f"You won {user_score} times.")
print(f"Computer won {pc_score} times.")
