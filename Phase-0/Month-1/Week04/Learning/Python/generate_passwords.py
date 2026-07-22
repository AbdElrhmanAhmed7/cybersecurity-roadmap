# Day 18 (Task 2)

import random
import string

def generate_passwords(count, length):
    n = length // 3
    for i in range(count):
        chars = "".join(random.choices(string.ascii_letters, k=n))
        digits = "".join(random.choices(string.digits, k=n))
        symbols = "".join(random.choices("!@$%^&*.", k=n))
        extra = []
        lst = [chars, digits, symbols]
        length_copy = length
        if length % 3 != 0:
            while length_copy > len(chars + digits + symbols):
                extra.append(random.choice(string.ascii_letters + string.digits + "!@$%^&*."))
                length_copy -= 1
        lst = list("".join(lst + extra))
        random.shuffle(lst)
        result = "".join(lst)
        yield result

for f in generate_passwords(5,12):
    print(f)