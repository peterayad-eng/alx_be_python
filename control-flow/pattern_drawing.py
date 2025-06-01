number = int(input("Enter the size of the pattern: "))
n = number
while number != 0:
    for i in range(n):
        print("*", end="")

    print("")
    number = number - 1

