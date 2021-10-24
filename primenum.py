# user=int(input("enter the number--"))
# i=2
# while i<user:
#     if user%i==0:
#         print(user,"it is not  prime number")
#         break
#     i=i+1
# else:
#     print(user,"it is  prime number")



num=int(input("enter your number--"))
i=2
while i<=num:
    j=2
    c=0
    while j<i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==0:
        print(i)
    i=i+3



