number=input("enter a number cotaining more than one digit: ")
total=0
i=0
while i<len(number):
    total+=int(number[i])
    i+=1
print("your total is: " ,total)