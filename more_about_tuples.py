mixed=(1,2,3,4,5)
for i in mixed:
    print(i)


nums=(1)
print(type(nums))
nums1=(2,)
print(type(nums1))
words=("dhruv")
print(type(words))
words1=("prathamesh",)
print(type(words1))


guitars='yamaha','its me','dhurv'
print(type(guitars))


names=("monu","prathamesh","sudham")
name1,name2,name3=(names)
print(names[1])


lists=("monu",["prathamesh",97])
print(lists)
lists[1].pop()
print(lists)
lists[1].append(77)
print(lists)


print(min(mixed))
print(max(mixed))