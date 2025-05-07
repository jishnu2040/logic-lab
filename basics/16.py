lst =[43, 3, 5, 6, 7, 8, 9, 10]
num = int(input("Enter a number in this list: "))
for i in lst:
    if i == num:
        print("index of the number is ", lst.index(i))