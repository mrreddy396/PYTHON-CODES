m=0
flag=0
print("Enter a value")
n=int(input())
m=n/2
if n==0 or n==1:
    print(f"{n} is not prime number")
else:
    i=2
    while i<=m:
        i=i+1
        if n%i==0:
            print(f"{n} is not prime number")
            flag=1
            break
if flag==0:
    print(f"{n} is  prime number")

