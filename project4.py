import random
from colorama import Fore,init;init(autoreset=True)
def ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def decide_winner(player, ai):
    if player == ai:
        return print(f"{Fore.MAGENTA} Its a Tie")
    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        return print(f"{Fore.GREEN}Congratulations, you win! ")
        
    else:
        return print(f"{Fore.GREEN} AI win! ")

def play_game():
    print(f"{Fore.BLUE}Welcome to Rock, Paper, Scissors Game")
    

    player = input(f"{Fore.YELLOW}Your choice rock/paper/scissor: ").lower()

    if player not in ["rock", "paper", "scissors"]:
        print(f"{Fore.RED} Invalid choice! Please try again.")
        return

    ai = ai_choice()

    print("AI chose:", ai)
    print(decide_winner(player, ai))
    


play_game()
