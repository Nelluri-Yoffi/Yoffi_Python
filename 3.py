import random
def play_game():
    words = ["python", "java", "coding", "computer", "programming"]
    password = random.choice(words)
    print("Guess the Password!")
    print("Hint: It's a programming-related word.")
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        attempts += 1
        if guess == password:
            print("🎉 You cracked it!")
            print("Attempts:", attempts)
            break
        elif len(guess) < len(password):
            print("Too short!")

        elif len(guess) > len(password):
            print("Too long!")

        else:
            print("Wrong password, but the length is correct!")

play_game()