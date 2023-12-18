def filter_odd_even(l):
    odd_numbers=[]
    even_numbers=[]
    for i in l:
        if i%2==0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    output=[odd_numbers,even_numbers]
    return output
numbers=[1,2,3,4,5,6,7,8,9]
print(filter_odd_even(numbers))