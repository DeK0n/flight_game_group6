# random player id generator


def playerIdGen():
    import random
    x = "id"+str(random.randint(1000, 9999))  # e.g. id7362
    return x