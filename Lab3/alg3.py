def alg3(n):
    c = [True] * (n + 1)

    c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    return c
