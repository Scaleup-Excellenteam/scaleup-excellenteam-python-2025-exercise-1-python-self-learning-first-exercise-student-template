from os import listdir


def thats_the_way(path):
    return [f for f in listdir(path) if f.startswith("deep")]
