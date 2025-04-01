import os

def thats_the_way(folder_path):
    """
    Returns a list of file names in the given folder that starts with 'deep'.

    :param folder_path: Path of the folder to search in.
    :return: List of files names that starts with 'deep'.
    """

    # Get all items in the given folders, and return only those whose names start with "deep".
    return [filename for filename in os.listdir(folder_path) if filename.startswith("deep")]

# This block will only run if the script is executed directly.
if __name__ == '__main__':
    # Folder path
    folder = 'images'

    # Call the function and store the result
    deep_files = thats_the_way(folder)

    # Print the result
    print("Files starting with 'deep':", deep_files)

    # Print the number of matching files
    print(f"Found {len(deep_files)} file(s) starting with 'deep'")