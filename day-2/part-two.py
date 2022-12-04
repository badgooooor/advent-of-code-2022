total_score_part_2 = 0
scores_part_2 = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}

with open('input.txt') as inputfile:
    for line in inputfile:
        this_game = line.strip().split()
        total_score_part_2 += scores_part_2[this_game[0]][this_game[1]]

print(total_score_part_2)