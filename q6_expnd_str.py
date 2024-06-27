inp_str = input("Enter String to be expanded...")
length = len(inp_str)

for i in range(length):
    if inp_str[i] == '-' and i > 0 and i != length - 1:
        stt = ord(inp_str[i - 1])
        end = ord(inp_str[i + 1])

        for j in range(stt, end + 1): 
            print(chr(j), end='')
    # else:
    #     print(inp_str[i], end='') 
