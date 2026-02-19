import secrets

choices = ["null" , "Rock" , "Paper" , "Scissors" ]

while True:

    try:
        user_input = int(input("Welcome to the game! Please choose what will you take\n\n 1-Rock , 2-Paper, 3-Scissors: "))
        
        if user_input not in [1, 2, 3]:
            print("Please enter a number between 1 and 3!")
            continue
    
    except ValueError:
        print("Invalid input! Please enter a number. ")
        continue

    print(f"You chose {choices[user_input]}, Now its computers turn... ")

    comp_input = secrets.choice(choices[1:])
    print(f"Computer chose {comp_input}!")
        #Draw
    if comp_input == "Rock" and user_input == 1 or comp_input == "Paper" and user_input == 2 or comp_input == "Scissors" and user_input == 3:
        print("Its a draw!")
        #Player win
    elif user_input == 1 and comp_input == "Scissors" or user_input == 3 and comp_input == "Paper" or user_input == 2 and comp_input == "Rock":
        print("You win! 🎉")
    else:
        print("You lose! 💀")


    play_again = input("Would you like to play again ? (y/n): ").lower()
    if play_again == "n":
        break
    elif play_again =="y":
        continue

print("Thanks for playing!")