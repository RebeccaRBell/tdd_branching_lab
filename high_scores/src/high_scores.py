def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def top_three(scores):
    top = sorted(scores)
    return top[-1], top[-2], top[-3]


def high_to_low(scores):
    scores.sort(reverse = True)
    return scores