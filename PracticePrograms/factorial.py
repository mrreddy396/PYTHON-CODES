print("enter vale" )
x=int(input())
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
#num=3
print(f"factorial of  is {factorial(x)}")
