import sys
from typing import List
from decimal import Decimal


def encode(message: str, symbols: List[str], probabilities: List[float]) -> (Decimal, Decimal):
    message = list(message)

    start = Decimal(0)
    width = Decimal(1)

    for char in message:
        start = start + sum(probabilities[0:symbols.index(char)]) * width
        width = probabilities[symbols.index(char)] * width

    return start, width


if __name__ == "__main__":
    if sys.argv[1] == "-e" or sys.argv[1] == "-encode":
        symbols = input("Please enter your symbols: ").split(" ")
        probabilities = input("Please enter the corresponding probabilities: ").split(" ")
        probabilities = list(map(lambda x: Decimal(x), probabilities))
        message = input("Please enter the message to decode: ")

        start, width = encode(message, symbols, probabilities)

        print("Encoded Message: "
            f"[{round(start, 4)}, {round(start, 4)} + {round(width, 4)})"
            f" = [{round(start, 4)}, {round(start + width, 4)})")