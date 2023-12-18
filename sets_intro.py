s={1,2,3,4,3,2}
print(s)
l=[1,2,34,34,21,2,5,6,67,8,89,9,8]
s2=list(set(l))
print(s2)

s.add(5)
print(s)
s.remove(1) #give error if element not present
print(s)
s.discard(78) #dont give error if element not present
print(s)

print(l.clear())

print(s)
s1=s.copy()
print(s1)