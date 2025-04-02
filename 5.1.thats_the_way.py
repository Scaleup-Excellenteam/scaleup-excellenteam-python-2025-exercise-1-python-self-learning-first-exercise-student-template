import os
def thats_the_way(directory):
    inside_files =[]
    for filename in os.listdir(directory):
        if filename.startswith("deep"):
            inside_files.append(filename)
    return inside_files

if __name__ == '__main__':
    filename = R""
    print(thats_the_way(filename))
