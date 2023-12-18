def cube_finder(l):
    cube={}
    for i in range(1,l+1):
        cube[i]=i**3
    return cube
user_input=int(input("enter a number: "))
print(cube_finder(user_input))
