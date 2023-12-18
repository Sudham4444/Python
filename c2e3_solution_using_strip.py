name,character=input("enter your name and any single character with comma separated: ").split(",")
print("your count is : ",name.strip().lower().count(character.strip().lower()))