first_num=int(input("enter the number"))
sec_num=int(input("enter the number"))
i=1
while i<=first_num and i<=sec_num:
    if first_num%i==0 and sec_num%i==0:
        hcf=i
        print(hcf)
    i=i+1
print(hcf,"is a hcf of first_num and sec_num")