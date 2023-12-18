import random
random_number=random.randint(1, 100)
#
winning_number=random_number
guess_number= int(input("guess the number between 1 to 100: "))
guessed_number=1
game_over=False
while not game_over:
    if winning_number==guess_number:
        print(f"you win!!, and you gusssed this number in {guessed_number} times")
        game_over=True
    else:
        if guess_number<winning_number:
            print("too low")
            guessed_number+=1
            guess_number=int(input("guess the number again: "))
        else:
            print("too high")
            guessed_number+=1
            guess_number=int(input("guess the number again: "))
