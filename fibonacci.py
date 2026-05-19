q =  int(input("Enter A Number: "))
a = 0
b = 1
for i in range(q):
    print(a,end = " ")
    c = a+b
    a = b
    b= c
