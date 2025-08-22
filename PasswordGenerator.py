import random
import string

def gen_pw(length=30):
    symbols = "@$!&"
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    # Choose a starting symbol and color
    symbol = random.choice(symbols)
    color = random.choice(colors)

    # All possible characters
    all_chars = string.ascii_letters + string.digits + symbols

    # Fill the rest randomly
    extra_length = length - (len(color) + 1)
    extra = [random.choice(all_chars) for _ in range(extra_length)]

    # Make sure at least one uppercase is included
    if not any(c.isupper() for c in extra):
        extra[random.randrange(len(extra))] = random.choice(string.ascii_uppercase)

    # Shuffle to avoid predictable placement
    pw_list = list(symbol + color + "".join(extra))
    random.shuffle(pw_list)
    return "".join(pw_list)

# Example
print(gen_pw())