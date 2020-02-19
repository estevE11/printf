def printf(s, *vars):
    if len(vars) < 1:
        print(s)
    else:
        res = ""
        i = 0
        for it in s:
            if it == "%":
                res += str(vars[i])
                i += 1
            else:
                res += it
        print(res)

name = "Sailor"
x = 4
y = 5
printf("% at (%, %)", name, x, y)
