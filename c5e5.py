def common_elements(l1,l2):
    common=[]
    for i in l1:
        if i in l2:
            common.append(i)
    return common


print(common_elements([1,2,3,4], [1,3,5,2]))