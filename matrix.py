# mat = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]
# for i in mat:
#     for j in i:
#         print(j, end=" ")
#     print()


# Using function--
# def print_matrix(mat):
#     for i in mat:
#         for j in i:
#             print(j,end=" ")
#         print()

# mat = [
#     [1,1,1],
#     [2,2,2],
#     [3,3,3]
# ]

# print_matrix(mat)


# Enter matrix by user input--
def create_matrix(m,n):
    mat = []
    for i in range(m):
        rows =[]
        for j in range(n):
            input_num = int(input(f"Enter the value of mat[{i}][{j}] : "))
            rows.append(input_num)
        mat.append(rows)
    return mat

def show(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

rows = int(input("Enter rows : "))
cols = int(input("Enter cols : "))

# create_matrix(rows,cols)
show(create_matrix(rows,cols))


