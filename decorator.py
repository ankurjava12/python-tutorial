def greet(func):
    def mfunc(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Thanks for using this function")
    return mfunc

# decorator uses with xero positional arguements
@greet
def hello():
    print("Hello World")
hello()

# decorator uses with two positional arguements

@greet
def add(a,b):
    print(a+b)
add(11,12)

# greet(add)(11,12)