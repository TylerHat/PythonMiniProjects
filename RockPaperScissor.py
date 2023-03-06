import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
comp_score = 0
user_score = 0

while True:
##def game(user_score, comp_score, player):
    computer = random.choice(choices)
    player = input("Rock or Paper or Scissors? ").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "beats", player)
            comp_score+=1
        else:
            print("You win!", player, "beats", computer)
            user_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "beats", player)
            comp_score+=1
        else:
            print("You win!", player, "beats", computer)
            user_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "beats", player)
            comp_score+=1
        else:
            print("You win!", player, "beats", computer)
            user_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{comp_score}")
        print(f"Plaer:{user_score}")


        