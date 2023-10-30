def tub(n: int):
    if int(n ** 0.5) + 1 % 2 == 0:
        print(True)
    else:
        print(False)


tub(13)