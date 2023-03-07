def alg4(n):
    c = [True] * (n + 1)

    c[1] = False
    i = 2

    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    return c
