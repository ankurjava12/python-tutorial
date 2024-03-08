def print_pattern(rows,cols):
    for i in range(rows):
        for j in range(cols):
            if j==0 or j==4:
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()
print_pattern(5,5)