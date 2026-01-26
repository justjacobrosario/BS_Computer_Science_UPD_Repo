def did_not_follow(inputs):
    return tuple(msg for msg in inputs if (msg[:10] != "[WFM/MYZ] ") if (msg[:10] != "[WFM/TYZ] "))

print(did_not_follow((
    "[WFM/TYZ] Ada, Lovelace",
    "WFM/MYZ Charles, Babbage",
    "[LAB MYZ] Linus, Torvalds",
    "[MYZ] John, von Neumann",
    "[WFM] Edsger, Dijkstra",
    "[MYZ/WFM] Andrey, Kolmogorov",
    "[MYZ / TYZ] Radia, Perlman",
    "[WFM/MYZ]Paul, Graham",
    "Scott, Aaronson",
    "guido11",
    "[WFM/TYZ] Michael, Sipser",
    "[WFM/MYZ]",
    "[CS 11 WFM/MYZ] Tim, Berners-Lee",
    "[Lab TYZ] Barbara, Liskov",
    "[wfm/myz] Marvin, Minsky",
    "[WFM/TYZ] Donald, Knuth",
    "Erik, Demaine [WFM/MYZ]",
    "[WTF/TYZ] Emil, Post",
)))  