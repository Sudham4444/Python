numbers=list(range(1,11))
print(numbers)


popped_item=numbers.pop()
print(popped_item)
print(numbers)


print(numbers.index(3))


def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))
