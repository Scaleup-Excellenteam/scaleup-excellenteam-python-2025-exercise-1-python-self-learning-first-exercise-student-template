import os


def find_common_files(folder1, folder2):
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))
    return list(files1 & files2)


if __name__ == '__main__':
    print(find_common_files("path/to/folder1", "path/to/folder2"))
