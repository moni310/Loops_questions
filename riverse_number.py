num=int(input("enter the number"))
riverse=0
while num!=0:
    r=num%10
    riverse=riverse*10+r
    num=num//10
print(riverse)