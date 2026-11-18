def vetvicka(strom):
    ovocie = set()
    if "(" not in strom or ")" not in strom:
        return {strom,}

    brackets_count = 0
    l = 0
    for r in range(len(strom)):
        if strom[r] == "(":
            brackets_count += 1
        elif strom[r] == ")":
            brackets_count -= 1
        if brackets_count == 0 and strom[r] != " ":
            ovocie = ovocie.union(vetvicka(strom[l+1:r]))
            l = r + 1

    print(len(ovocie))
    return ovocie



vetvicka(input().strip()[1:-1])
