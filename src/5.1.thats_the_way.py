"""
Module for listing files in a specified directory that start with "deep".

This script defines a function to scan a directory and return a list of files
whose names begin with "deep". It includes error handling for cases where the
specified directory does not exist.

Example usage:
    python script.py
"""
import os


def thats_the_way(your_path):
    """
      Lists all files in the specified directory whose names start with "deep".

      Parameters:
      your_path (str): The path to the directory to search for files.

      Returns:
      list: A list of file names that start with "deep".
            If the directory is not found, returns a string message.
      """
    try:
        lst =[]
        fold=os.listdir(your_path)
        for f in fold:
            if f.startswith("deep"):
                lst.append(f)
        return lst
    except FileNotFoundError:
        return "File not found"


if __name__ == "__main__":
    thats_the_way("")
