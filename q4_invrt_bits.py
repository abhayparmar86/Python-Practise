def invert(number, strt, end):
    for i in range(strt-1, end):
        number = (1<<i)^number
    
    print(number)

    rev_bin = []


    while(number > 0):
        rev_bin.append(number % 2)
        number = number // 2

    rev_bin.reverse()
    print(*rev_bin)


num = int(input("Enter number: "))
temp = num
bin_num = []

while(temp > 0):
    bin_num.append(temp % 2)
    temp = temp//2

bin_num.reverse()
print(*bin_num)

strt = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

invert(num, strt, end)
