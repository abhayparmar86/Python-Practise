# Write a python program to find keyword/sub string from a given string. If sub string is available print "Search successful" otherwise print "Search Unsuccessful" 

flag = 0
space = 0

string1 = input("Enter the main String: ")
# print(string1)


if len(string1) == 0:
    print("Empty main string detected...")
    flag = 1

if string1.isspace():
    print("Nothing inside the main string...")
    flag = 1
    # space = space + 1
    
# if space == len(string1):
#     print("Nothing inside the string...")
#     flag = 1

find_str = input("Enter Sting to be found: ")
# print(find_str)


if len(find_str) == 0:
    print("Empty find string detected...")
    flag = 1

if find_str.isspace():
    print("Nothing inside the find string...")
    flag = 1


if flag == 1:
    print("\nEnter proper strings...")
else:
    if find_str in string1:
        print("Search Successful")
    else:
        print("search Unsuccessful")
