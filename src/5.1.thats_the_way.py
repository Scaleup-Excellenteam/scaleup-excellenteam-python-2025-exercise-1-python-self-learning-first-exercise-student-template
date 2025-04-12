"""Exercise solution 5.2"""
import os


def thats_the_way(folder_path):
    """
    Returns a list of all files that begin with the sequence of letters "deep" in the specified folder.

    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path '{folder_path}' is not a valid directory")

    arr = []

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)) and filename.lower().startswith("deep"):
            arr.append(filename)

    return arr


if __name__ == "__main__":
    IMAGES_FOLDER = "images"

    try:
        result = thats_the_way(IMAGES_FOLDER)
        print(f"Files starting with 'deep' in {IMAGES_FOLDER}:")
        for file in result:
            print(f"- {file}")
    except FileNotFoundError:
        print(f"The folder '{IMAGES_FOLDER}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
