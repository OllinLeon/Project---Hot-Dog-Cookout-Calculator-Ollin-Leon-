import math

num_people = int(input("Enter the number of people attending the cookout: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

total_hotdogs = num_people * num_hotdogs_per_person

hotdogs_per_package = 10
buns_per_package = 8
num_hotdog_packages = (total_hotdogs + hotdogs_per_package - 1) // hotdogs_per_package
num_bun_packages = (total_hotdogs + buns_per_package - 1) // buns_per_package

leftover_hotdogs = (num_hotdog_packages * hotdogs_per_package) - total_hotdogs
leftover_buns = (num_bun_packages * buns_per_package) - total_hotdogs

print(f"Minimum number of packages of hot dogs required: {num_hotdog_packages}")
print(f"Minimum number of packages of hot dog buns required: {num_bun_packages}")
print(f"Number of hot dogs left over: {leftover_hotdogs}")
print(f"Number of hot dog buns left over: {leftover_buns}")