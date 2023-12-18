# l=['abc','pqr','xyz']
# new_list=[]
# for i in l:
#     new_list.append(l.reverse())
# print(new_list)

# new_list_1=[l.reverse() for i in l]
# print(new_list_1)

name="sudham","prathamesh"
def reverse_string(l):
    return[name[::-1] for name in l]
print(reverse_string(name))