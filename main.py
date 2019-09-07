import os
#  equation = sum_n((damage/2^(nc + p)))

c = int(input("How many people are in the group? "))
d = int(input("What's the total damage? "))
group_total = 0

for i in range(1, c + 1):
    print("\nPlayer " + str(i))
    total = 0.0
    for n in range(0, 1000000000000):
        part = d/(2**(n*(c + 1) + i))
        total += part
        if part == 0:
            break
        if n == 99:
            print(part)
        elif n % 20 == 0:
            print(part, end=" | ")

    group_total += total

    print("Total damage to player " + str(i) + ": " + str(total) + "\n")

print("Group total = " + str(group_total))

os.system("pause")
