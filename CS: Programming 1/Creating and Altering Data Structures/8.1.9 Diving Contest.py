# fill in this function to return the total of the three judges' scores!
def calculate_score(judge_scores):
    score = judge_scores[0] + judge_scores[1] + judge_scores[2]
    return score

calculate_score((10, 10, 10))
# => 30

calculate_score((9, 9, 6))
# => 24
