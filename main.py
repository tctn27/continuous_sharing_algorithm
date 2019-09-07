import os
import math

num_people = int(input("How many people are in the group? "))
damage = int(input("What's the total damage? "))
group_total = 0

rounding = False
if input("Would you like to use rounding? ").lower() == "yes":
    rounding = True

for player_instance in range(1, num_people + 1):
    print("\nPlayer " + str(player_instance))
    total = 0.0
    for iteration in range(0, 1000000000000):  # effectively infinite
        part = damage / (2 ** (iteration * (num_people) + player_instance))
        # equation: sum_over_iteration((damage/2^(iteration * (num_people + 1) + player_instance)))
        if rounding:
            part = math.floor(part)
        total += part
        if part == 0:  # don't waste computer time
            print("")
            break
        elif part >= 1 and iteration <= 10:
            print(part, end=" | ")

    group_total += total  # add total damage across all players

    print("Total damage to player " + str(player_instance) + ": " + str(total) + "\n")

print("Group total: " + str(group_total))
print("Damage mitigated: " + str(damage - group_total))

os.system("pause")
