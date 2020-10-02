a=5
i=1
while i<=5:
    guess_num=int(input("number"))
    if a==guess_num:
        print("congratulation,you are winner")
        break;
    else:
        print("guess again")
    i=i+1
