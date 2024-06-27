# Write a Python program to find string length without using library function (strlen).
# .isnumeric() or .isdigit()
# special_characters = ""!@#$%^&*()-+?_=,<>/""
# s=input()
# # Example: $tackoverflow

# if any(c in special_characters for c in s):
#     print("yes")
# else:
#     print("no")

flag = 0

string = input("Enter string: ")
# print(string)

if string.isspace():
    print("Nothing inside the find string...")
    flag = 1

str_len = 0
special_characters = '''"!@#$%^&*()-+?_=,<>/"'''

for i in string:
    if i == ' ':
        print(f"Space found at position: {string.index(i)+1}")
        break
    elif i in special_characters:
        print(f"Special character encountered at: {string.index(i)+1}")
    elif i.isdigit():
        print(f"Number encountered at {string.index(i)+1}")
    str_len += 1

print("String length: ", str_len)
