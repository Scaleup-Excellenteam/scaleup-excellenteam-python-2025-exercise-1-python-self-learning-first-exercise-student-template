import os

def thats_the_way(directory):
    """
    Scans the specified directory and returns a list of filenames
    that start with the prefix 'deep'.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        list: A list of filenames (str) that start with 'deep'.
    """
    inside_files = []
    for filename in os.listdir(directory):
        if filename.startswith("deep"):
            inside_files.append(filename)
    return inside_files


if __name__ == '__main__':
    """
    Example usage:
    Prompts the user to input a directory path and prints all files
    inside that directory which start with 'deep'.
    """
    filename = R""  # Insert path here, e.g. r"C:\Users\HALAA\some_folder"
    print(thats_the_way(filename))

