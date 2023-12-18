user_name=input("enter your name: ")
temp_var=""
i=0
while i<len(user_name):
    if user_name[i] not in temp_var:
        temp_var+=user_name[i]
        print(f"{user_name[i]}:{user_name.count(user_name[i])}")
    i+=1