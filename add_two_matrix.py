def create_matrix(m,n):
    mat = []
    for i in range(m):
        rows =[]
        for j in range(n):
            input_num = int(input(f"Enter the value of mat[{i}][{j}] : "))
            rows.append(input_num)
        mat.append(rows)
    return mat

def add_mat(a,b):
    mat=[]
    for i in range(len(a)):
        rows=[]
        for j in range(len(a[0])):
            rows.append(a[i][j] + b[i][j])
        mat.append(rows)
    return mat

def print_mat(added_mat):
    for i in added_mat:
        for j in i:
            print(j,end=" ")
        print()

rows=int(input("Enter rows: "))
cols=int(input("Enter cols: "))

print("Enter the value of a")
a = create_matrix(rows,cols)
print("Enter the value of b")
b = create_matrix(rows,cols)

added_mat=(add_mat(a,b))
print_mat(added_mat)