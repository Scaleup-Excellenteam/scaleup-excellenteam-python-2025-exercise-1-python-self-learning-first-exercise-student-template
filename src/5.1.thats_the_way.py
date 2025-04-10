"""
This module retrieves a list of files in a specified directory.
It filters and returns only those files whose names start with "deep".
If the directory is not found, it returns an empty list.
"""

import os


def thats_the_way(path: str) -> list:
    """
    Retrieves files from the given directory that start with 'deep'.

    Args:
        path (str): The directory path to scan.

    Returns:
        list: A list of filenames starting with 'deep'. Returns an empty list if the directory doesn't exist.
    """
    try:
        return [file_name for file_name in os.listdir(path) if file_name.startswith("deep")]
    except FileNotFoundError:
        print("Directory doesn't exist")
        return []


if __name__ == '__main__':
    print(thats_the_way(r"content/week05/images"))
