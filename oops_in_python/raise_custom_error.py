num = int(input("enter a number between 10 to 20 : "))
if num<10 or num>20:
    raise ValueError("value should be between 10 and 20")
print(num)
    