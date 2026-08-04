EPSILON = 1e-9

def calculate_mac(pattern, filter_data):
    score = 0.0

    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            score += pattern[row][col] * filter_data[row][col]

    return score

def compare_scores(score_a, score_b, label_a, label_b):
    difference = abs(score_a - score_b)

    if difference < EPSILON:
        return "UNDECIDED"

    if score_a > score_b:
        return label_a

    return label_b
