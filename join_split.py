#split
user_info="sudham 44".split()
print(user_info)
user_info1="prathamesh,77".split(",")
print(user_info1)

name,age=input("enter your name and age comma seperated: ").split(",")
print(name, age)


#join
user_info3=["babbu","20"]
print(",".join(user_info3))