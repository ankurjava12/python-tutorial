def table(num):
    for i in range(1,11):
        if i == 4 or i == 1:
            i = "#"
        print(f"{num} X {i} = {num*i}")

table(9)