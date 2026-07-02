import random

choices = ["rock", "paper", "scissors"]
score_player = 0
score_computer = 0

print("✊ Rock-Paper-Scissors! Type 'quit' to exit.")
print("Rock beats scissors, paper beats rock, scissors beats paper.")

while True:
    player = input("\nYour choice (rock/paper/scissors): ").lower()
    
    if player == "quit":
        print(f"\nFinal score: You {score_player} - Computer {score_computer}")
        break
    
    if player not in choices:
        print("❌ Invalid! Choose rock, paper, or scissors.")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("🤝 Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("✅ You win!")
        score_player += 1
    else:
        print("❌ Computer wins!")
        score_computer += 1
        
        
