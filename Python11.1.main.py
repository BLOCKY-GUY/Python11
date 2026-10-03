rows = int(input("Please Enter the total Number of Rows: "))
print("Floyd's Triangle")

number = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(f"{number} ", end="")
        number += 1
    print()