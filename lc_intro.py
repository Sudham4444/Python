squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

square2=[i**2 for i in range(1,11)]
print(square2)


negative=[]
for j in range(1,11):
    negative.append(-j)
print(negative)

negative1=[-j for j in range(1,11)]
print(negative1)



names=['sudham','prathamesh']
new_list=[]
for k in names:
    new_list.append(k[0])
print(new_list)

new_list_2=[l[0] for l in names]
print(new_list_2)