def reverse_list(l):
    l.reverse()
    return l
numbers=[1,2,3,4]
print(reverse_list(numbers))




def reverse_list1(l1):
    return l1[::-1]
numbers1=[1,2,3]
print(reverse_list1(numbers1))



def reverse_list2(l2):
    r_list=[]
    for i in range(len(l2)):
        popped_item=l2.pop()
        r_list.append(popped_item)
    return r_list
numbers2=[1,2]
print(reverse_list2(numbers2))
