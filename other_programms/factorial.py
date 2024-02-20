# Using loop
num = 5
result = 1
for i in range(1,num+1):
    result *= i
print(result)
    



# Using recursion --
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))