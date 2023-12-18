numbers=list(range(1,11))
print(numbers)

even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(list(even))


even_nums=[j for j in numbers if j%2==0]
print(list(even_nums))
even_nums_1=[k for k in range(1,11) if k%2==0]
print(list(even_nums_1))

odd_nums=[k for k in numbers if k%2!=0]
print(odd_nums)
odd_nums_1=[l for l in range(1,11) if l%2!=0]
print(odd_nums_1)