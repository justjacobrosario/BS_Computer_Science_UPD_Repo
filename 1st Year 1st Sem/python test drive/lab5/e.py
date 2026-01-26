


def grass_triplets(lawn):
    pre_occurences = prefix_occurences(lawn)
    count = 0

    for i in range(len(lawn)):

        occ_i = 1 if lawn[i] == "x" else 0
        for j in range(i, len(lawn)):
            if i < j:
                if lawn[j] == "x":
                    occ_i += 1
                if occ_i == 3:
                    count += 1
    return count


def prefix_occurences(lawn):
    res = [0]

    for cell in lawn:
        if cell == "x":
            res.append(res[-1]+1)
        else:
            res.append(res[-1])
    res.pop(0)
    return res

print(prefix_occurences("xx...xx"))


print(grass_triplets("xx...xx"))