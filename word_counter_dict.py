def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count

user_input=input("enter a name: ")
print(word_counter(user_input))