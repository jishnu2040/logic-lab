grp = [33, 2, 4, 5, 6, 7, 8, 9, 10, 4, 4, 22, 59]

check = 4
count = 0

for i in grp:
    if i == check:
        count += 1

print(f"Count of {check} in the list is: {count}")