string="prathamesh"
print(string[2])
print(string[0:5:2])
print(string[-1::-1])

name=input("enter your name: ")
age=int(input("enter your age: "))
print("hello",name,"your age is - ",age)


name_1,age_1=input("enter your name and age comma seperated: ").split(",")
print("hey",name,"you are ",age, "years old")

print(len(string))
print(string.lower())
print(string.upper())
print(string.title())

print(string.find("a"))
a_position_1=string.find("a")
print(a_position_1)
a_position_2=string.find("a",a_position_1+1)
print(a_position_2)


print(string.center(12,"*"))

print(string.replace("s", "S"))
print(string.replace("a", "A",1))
print(string)
