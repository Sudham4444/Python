def nums_to_string(l):
    return[str(i)for i in l if (type(i)==int or type(i)==float)]
print(nums_to_string([True,False,[1,2,3],1,2,0,1.4,['1','2']]))