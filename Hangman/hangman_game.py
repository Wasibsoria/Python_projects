import random
kelimeler=["apple", "bridge", "camera", "desktop", "elephant", 
    "forest", "guitar", "horizon", "island", "jungle", 
    "keyboard", "library", "mountain", "network", "ocean", 
    "phoenix", "quartz", "rhythm", "sunshine", "treasure"]

#kelime seçme ve boşluk tanımlama
selected_sequence = random.randint(0,19)
selected_word = kelimeler[selected_sequence]
empty_bars = len(selected_word)
bars = []
chance = 6

for i in range(empty_bars):
    bars.append("_")
print(bars)

while chance > 0 and "_" in bars:
    
    guess = input(f"Enter a letter (Chances left {chance}): ").lower()
    
    if guess in selected_word:
        for j in range(len(selected_word)):
            if selected_word[j] == guess:
                bars[j] = guess
        print("Right choice!")
        print(bars)
    else:
        chance -= 1
        def hangman():
            match chance:
                case 5:
                    print("Wrong Guess!")
                    print("  O  ")              

                case 4:
                    print("Wrong Guess!") 
                    print("  0\n |  ")

                case 3:
                    print("Wrong Guess!")  
                    print("  0\n /|  ")
                case 2:
                    print("Wrong Guess!")
                    print("  O\n /|\\ ")
                case 1:
                    print("Wrong Guess!")
                    print("  O\n /|\\\n /   ")
                case 0:
                    print("Wrong Guess!")
                    print("  O\n /|\\\n / \\ ")

             
        hangman()     
        print("Wrong choice!")
if chance > 0:
    print(bars)



if "_" not in bars:
    print("You Win!")
else:
    print(f"You Lose!, Word was: {selected_word}")
