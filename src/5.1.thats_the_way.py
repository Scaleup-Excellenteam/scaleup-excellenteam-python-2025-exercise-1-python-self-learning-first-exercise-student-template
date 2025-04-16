"""
This module processes filtered files from a nested directory structure.
"""

import os


def thats_the_way(folder_path):
    """
    Find all files in a given folder whose names start with 'deep'.

    :param str folder_path: The path to the folder to search in.
    :return: A list of filenames that start with 'deep' and are regular files (not directories).
    :rtype: list[str]
    """
    # Get all contents (files and folders) in the specified directory
    files = os.listdir(folder_path)

    # Filter only regular files whose names start with 'deep'
    deep_files = [
        f for f in files
        if f.startswith("deep") and os.path.isfile(os.path.join(folder_path, f))
    ]

    # Return the list of matching files
    return deep_files

if __name__ == '__main__':
    folder = input("Enter the folder path: ")
    result = thats_the_way(folder)
    print("Files starting with 'deep':", result)
