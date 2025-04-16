
"""
This module contains a function `thats_the_way` that returns a list of all file names
in a specified directory that start with the prefix "deep".

Function:
    thats_the_way(directory_path):
        - Takes a directory path as input.
        - Returns a list of filenames in that directory starting with "deep".
        - If the directory is not found or access is denied, prints an error message.
"""
import os
START = "deep"
def thats_the_way(directory_path):
    """
    Return a list of all files in the given directory that start with the prefix "deep".
    Args:
        directory_path (str): The path to the directory where files are listed.
    Returns:
        list: A list of filenames that start with "deep", or None if there was an error.
    """
    try:
        return [
            f for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f)) and f.startswith(START)
        ]
    except FileNotFoundError:
        return "Error: no such directory"
    except PermissionError:
        return "Error: permission denied"

if __name__ == "__main__":
    print(thats_the_way(os.getcwd()))
