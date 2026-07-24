


def flight_safety(islands, s, e, d):
    islands = sorted(islands, key = (lambda x: x[0]))

    cache = {}


    def helper(indx):
        if indx in cache:
            return cache[indx]
        else:

            if indx == len(islands) or indx < 0:
                cache[indx] = float("inf")
                return float("inf")

            else:

                if s > e:
                    change = -1
                else:
                    change = 1

                puntahan = islands[indx][1] + helper(indx + change)
                skip = helper(indx + (change * 2))

                if abs(islands[indx][0] - islands[indx + (change * 2)][0]) <= d:
                    recursion = min(puntahan, skip)
                else:
                    recursion = puntahan
                cache[indx] = recursion
                return recursion

    return helper(s)

print(flight_safety([
    (19, 1),
    (9, 4),
    (5, 2),
    (14, 5),
    (11, 1),
    (17, 3),
    (3, 2),
    (1, 1),
], 5, 2, 6)
)