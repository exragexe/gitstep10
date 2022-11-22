

try:
    import random

    size = int(input(" Enter amount numbers: "))
    begin = -100
    end = 100
    my_text = []

    for l in range(size):
        my_text.append(random.randint(begin, end))

    random.shuffle(my_text)
    print(my_text)
    ###########################
    num = {1: lambda ls: ls[::-1]}
    print(num[1](my_text))

except Exception as e:
    print(e)