# a = int(input("enter a number : "))
# b = int(input("enter a number : "))

# try:
#     c = a / b
#     print(c)
# except Exception as e:
#     print(e)
#     print("invailid input")
    
# print("end of the program")


# try:
#     num = int(input("enter a number : "))
#     print(num)
#     a = [1,2,3,4]
#     print(a[num])
# except ValueError:
#     print("value error")
# except IndexError:
#     print("index error")


try:
    num = int(input("enter a number to print their table : "))    
    for i in range(1, 11):
        print(f"{num} X {i} = {num *i}")
except:
    print("invailid input, Please input the integer")