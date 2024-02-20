class Main:
    def reverse(self, number):
        reverse_str = str(number)
        return reverse_str[::-1]
obj = Main()
print(obj.reverse(123))
print(obj.reverse(123456789))


# class Main:
#     def reverse(self, number):
#         sum = 0
#         while number > 0:
#             reminder = number % 10
#             sum = sum * 10 + reminder
#             number = number // 10
#         return sum
# obj = Main()
# print(obj.reverse(123))
# print(obj.reverse(123456789))