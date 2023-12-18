import random
random_number=random.randint(0, 10)
print(random_number)
winning_number=random_number
guess_number= int(input("guess the number between 0 to 10: "))
if winning_number==guess_number:
    print("you win!!")
else:
    if guess_number<winning_number:
        print("too low")
    else:
        print("too high")
