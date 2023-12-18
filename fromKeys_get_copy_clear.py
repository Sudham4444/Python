# d={"name":"unknown","age":"unknown"}
d=dict.fromkeys(["name","age","height"],"unknown") #instead of list you can also use tuple
print(d)

d1=dict.fromkeys(range(1,11),"unknown")
print(d1)


d2={"name":"prathamesh","age":20}
print(d2["name"])
print(d2.get("age"))

# print(d2["names"])  #gives error (to handle this we use get methid)
print(d2.get("names"))

if "name" in d2:
    print("present")
else:
    print("not present")

if d.get("name"):    #if None --->False, else---->True
    print("present")
else:
    print("not present")

d3=d2.copy()


print(d3 is d2) #checks in memory
print(d3==d2) #because equals checks key values


print(d3)
print(d3.popitem())
print(d2)

print(d2)
d2.clear()
print(d2)