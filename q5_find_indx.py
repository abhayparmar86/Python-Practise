size = int(input("Enter size of Array: "))
arr = []

for i in range(size):
    elem = int(input())
    arr.append(elem)

print(*arr)

find_num = int(input("Enter element to be found: "))

for i in range(size):
    if arr[i] == find_num:
        print(f"Element found at {i}")
        break
    
print("Element not found!")