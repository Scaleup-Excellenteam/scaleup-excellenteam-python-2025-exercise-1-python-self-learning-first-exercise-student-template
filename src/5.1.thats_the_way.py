import os


def thats_the_way(directory):
    """
    This function takes a directory and returns a list of all files in the directory that start with "deep" in there
    name file. :param directory: path to the folder you want to search :return: list of all files in the directory
    that start with "deep" in there name file
    """
    inside_files = []
    for filename in os.listdir(directory):
        if filename.startswith("deep"):
            inside_files.append(filename)
    return inside_files


if __name__ == '__main__':
    filename = R""
    print(thats_the_way(filename))
