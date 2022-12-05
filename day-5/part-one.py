from collections import deque
import re
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

# Create stack from section in input
def create_stack(lines):
    stack = [deque() for x in range(9)]
    stack_lines = lines[0:8]
    crate_and_index = []

    for line in stack_lines:
        # Get crates in stack and where should the crate be.
        crate_and_index_line = [(int(i / 4), line[i:i+2].replace('[','')) for i in findall('[', line)]
        crate_and_index.append(crate_and_index_line)

    crate_and_index.reverse()

    for row in crate_and_index:
        for item in row:
            stack_idx, crate = item[0], item[1]
            stack[stack_idx].append(crate)
    
    return stack

def parse_command(command):
    numbers = re.findall('[0-9]+', command)
    return [int(x) for x in numbers]

# Move the crates by commands
def move_crates(lines, stack):
    for line in lines:
        [crates_to_move, from_stack, to_stack] = parse_command(line)
        temp_crate = []

        for x in range(crates_to_move):
            temp = stack[from_stack - 1].pop()
            temp_crate.append(temp)
        for crate in temp_crate:
            stack[to_stack - 1].append(crate)
    
    return stack

# DEBUG: Use for display
def print_stack(title, stack):
    print(title)
    for stack_line in crate_stack:
        print(stack_line)
    print('\n')

# Get answer by top of the stack
def print_top(stack):
    answer = []
    for line in stack:
        answer.append(line[-1])
    return answer

crate_stack = create_stack(lines)
print_stack('Created stack', crate_stack)

moved_stack = move_crates(lines[10:], crate_stack)
print_stack('Moved stack', moved_stack)

answer = print_top(moved_stack)
print('Result : ', answer)