# Write a python program to reverse the given number in most efficient way. 

num = int(input("Enter the number to be reversed: "))

num_arr = []

while(num > 0):
    num_arr.append(num%10)
    num = num // 10

for i in num_arr:
    print(i, end = '')