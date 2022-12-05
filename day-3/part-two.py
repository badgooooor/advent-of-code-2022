priority_sum = 0

with open("input.txt", "r") as f:
    rucksacks = [r.strip('\n') for r in f.readlines()]

groups = zip(*(iter(rucksacks),) * 3)

for group in groups:
    priority_char = list(set.intersection(*map(set, group)))[0]
    priority_ord = ord(priority_char)
    if priority_ord <= 90:
        priority = priority_ord - 38
    else:
        priority = priority_ord - 96
    
    priority_sum += priority
    print(priority_char, priority)

print('Total :', priority_sum)
