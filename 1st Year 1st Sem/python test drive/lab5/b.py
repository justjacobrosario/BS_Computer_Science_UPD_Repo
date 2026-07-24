"""
budget of b1 to b2 inclusive

m movie proposals (elements as minutes)
a actors (elements as bezos per sec)

one movie and one actor
goal:
how many ways such that over cost is between budget

"""

def movie_count(movies, actors, b1, b2):
    count = 0
    for m in movies:
        for a in actors:
            if b1 <= ((m*60) * a) <= b2:
                count += 1
    return count


def movie_count(movies, actors, b1, b2):
    count = 0
    movies = [n*60 for n in movies]
    
    movies = sorted(movies)
    count = 0

    for a in actors:

        b1_above_i = above_b1(movies, a, b1)
        b2_below_i = below_b2(movies, a, b2)
        if b1_above_i != None and b2_below_i != None:
            count += abs(b2_below_i - b1_above_i + 1)

    return count


def above_b1(movies, a, b1):
    l = 0
    r = len(movies) - 1
    candidates = None

    while l <= r:
        m = (l+ r) // 2
        if movies[m]*a >= b1:
            r = m - 1
            candidates = m
        else:
            l = m + 1
    return candidates

def below_b2(movies, a, b2):
    l = 0
    r = len(movies) - 1
    candidates = None

    while l <= r:
        m = (l+ r) // 2
        if movies[m]*a <= b2:
            l = m + 1
            candidates = m
        else:
            r = m - 1
    return candidates


#print(below_b2(sorted([63*60, 70*60, 90*60, 120*60, 150*60]), 1, 15000))

print(movie_count(
    [90, 63, 120, 70, 150],
    (3, 1, 4, 9, 6),
    5_000,
    15_000
)
)