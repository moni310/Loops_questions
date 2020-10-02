i=1
a=5
while i<=5:
    guess=int(input("enter the number"))
    if a>guess:
        print("your number is lesser than me")
    elif a<guess:
        print("your number is greater than me")
    elif a==guess:
        print("congratulation,you got it")
    i=i+1