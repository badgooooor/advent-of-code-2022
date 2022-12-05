priority_sum = 0
with open('input.txt') as inputfile:
    for line in inputfile:
        first_conpartment, second_conpartment = set(line[:len(line)//2]), set(line[len(line)//2:])
        intersected_conpartment = list(first_conpartment.intersection(second_conpartment))[0]
        priority_ord = ord(intersected_conpartment)
        if priority_ord <= 90:
            priority = priority_ord - 38
        else:
            priority = priority_ord - 96
        print(intersected_conpartment, priority)

        priority_sum += priority

print('Total :', priority_sum)
