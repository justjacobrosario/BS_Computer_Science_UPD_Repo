first = input()
strm, strd = first.split(" ")
M, D = int(strm), int(strd)

S = input()

def watch(s, d):
    count = 0
    for i in range(M):
        if s[i] == ".":
            is_guarded = False
            for j in range(d+1):
                if (0 <= (i - j) < M) and (s[i-j] == "G"):
                    is_guarded = True
                    break
                if (0 <= (i + j) < M) and (s[i+j] == "G"):
                    is_guarded = True
                    break
            if not is_guarded:
                count += 1

    print(count)

watch(S, D)
