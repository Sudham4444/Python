s={"a","b","c"}
if "a" in s:
    print("present")
else:
    print("not present")

for item in s:
    print(item)

l=[1,2,3,4,5,4,5,6]
print(set(l))


s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1)

print(s1|s2)
print(s1&s2)
