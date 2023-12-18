def  three_numbers(num_1,num_2,num_3):
    if num_1>num_2 and num_1>num_3:
        return num_1
    elif num_2>num_3 and num_2>num_1:
        return num_2
    else:
        return num_3
user_input_1=int(input("enter first number: "))
user_input_2=int(input("enter second number: "))
user_input_3=int(input("enter third number: "))
print(three_numbers(user_input_1,user_input_2,user_input_3) ,"is greater")