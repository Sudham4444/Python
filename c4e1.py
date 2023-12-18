def  two_numbers(num_1,num_2):
    if num_1>num_2:
        return num_1
    return num_2
user_input_1=int(input("enter first number: "))
user_input_2=int(input("enter second number: "))
print(two_numbers(user_input_1,user_input_2) ,"is greater")