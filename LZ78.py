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
    d = []
    encoding = []

    message = list(message)

    # Print headings
    print(RED + "{: <20} {: <10} {: <10} {: <30} {: <20}".format(
          "r", "s", "l", "new dictionary entry", "output"))

    # Print message before any algorithm steps
    print(BLACK + "{: <20} {: <10} {: <10} {: <30} {: <20}".format(
          "".join(message), "", "", "", ""))

    while message:
        prefix, max_length = longest_prefix(d, message)
        old_message = message
        message = message[max_length:]

        if message:
            next_char = message.pop(0)
        else:
            next_char = ""
    
        if prefix:
            next_code = f"({max_length + 1}, {next_char})"
            encoding.append(next_code)
            d.append(prefix + next_char)
        else:
            next_code = f"(0, {next_char})"
            encoding.append(next_code)
            d.append(next_char)

        length = max_length + 1 if max_length != 0 else 0

        # Print new row of table
        print(BLACK + "{: <20}{} {: <10}{} {: <10} {}{: <30}        {: <20}".format(
              "".join(old_message), BLUE, prefix, BLACK, length, 
              BLUE, prefix + BLACK + next_char, str(next_code)))

    return encoding

if __name__ == "__main__":
    message = sys.argv[1]
    print("Encoded message:", "".join(encode(message)))