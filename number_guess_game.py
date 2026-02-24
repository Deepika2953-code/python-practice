import random
correct = random.randint(1,50)
print("NUMBER GUESS GAME\n")
attempt = 5
print("GUESS THE CORRECT NUMBER PICKED BY THE COMPUTER\n")
print("Pick a number between 1 to 50\n")
print("\n")
while (attempt > 0):
    guess = int(input("Enter your guess:"))
    if guess==correct:
        print("You won! The correct number is ",correct)
        break
    elif guess<correct:
        print("Your number is less! Try again")
    else:
        print("Your number is high! Try again")
    attempt-=1
    print("Remaining attempts:",attempt)
if (attempt==0):
    print("You lost! The correct number is ",correct)
    
