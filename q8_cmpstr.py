import q8_compstr

flag = 0
string1 = input("Enter String 1: ")
print(string1)

if string1.isspace():
    print("Nothing inside the string1...")
    flag = 1

# space1 = 0
# for i in string1:
#     if i == ' ':
#         space1 = space1 + 1

# if space1 == len(string1):
#     flag = 1

string2 = input("Enter String 2: ")
print(string2)

if string2.isspace():
    print("Nothing inside the string2...")
    flag = 1

# space2 = 0
# for i in string2:
#     if i == ' ':
#         space2 = space2 + 1

# if space2 == len(string2):
#     flag = 1

if flag == 0:
    q8_compstr.str_comp(string1, string2)

