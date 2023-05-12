from decimal import *


def bbpPi(n):
    # Returns the nth decimal digit of Pi using the BBP formula.
    if n < 0:
        raise ValueError("Invalid value of n.")

    pi = 0
    for k in range(n + 1):
        pi += (1 / pow(16, k)) * (
                4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))

    return int(pi * pow(10, n) % 10)


def legendrePi(n):
    # Returns the nth decimal digit of Pi using the Gauss-Legendre algorithm.
    if n < 0:
        raise ValueError("Invalid value of n.")

    getcontext().prec = n + 1  # Set the precision to n+1 decimal places

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(n):
        atmp = (a + b) / Decimal(2)
        b = (a * b).sqrt()
        t -= p * (a - atmp) ** Decimal(2)
        a = atmp
        p *= Decimal(2)

    pi = (a + b) ** Decimal(2) / (Decimal(4) * t)

    return int(str(pi)[n])


def spigotPi(n):
    # Returns the nth decimal digit of Pi using the spigot algorithm.
    if n < 0:
        raise ValueError("Invalid value of n.")

    pi = 0
    d = 1
    for i in range(n):
        pi += 4 * d
        d = (d * 10 - int(d * 10 / 10) * 10)

    return int(pi / pow(10, n - 1)) % 10
