tup1=[1,4,6,8,9,56,67]
tup1.sort(reverse=True)
print(tup1)
sum=0
for i in range(7):
    if tup1[i]%4!= 0:
        print(tup1[i])
        sum=sum+tup1[i]
print(sum)
