user_age=int(input("enter your age: "))
if user_age==0:
    print("you can't watch movie!!!")
elif 1<=user_age<=3:
    print("you can watch movie free!!")
elif 4<=user_age<=10:
    print("you ticket fair is $150!")
elif 11>=user_age<=60:
    print("your ticket fair is $250!")
else:
    print("your ticket fair is $200")