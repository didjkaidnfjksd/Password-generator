import random
import string

def gen_pw(length=30):
    symbols = "@$!&"
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    
    symbol = random.choice(symbols)
    color = random.choice(colors)

    
    all_chars = string.ascii_letters + string.digits + symbols

    
    extra_length = length - (len(color) + 1)
    extra = [random.choice(all_chars) for _ in range(extra_length)]

    
    if not any(c.isupper() for c in extra):
        extra[random.randrange(len(extra))] = random.choice(string.ascii_uppercase)

    
    pw_list = list(symbol + color + "".join(extra))
    random.shuffle(pw_list)
    return "".join(pw_list)

# Example
print(gen_pw())
