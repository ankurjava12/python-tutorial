# 
list = [1,2,3,4,5]
print(list)
print(type(list))


# 
l = [1,2,3,4,5,"Ankur Singh","Aditya Mishra"]
if 1 in l:
    print("Yes")
else:
    print("No")
    
if "Ank" in "Ankur Singh":
    print("Yes")
else:
    print("No")


# 
l = [1,2,3,4,5,"Ankur Singh","Aditya Mishra"]
if "Ank" in "Ankur Singh":
    print("Yes")
else:
    print("No")


# 
l = [1,2,3,4,5,"Ankur Singh","Aditya Mishra"]
print(l[:])
print(l[1:4])
print(l[2:-1])
print(l[:3])


# list comprehension
lst = [i for i in range(10)]
print(lst)


# list comprehension with conditon
lst = [i for i in range(10) if i%2 == 0]
print(lst)


# 
l = [1,2,3,4,5,7,5,8,3,8,3,6,89,0,8,6]
l.sort()
print(l)