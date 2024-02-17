str = input("Enter the string : ").lower().replace(" ","")

count_vowels = 0
count_consonants = 0

list = ['a','e','i','o','u']

for i in range(len(str)):
    if str[i] in list:
        count_vowels += 1
    else:
        count_consonants += 1

print("Number of vowels in string is : ",count_vowels)
print("Number of consonants in string is : ",count_consonants)