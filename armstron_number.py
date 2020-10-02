num=int(input("enter the number"))
sum=0
i=0
b=num
while num>i:
     a=num%10
     var=a**3
     num=num//10
     sum=sum+var
if b == sum:
      print("it is armstrong ")
else:
      print("it is not armstrong")      
