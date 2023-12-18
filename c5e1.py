user_input=int(input("enter the range: "))
numbers=list(range(user_input))
print(user_input)




def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
print(square_list(numbers))



# def cube_list(m):
#     cube=[]
#     for j in m:
#         cube.append(j**3)
#     return cube
# print(cube_list(numbers))


def cube_list(m):
    cube=[]
    for j in m:
        cube.append(j**3)
    return cube
print(cube_list(numbers))