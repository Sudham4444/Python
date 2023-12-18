user={}
name=input("enter your name: ")
age=int(input("enter your age: "))
city=input("enter your city: ")
sex=input("enter your sex: ")

user["name"]=name
user["age"]=age
user["city"]=city
user["sex"]=sex
print(user)

for key,value in user.items():
    print(f"{key}:{value}")
