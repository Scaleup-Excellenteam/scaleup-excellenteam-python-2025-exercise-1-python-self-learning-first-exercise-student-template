import os
"""Module that provides a function to retrieve files from a directory whose names start with 'deep'."""

def thats_the_way(directory_path: str) -> list[str]:
    """
    Returns a list of all files in the given directory whose names start with 'deep'.

    :param directory_path: The path to the directory where the files are located.
    :return: A list of filenames (strings) that start with 'deep'.
    """
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")

        directory_files = os.listdir(directory_path)
        deep_files = [file for file in directory_files if file.startswith('deep')]
        return deep_files

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []


if __name__ == '__main__':
    DIRECTORY_RELATIVE_PATH = "./images"
    DIRECTORY_FULL_PATH = os.path.abspath(DIRECTORY_RELATIVE_PATH )

    contain_deep_files = thats_the_way(DIRECTORY_FULL_PATH)
    print(contain_deep_files)
