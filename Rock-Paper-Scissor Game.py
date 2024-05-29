import random

print("-----------PLAY ROCK PAPER SCISSOR----------")

while True:
    print("\n     RULES\nEnter 0 for Rock\n      1 for Paper\n      2 for Scissor\n      3 to End the Game\n")
    
    user=int(input('Enter your choice : '))
    if user==3:
        print("\nThe game has been ended successfully.")
        break
    
    if user>=0 and user<=2:
        choices = ['Rock','Paper','Scissor']
        print(f"\nYou've chosen {choices[user]}")
        
        computer=random.randint(0,2)
        print(f"Computer has chosen {choices[computer]}\n")
        
        if (user==0 and computer==2) or (user>computer):
            print('You win')
        elif (user==2 and computer==0) or (user<computer):
            print('You lose')
        else:
            print("It's a draw")
    else:
        print("Invalid input")
