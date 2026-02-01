import random

# 1. Define the Choices Array
choices = ["Rock", "Paper", "Scissors"]

# 2. Get Player Input
playerChoice = input("Please enter your choice (1: Rock, 2: Paper, 3: Scissors): ")
playerChoice = int(playerChoice)

# 3. Convert to Integer & 4. Error Handling
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3. Try again!")

else:
    # 5. Get Computer's Choice
    computerChoice = random.randint(1,3)

    # 6. Array Indexing & 7. Determine the winner (using if/elif/else)
    if playerChoice == computerChoice:
        print("Tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors: You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Scissors beats Paper: You win!")
    else:
        print("You lose!")
    # 8. String Comparison
    if playerChoice != 1:
        print("You didn't pick the classic Rock...")