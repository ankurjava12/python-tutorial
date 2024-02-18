# n = int(input("enter a number : "))
# arr = []
# for i in range(n):
#     element = int(input("enter the arry element : "))
#     arr.append(element)
#     avg = sum(arr)/len(arr)
# print(arr)
# print("Average of the array element",avg)


# 
# def avg_arr(len_arr):
#     arr=[]
#     for i in range(len_arr):
#         element=int(input("Enter a array element : "))
#         arr.append(element)
#     avg = sum(arr)/len(arr)
#     print(f"The avrage of array element is : {avg}")



# len_arr = int(input("Enter the length of array: "))

# avg_arr(len_arr)

def create_arr(len_arr):
    arr=[]
    for i in range(len_arr):
        element=int(input("Enter a array element : "))
        arr.append(element)
    
def avg_arr(arr):
    for i in range(len_arr):
        avg = sum(arr)/len(arr)
    print(f"The avrage of array element is : {avg}")

len_arr = int(input("Enter the len of array : "))
arr = create_arr(len_arr)
avg_arr(arr)
