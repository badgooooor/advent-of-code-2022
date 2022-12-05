pair_count = 0

def array_string_to_array_int(array_string):
    return [int(x) for x in array_string.split('-')]

def check_overlap(task_one_number, task_two_number):
    set1 = set(range(task_one_number[0], task_one_number[1] + 1))
    set2 = set(range(task_two_number[0], task_two_number[1] + 1))
    return len(set1.intersection(set2)) > 0


def check_contain(task_one_number, task_two_number):
    check_one_contain_two = task_one_number[0] <= task_two_number[0] and task_one_number[1] >= task_two_number[1]
    check_two_contain_one = task_one_number[0] >= task_two_number[0] and task_one_number[1] <= task_two_number[1]
    return check_two_contain_one or check_one_contain_two

with open('input.txt') as inputfile:
    for line in inputfile:
        task_one, task_two = line.split('\n')[0].split(',')
        task_one_number = array_string_to_array_int(task_one)
        task_two_number = array_string_to_array_int(task_two)
 
        if check_overlap(task_one_number, task_two_number) or check_contain(task_one_number, task_two_number):
            pair_count += 1

print('Total pair : ', pair_count)