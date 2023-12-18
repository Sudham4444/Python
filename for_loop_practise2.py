user_name=input("enter your name: ") 
temp=""
for i in range(len(user_name)):
    if user_name[i] not in temp:
        print(f"{user_name[i]}: {user_name.count(user_name[i])}")
        temp+=user_name[i]