import random

secret_number = str(random.randint(1000, 9999))
game_won = False
attempts = 0

while not game_won:
    correct_positions = 0
    correct_numbers = 0

    guess = input("Enter your 4-digit guess: ")

    if guess.lower() == "help":
        game_won = True
        break

    for index in range(4):
        if secret_number[index] == guess[index]:
            correct_positions += 1
        elif secret_number[index] in guess:
            correct_numbers += 1

    if correct_positions == 4:
        game_won = True
    else:
        attempts += 1
        print(
            f"Correct position: {correct_positions} | "
            f"Correct number, wrong position: {correct_numbers}"
        )

print(f"You got it in {attempts} attempts! The number was {secret_number}.")
