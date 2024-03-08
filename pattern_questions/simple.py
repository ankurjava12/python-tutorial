def print_pattern(rows,cols):
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        print()
print_pattern(5,5)