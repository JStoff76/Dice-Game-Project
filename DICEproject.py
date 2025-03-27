#import a random
import random

#getting player variables, number of reps, and game type
p1_bank = float(input("Enter Player 1 starting amount: "))
p2_bank = float(input("Enter Player 2 starting amount: "))
reps = float(input("Enter number of replications: "))
rounds = 0

# Establishing fair and Unfair probabalities and Errors for criteria


while True: 
    game_type = input(str("Dice probabilities: fair or unfair: "))
    if game_type in "fair":
        dice_probability = [1/6] * 6
        break
    else:
        if game_type == "unfair":
            while True:
                unfair_input = input("enter 6 values that add to 1 in format 0.__ :")
                dice_probability = []
                for p in game_type.split(","):
                    dice_probability.append(float(p.strip()))
                if len(dice_probability) == 6 and abs(sum(dice_probability) == 1):
                    break 
                else:
                    print(("Error please enter 6 comma seperated values that add to 1: "))  
                    break

#establish the necessary variables for ending statistics

p1_endtotal = 0
p2_endtotal = 0
p1_max_total = 0
p2_max_total = 0
p1_wins = 0
p2_wins = 0
total_rounds = 0

#running the game
reps = int(reps)
for i in range (reps):
    p1_money = p1_bank
    p2_money = p2_bank
    p1_max = p1_money
    p2_max = p2_money
    rounds = 0

    # Random dice rolls result in additon or subtraction from the players bank 
while p1_money > 0 and p2_money > 0:   
    rounds += 1
    roll1 = random.choices([1,2,3,4,5,6], weights = dice_probability)[0]
    if roll1 <= 3:
        p1_money -= min(roll1, p1_money)
        p2_money += min(roll1, p1_money)
    else:
        win_amount = min(roll1-3, p2_money)
        p1_money += win_amount
        p2_money -= win_amount
        p1_max_total = max(p1_max_total, p1_money)
        p2_max_total = max(p2_max_total, p2_money)

    if p1_money <= 0 or p2_money <= 0:
        break

    # use random rolls to get the dice roll result

    roll2 = random.choices([1,2,3,4,5,6], weights = dice_probability) [0]
    if roll2 <= 3:
        p2_money -= min(roll2, p2_money)
        p1_money += min(roll2, p2_money)
    else:
        win_amount = min(roll2-3, p1_money)
        p2_money += win_amount
        p1_money -= win_amount
        p2_max_total = max(p2_max_total, p2_money)
        p1_max_total = max(p1_max_total, p1_money)

    if p1_money <= 0 or p2_money <= 0:
        break
    
        
        rounds += 1
        
    # Keeping track of total money earned over X anount of reps
    
p1_endtotal += p1_money
p2_endtotal += p2_money
p1_max_total += p1_max
p2_max_total += p2_max
total_rounds += rounds

if p1_money > 0:
         p1_wins += 1
else:
         p2_wins += 1






# Compute the averages and probabilities
avg_end_player1 = p1_endtotal / reps
avg_end_player2 = p2_endtotal / reps
avg_max_player1 = p1_max_total / reps
avg_max_player2 = p2_max_total / reps
prob_player1_win = 100 * p1_wins / reps
prob_player2_win = 100 * p2_wins / reps
avg_rounds = total_rounds / reps

# Display the statistics
print(f"Average ending amount for Player 1: ${avg_end_player1:.2f}")
print(f"Average ending amount for Player 2: ${avg_end_player2:.2f}")
print(f"Average highest amount that Player 1 achieves: ${avg_max_player1:.2f}")
print(f"Average highest amount that Player 2 achieves: ${avg_max_player2:.2f}")
print(f"Probability that Player 1 wins a game: {prob_player1_win:.2f}%")
print(f"Probability that Player 2 wins a game: {prob_player2_win:.2f}%")
print(f"Average number of rounds per game: {avg_rounds:.2f}")


