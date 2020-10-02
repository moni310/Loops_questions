num=101010101
i=9
while i<=num:
    print(" "*(9-i),end=" ")
    num=num//100
    print(num)
    i=i-1