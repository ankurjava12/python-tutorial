def fav(n):
    if n <= 1:
        return n
    else:
        return fav(n-1)+fav(n-2)

def print_fav(n):
    if n <= 0:
        print("Please enter positive integer")
    else:
        for i in range(n):
            print(fav(i))

print_fav(11)

