for i in range(11):
    print(i,end=" ")




def fibonacci_sequence(n):
    a,b=0,1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

user_input=int(input("\nenter a number: "))
fibonacci_sequence(user_input)