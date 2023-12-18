def greater(num_1,num_2):
    if num_1>num_2:
        return num_1
    return num_2

def new_greatest(num_1,num_2,num_3):
    #bigger=greater(num_1,num_2)
    return greater(greater(num_1,num_2),num_3)
num_1,num_2,num_3=input("enter three numbers: ").split(",")
print(int(new_greatest(num_1,num_2,num_3)),"is greater")