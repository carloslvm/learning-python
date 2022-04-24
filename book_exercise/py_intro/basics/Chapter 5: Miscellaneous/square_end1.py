#!/usr/bin/python3

# Count how many of the squares of the numbers from
# 1 to 100 end in a 1.

count = 0
for calculate in range(1, 101):
    if (calculate**2) % 10 == 1:
        count += 1

print(count)
