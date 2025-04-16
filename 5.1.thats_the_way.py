import os

def thats_the_way(directory_path):
    return [f for f in os.listdir(directory_path) if f.startswith("deep")]

if __name__ == '__main__':
    print(thats_the_way("images"))
