def printf(s, *vars):
    if len(vars) < 1:
        print(s)
    else:
        res = ""
        curr = ""
        i = 0
        for it in s:
            if it == "%":
                res += curr
                curr = ""
                res += str(vars[i])
                i += 1
            else:
                curr += it
        res += curr
        print(res)
