import sys
import re

BLACK = "\033[1;30m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"

def longest_prefix(prefixes: [str], message: str) -> (str, int):
    max_length = 0
    longest_prefix = ""

    for prefix in prefixes:
        i = 0
        while i < len(prefix) and i < len(message):
            if prefix[i] != message[i]:
                break
            else:
                i += 1

        if i > max_length:
            max_length = i
            longest_prefix = prefix
            
    return longest_prefix, max_length


def encode(message: str) -> list:
    d = [""]
    encoding = []

    message = message.replace(" ", "_")
    message = list(message)

    # Print headings
    print(RED + "r".ljust(20), "s".ljust(10), 
          "l".ljust(10), "new dictionary entry".ljust(30), 
          "output".ljust(20))

    # Print message before any algorithm steps
    print(BLACK + "{: <20} {: <10} {: <10} {: <30} {: <20}".format(
          "", "", "", "0. ∅", ""))

    while message:
        prefix, max_length = longest_prefix(d, message)
        old_message = message
        message = message[max_length:]

        if message:
            next_char = message.pop(0)
        else:
            next_char = ""
    
        next_code = f"({d.index(prefix)}, {next_char})"
        encoding.append(next_code)
        d.append(prefix + next_char)

        if prefix:
            print(BLACK + "".join(old_message).ljust(20), BLUE + prefix.ljust(10), 
                BLACK + str(d.index(prefix)).ljust(10), str(len(d) - 1) + ".", 
                BLUE + str(prefix + BLACK + next_char).ljust(34),
                next_code.ljust(20))
        else:
            print(BLACK + "".join(old_message).ljust(20), BLUE + "∅".ljust(10), 
                BLACK + str(d.index(prefix)).ljust(10), str(len(d) - 1) + ".", 
                BLUE + str(prefix + BLACK + next_char).ljust(34),
                next_code.ljust(20))
 
    return encoding


def format_message(message: str) -> list:
    message = re.findall(r"\((\d+),\s*([a-zA-Z\s]+)\)", message)
    message = list(map(lambda x: (int(x[0]), x[1]), message))
    return message


def decode(message: list) -> str:
    d = [""]
    decoding = []

    # Print headings
    print(RED + "output".ljust(20), "new dictionary entry".ljust(10))
    print(BLACK + "".ljust(20), "0. " + BLUE + "∅".ljust(10))

    for symbol in message:
        char = str(symbol[1]).replace(" ", "_")
        output = f"({symbol[0]}, {char})"

        word = (d[symbol[0]] + symbol[1]).replace(" ", "_")
        d.append(word)
        decoding.append(word)

        print(BLACK + output.ljust(20), f"{len(d) - 1}. " + BLUE + f"{word}".ljust(10))

    return decoding


if __name__ == "__main__":
    if sys.argv[1] == "-e" or sys.argv[1] == "-encode":
        message = sys.argv[2]
        print(YELLOW + "Encoded message:", "".join(encode(message)))
    elif sys.argv[1] == "-d" or sys.argv[1] == "-decode":
        message = sys.argv[2]
        message = format_message(message)
        print(YELLOW + "Decoded message:", "".join(decode(message)))
    else:
        print(f"Usage: python3 {sys.argv[0]} [(-e)ncode|(-d)ecode] [message|codeword]")
