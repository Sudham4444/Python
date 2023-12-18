import random
random_number=random.randint(1, 100)
#
winning_number=random_number
guessed_number=1
game_over=False
while True:
    guess_number= int(input("guess the number between 1 to 100: "))
    if winning_number==guess_number:
        print(f"you win!!, and you gusssed this number in {guessed_number} times")
        break
    else:
        if guess_number<winning_number:
            print("too low")
        else:
            print("too high")
        guessed_number+=1
