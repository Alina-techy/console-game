import random

print("Welcome! Guess a number between 1-100.")
secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret:
            print("🔼 Too low! Try higher.")
        elif guess > secret:
            print("🔽 Too high! Try lower.")
        else:
            print(f"🎉 Correct! Got it in {attempts} tries!")
            break
    except ValueError:
        print("Enter a valid number!")
