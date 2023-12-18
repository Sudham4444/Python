user_info={
    "name":"babbu",
    "age":20,
    "fav_movie":"harry potter"
}

if "name" in user_info:
    print("present")
else:
    print("not present")

if "babbu" in user_info.values():
    print("present")
else:
    print("not present")




for i in user_info.values():
    print(i)

for i in user_info:
    print(user_info[i])



user_info_value=user_info.values()
print(user_info_value)
print(type(user_info_value))



user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))



user_items=user_info.items()
print(user_items)
print(type(user_items))



for key,value in user_info.items():
    print(f"key is {key} and value is {value}")