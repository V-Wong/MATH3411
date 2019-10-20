import sys
from typing import List
from decimal import Decimal

BLACK = "\033[1;30m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"


def encode(message: str, symbols: List[str], probabilities: List[float]) -> (Decimal, Decimal):
    message = list(message)

    start = Decimal(0)
    width = Decimal(1)

    # Print headings
    print(RED + "character".ljust(10), "subinterval start".ljust(40), 
          "subinterval width".ljust(40))

    # Print initial subinterval values
    print(BLACK + "".ljust(10), "0.0000".ljust(40), f"{BLUE}1.0000{BLACK}".ljust(40))

    for char in message:
        old_start = start
        old_width = width

        start = start + sum(probabilities[0:symbols.index(char)]) * width
        width = probabilities[symbols.index(char)] * width

        # Print progress of subinterval start and widths
        print(char.ljust(10), f"{round(old_start, 4)} + "
              f"%.4f" % sum(probabilities[0:symbols.index(char)]),
              f"x {BLUE}{round(old_width, 4)}{BLACK} = {round(start, 4)}".ljust(38), 
              f"{round(probabilities[symbols.index(char)], 4)} x " 
              f"{round(old_width, 4)} = {BLUE}{round(width, 4)}{BLACK}".ljust(40))

    return start, width


if __name__ == "__main__":
    if sys.argv[1] == "-e" or sys.argv[1] == "-encode":
        symbols = list(input("Please enter your symbols: ").replace(" ", ""))
        probabilities = input("Please enter the corresponding probabilities: ").split(" ")
        probabilities = list(map(lambda x: Decimal(x), probabilities))
        message = input("Please enter the message to encode: ")

        start, width = encode(message, symbols, probabilities)

        print(YELLOW + "Encoded Message: "
              f"[{round(start, 4)}, {round(start, 4)} + {round(width, 4)})"
              f" = [{round(start, 4)}, {round(start + width, 4)})")
    