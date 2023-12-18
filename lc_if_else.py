new_list_1=[]
for i in range(1,11):
    if i%2==0:
        new_list_1.append(i*2)
    else:
        new_list_1.append(-i)
print(new_list_1)



new_list=[j*2 if j%2==0 else-j  for j in range(1,11)]
print(new_list)



