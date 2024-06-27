# Write a python program to find 1's count in binary value of given integer number. 

num = int(input("Enter number: "))
temp = num
bin_num = []

while(temp > 0):
    bin_num.append(temp % 2)
    temp = temp//2

bin_num.reverse()
print(*bin_num)

count = 0

for i in bin_num:
    if i == 1:
        count = count + 1

print(f"There are {count} 1's")