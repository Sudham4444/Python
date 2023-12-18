def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed=[1,2,3,[23,45,6,[2,3,4,5]],3434,43,[34,4,5]]
print(sublist_counter(mixed))