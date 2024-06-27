

def num_to_string(num):
    if num < 0:
        print("Number is negative, making it positive...")
        num = -num

    if num == 0:
        print("Zero")

    # print(num)

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];

    tenspart = (num % 100) // 10
    unitspart = num % 10

    if num >= 100000:
        num_to_string(num//100000)
        print("Lakh", end = ' ')
        num = num % 100000

    if num >= 1000:
        num_to_string(num // 1000)
        print("Thousand", end = ' ')
        num = num % 1000

    if num >= 100:
        num_to_string(num // 100)
        print("Hundred", end = ' ')
        num = num % 100

    if tenspart == 1:
        if unitspart > 0:
            print(teens[unitspart], end = ' ')
        else:
            print(tens[tenspart], end = ' ')
    else:
        if tenspart > 0:
            print(tens[tenspart], end = ' ')
        if unitspart > 0:
            print(units[unitspart], end = ' ')


num = int(input("Enter number: "))

num_to_string(num)