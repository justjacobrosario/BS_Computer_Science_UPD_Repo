def scores_needed(results):
    if len(results) == 0:
        return None
    else:
        return get_hanakos(results[0]), scores_needed(results[1:])

def get_hanakos(scores):
    return (60 * len(scores)) - sum(scores)

    """existing_scores = tuple(x for x in results)
    return existing_scores"""

print(scores_needed((
        (40, 80, 10),
        (90, 10, 0),
    )))