import math


def middle_squares(n: int, seed: int) -> int:
    '''
    Iterate:
        x_i+1 = (x_i)^2
        Add leading 0's so that x_i+1 has 2n digits
        Crop x_i+1 to middle n digits
    '''

    for _ in range(n):
        seed = seed ** 2
    
        while len(str(seed)) < 2 * n:
            seed = "0" + str(seed)

        cropped_seed = seed
        while len(str(cropped_seed)) != n:
            cropped_seed = str(cropped_seed)[1:-1]

        print(f"{seed} -> {cropped_seed}")

        seed = int(cropped_seed)

    return seed

if __name__ == "__main__":
    print("Final seed: ", middle_squares(4, 2100))