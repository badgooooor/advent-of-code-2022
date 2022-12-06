with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

text = lines[0]

def find_first_index(offset):
    for i in range(0, len(text) - offset):
        substring_set = set(text[i:i+offset])

        if len(substring_set) == offset:
            print(text[i:i+offset],substring_set, i, i + offset)
            first_index = i + offset
            return first_index

print('Answer : ', find_first_index(4))
print('Answer : ', find_first_index(14))