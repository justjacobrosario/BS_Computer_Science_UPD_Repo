"""
socket (s1, s2, s3)
plugs (p1, p2, p3)

s1 + p1 == s2 + p2 == s3 + p3

"""

def plugs_that_match(s, p):
    s1, s2, s3 = s
    if p == ((),):
        return ()
    if len(p) == 0:
        return ()

    elif (len(p) == 1) and p[0] == (0,0,0):
        return ()

    else:
        if p[0][0] + s1 == p[0][1] + s2 == p[0][2] + s3:
            return (p[0],) + plugs_that_match(s, p[1:])
        else:
            return plugs_that_match(s, p[1:])

print(plugs_that_match((1, 1, 1), ((),)))

#always check whats being asked, if only one output or all satisfiable output