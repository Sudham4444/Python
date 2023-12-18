def last_char(name):
    return name[-1]
print(last_char("sudham")) 


def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

number=int(input("enter a number: "))
print(number, "is an",odd_even(number),"number ")




def is_even(number):
    if number%2==0:
        return True
    return False

num1=int(input("enter a number: "))
print(is_even(num1))



def is_even_1(number1):
    return number1%2==0
num2=int(input("enter a number: "))
print(is_even_1(num2))



def sentence():
    return "happy birthday sudham"
print(sentence())

