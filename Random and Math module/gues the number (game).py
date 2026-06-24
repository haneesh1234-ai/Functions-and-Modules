import random
print("Welcome! Guess the number between 1 and 10.")
computer = random.randint(1,10)
game = True
while game :
    try :
        guess = int(input("enter your guess : "))
        if guess >= 1 and guess <= 10 :
            if guess > computer :
                print("your are high")
            elif guess < computer :
                print("you are to low")
            elif guess == computer :
                print(" you win!!!")
                print("computer generate : ", computer)
                game = False 
                break
        else :
            print("number is not in the range")    
    except ValueError :
        print("invalid input ")