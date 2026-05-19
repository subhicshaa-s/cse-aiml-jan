a = int(input("Enter A Number:"))
flag = True
if a<=1:
    flag = False
else:
    for i in range(2,a):
        if num%i==0:
            flag = False
            break
if flag:
    print("Prime")
else:
    print("Not A Prime")
