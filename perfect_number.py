i=1
sum=0
num=int(input("enter the number"))
while i<num:
    if num%i==0:
        perfect=i
        sum=sum+perfect
    i=i+1
if num==sum:
    print(num,"it is perfect number")
else:
    print(num,"it is not perfect number")
