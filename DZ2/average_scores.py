def average_scores(scores):
    if len(scores) == 0:
        return tuple()
    result = [0.0] * len(scores[0])
    for subject in scores:
        for student in range(len(subject)):
            result[student] += subject[student]
    return tuple(map(lambda a: a / len(scores), result))


if __name__ == "__main__":
    n, x = map(int, input().split())
    scores = [tuple(map(float, input().split())) for i in range(x)]
    print('\n'.join(map(str, average_scores(scores))))
