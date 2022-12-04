f = open("input.txt", "r")

score_count = 0

selected_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

compete_score = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    }
}

for item in f:
    splited_key = item.split()
    score_count = score_count + selected_score[splited_key[1]] + compete_score[splited_key[0]][splited_key[1]]
    print('Count', score_count)

print('Total score: ', score_count)
