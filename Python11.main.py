print("Half Pyramid Patter of Star (*): ")
n = int(input("Enter the number or rows: "))

for i in range(n):
    for j in range(i + 1):
        print("* ", end ="")
    print()