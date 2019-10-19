import sys

BLACK = "\033[1;30m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"

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
                BLUE + str(prefix + BLACK + next_char).ljust(37),
                next_code.ljust(20))
        else:
            print(BLACK + "".join(old_message).ljust(20), BLUE + "∅".ljust(10), 
                BLACK + str(d.index(prefix)).ljust(10), str(len(d) - 1) + ".", 
                BLUE + str(prefix + BLACK + next_char).ljust(37),
                next_code.ljust(20))
 
    return encoding


def decoding(message: list) -> str:
    d = [""]
    decoding = []

    for symbol in message:
        word = d[symbol[0]] + symbol[1]
        d.append(word)
        decoding.append(word)

    return decoding

if __name__ == "__main__":
    message = sys.argv[1]
    print("Encoded message:", "".join(encode(message)))

    #message = [(0, "t"),(0, "o"),(0, " "),(0, "b"),(0, "e"),(3, "o"),(0, "r"),(3,"n"),(2, "t"),(3, "t"),(2, " "),(4, "e")]
    #print("".join(decoding(message)))