import os

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


if __name__ == '__main__':
    directory_relative_path = "./images"
    directory_full_path = os.path.abspath(directory_relative_path)

    deep_files = thats_the_way(directory_full_path)
    print(deep_files)
