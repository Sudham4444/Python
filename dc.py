# square={1:1,2:4,3:9}
square={num:num**2 for num in range(1,11)}
print(square)

square_1={f"square of {num} is":num**2 for num in range(1,11)}
# print(square_1)
for k,v in square_1.items():
    print(f"{k} : {v}")


string="prathamesh"
word_count={char:string.count(char) for char in string}
print(word_count)

