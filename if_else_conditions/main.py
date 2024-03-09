# correct email is abc@gmail.com
# correct password is abc@123

email = input("Enter your email : ")
if '@' in email:
    password = input("Enter your passwprd : ")
    if email == 'abc@gmail.com' and password == 'abc@123':
        print("Welcome")
    elif email == 'abc@gmail.com' and password != 'abc@123':
        print("Incorrect password")
        password = input("Enter your password again : ")
        if password == 'abc@123':
            print("Welcome")
        else:
            print("Again your password is incorrect")
    else:
        print("Invailid Credential")
else:
    print("Incorrect your email")
    email = input("Enter your email agian : ")
    if email == 'abc@gmail.com':
        password = input("Enter your passwprd : ")
        if email == 'abc@gmail.com' and password == 'abc@123':
            print("Welcome")
        elif email == 'abc@gmail.com' and password != 'abc@123':
            print("Incorrect password")
            password = input("Enter your password again : ")
            if password == 'abc@123':
                print("Welcome")
            else:
                print("Again your password is incorrect")
        else:
            print("Invailid Credential")
    else:
        print("Incorrect email again")