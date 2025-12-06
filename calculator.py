a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
operator = str(input("Enter the operator to be done:"))
if (operator == "+"):
    c = a+b
    print(c)
elif (operator == "-"):
    d = a-b
    print(d)
elif (operator == "/"):
    e = a/b
    print(e)
elif (operator == "*"):
    f = a*b
    print(f)
else:
    print("Invalid operator")
