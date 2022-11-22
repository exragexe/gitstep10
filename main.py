

import random
try:
    size = int(input(" Enter amount numbers: "))
    begin = -100
    end = 100
    my_text = []
    for l in range(size):
        my_text.append(random.randint(begin, end))

    random.shuffle(my_text)
    print(my_text)
    ################################
    data = {1 : lambda lst: max(lst), 2: lambda lst: min(lst)}
    print(f"MAX: {data[1](my_text)}, MIN: {data[2](my_text)}")

except Exception as ex:
    print(ex)