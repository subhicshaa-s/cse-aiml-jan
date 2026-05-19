n = int(input("Enter a number: "))
count_even =0
count_odd = 0
for i in range(1,n + 1):
    if i%2==0:
        count_even = count_even+i
for i in range(1,n+1):
    if i%2!=0:
        count_odd = count_odd+i
print(f"The number of odd digits {count_odd}")
print(f"The number of even digits {count_even}")
