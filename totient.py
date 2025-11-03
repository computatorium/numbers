def phi(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    result, remaining = n, n

    if remaining % 2 == 0:
        result -= result // 2
        while remaining % 2 == 0:
            remaining //= 2

    factor = 3
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 2

    if remaining > 1:
        result -= result // remaining
    return result
