with open("binfile.bin","wb") as file:
    num=[5,10,15,20,30]
    arr=bytearray(num)
    file.write(arr)