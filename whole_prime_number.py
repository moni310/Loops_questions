num=1
while num<=100:
    count=0
    i=2
    while i<=num//2:
        if num%i==0:
            print(num,"not prime")
            count=count+1
            break
        i=i+1
    if count==0 and num !=1:
        print(num,"prime&&&&&&&&&&&&&&&&&&&")
    num=num+1
