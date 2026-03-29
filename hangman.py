import random 

words = ["python", "coding", "computer", "data", "algorithm"]
word = random.choice(words).upper()  
guessed = ["_"] * len(word) 
wrong = 0 
max_wrong = 6 
 
print("Hangman! Guess the word (one letter at a time).") 
while wrong < max_wrong and "_" in guessed:
    print(" ".join(guessed))
    letter = input("Guess a letter: ").upper()
    
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        wrong += 1
        print(f"Wrong! {max_wrong - wrong} tries left.")

if "_" not in guessed:
    print(f" You win! Word: {''.join(guessed)}")
else:
    print(f" Game over! Word was: {word}")
