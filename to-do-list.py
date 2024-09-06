import random

def roll_dice():
    min_num = 1
    max_num = 6
    result = random.randint(min_num, max_num)
    return result

while True:
    num_players = input("Enter number of players (2 - 4): ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            break
        else:
            print("The number of players must be between 2 and 4.")
    else:
        print("Invalid input, please try again.")

target_score = 50
scores = [0 for _ in range(num_players)]

while max(scores) < target_score:
    for i in range(num_players):
        print("\nPlayer", i + 1, "it's your turn!")
        print("Current score:", scores[i], "\n")
        turn_score = 0

        while True:
            roll_choice = input("Do you want to roll the dice (y)? ")
            if roll_choice.lower() != "y":
                break

            roll_result = roll_dice()
            if roll_result == 1:
                print("You rolled a 1! Turn ends now.")
                turn_score = 0
                break
            else:
                turn_score += roll_result
                print("You rolled:", roll_result)
                print("Turn score:", turn_score)

        scores[i] += turn_score
        print("Your total score:", scores[i])

highest_score = max(scores)
winner_index = scores.index(highest_score)
print("Player", winner_index + 1, "wins with a score of:", highest_score)
