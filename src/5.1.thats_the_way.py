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
    images_folder = "images"

    try:
        result = thats_the_way(images_folder)
        print(f"Files starting with 'deep' in {images_folder}:")
        for file in result:
            print(f"- {file}")
    except FileNotFoundError:
        print(f"The folder '{images_folder}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
