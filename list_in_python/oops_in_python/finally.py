# try:
#     list = [1,2,3,4]
#     i = int(input("enter a number : "))
#     print(list[i])
# except Exception as e:
#     print(e)
# finally:
#     print("I am always executed.")



def func():
    try:
        list = [1,2,3,4]
        i = int(input("enter a number : "))
        print(list[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("I am always executed.")
func()