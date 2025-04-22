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

    Raises:
    FileNotFoundError: If the specified directory does not exist.
    """
    if not os.path.isdir(your_path):
        raise FileNotFoundError(f"The directory '{your_path}' was not found.")

    return [f for f in os.listdir(your_path) if f.startswith("deep")]


if __name__ ==__main__:
    thats_the_way("")
