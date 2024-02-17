n = int(input("enter a number : "))
arr = []
for i in range(n):
    element = int(input("enter the arry element : "))
    arr.append(element)
    avg = sum(arr)/len(arr)
print(arr)
print("Average of the array element",avg)