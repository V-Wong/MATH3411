import math


def middle_squares(n: int, seed: int) -> int:
    for _ in range(n):
        seed = seed ** 2

        while len(str(seed)) < 2 * n:
            seed = "0" + str(seed)

        while len(str(seed)) != n:
            seed = str(seed)[1:-1]

        seed = int(seed)

    return seed

if __name__ == "__main__":
    print(middle_squares(4, 2100))