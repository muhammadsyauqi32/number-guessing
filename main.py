import random

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
""")

choose = True
while choose:       
    print("""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
      """)

    pil = int(input("Enter your choice: "))
    if pil == 1:
        level = 10
        dif = "Easy"
    elif pil == 2:
        level = 5
        dif = "Medium"
    elif pil == 3:
        level = 3
        dif = "Hard"
    else:
        print("Wrong Input!")

    print("Great! You have selected the ",dif, "difficulty level.")
    print("Let's start the game!")



    #Bot Generator
    bot = random.randint(1, 100)

    for i in range(0, level):
        ans = int(input("\nEnter your guess : "))
        if bot == ans:
            print("Congratulations! You guessed the correct number in",i+1, "attempts")
            break
        elif  bot < ans:
            print("Incorrect! The number is less than ", ans)
        elif bot > ans:
            print("Incorrect! The number is greater than ", ans)
    print("The Number is", bot)
    end = input("Play Again? (y/n) : ")
    if end.lower() == 'y':
        choose = True
    elif end.lower() == 'n':
        choose = False
        print("Thanks for Playing!")       