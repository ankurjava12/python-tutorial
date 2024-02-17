# num = int(input("Enter a number : "))
# temp = num
# sum = 0
# while num > 0:
#     rem = num % 10
#     sum = sum * 10 + rem
#     num = num //10
# if temp == sum:
#     print(temp, "is a palindrome number.")
# else:
#     print(temp, "is not a palindrome number.")

class Palindrome:
    def check_palindrome(self,number):
        number_str = str(number)
        return number_str == number_str[::-1]
obj = Palindrome()
print(obj.check_palindrome(121))
print(obj.check_palindrome(122))
print(obj.check_palindrome(123321))