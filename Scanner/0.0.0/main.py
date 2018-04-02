import string
from token_v1 import token, Tokens
offset = 0
fstrim = None
tokens = Tokens()

def next():
    global fstrim
    global offset
    while True:
        fstrim.seek(offset)
        character = fstrim.read
        offset += 1
        if character not in string.whitespace:
            break
        offset -= 1
        return character


def scan():
    global fstrim
    global offset
    while True:
        fstrim.seek(offset)
        character = fstrim.read(1)
        offset += 1
        if character not in string.whitespace or character in "":
            break

    return character


def scanner(filename):
    global fstrim
    global offset
    global tokens
    with open(filename) as fstrim:
        while True:
            character = scan()
            if not character:
                break
            # comment
            if character in "#":
                character = scan()
                if character in "#" or character in "":
                    break
            # word
            elif character in string.ascii_letters:
                word = ""
                while True:
                    word += character
                    character = scan()
                    if character not in string.ascii_letters or character in "":
                        offset -= 1
                        break
                tokens.append(token("id", word))
            # Integer constant
            elif character in "1234567890":
                num = ""
                while True:
                    num += character
                    character = scan()
                    if character not in "1234567890":
                        offset -= 1
                        break
                tokens.append(token("integer", int(num)))
            elif character in "=!<"
            # arithmetic
            elif character in "+-*/%":
                tokens.append(token("arithmetic", character))
            # relational





scanner("thing.sictc")

