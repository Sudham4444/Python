user_info={
    "name":"babbu",
    "age":20,
    "fav_movie":"harry potter"
}

user_info["sex"]="male"
print(user_info)

popped_item = user_info.pop("fav_movie")
print(f"popped item is {popped_item}")
print(user_info)
print(type(popped_item))


popped_item_1=user_info.popitem()
print(user_info)
print(popped_item_1)
print(type(popped_item_1))