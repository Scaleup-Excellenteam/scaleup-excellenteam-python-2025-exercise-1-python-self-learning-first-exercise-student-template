import os

def thats_the_way(directory: str):
    """
    Returns a list of all files in the given directory that start with 'deep'.
    """
    result = []
    try:
        items = os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"No permission to access '{directory}'.")
        return []

    for item in items:
        full_path = os.path.join(directory, item)
        if item.startswith("deep") and os.path.isfile(full_path):
            result.append(item)
    return result

if __name__ == "__main__":
    directory = "images"
    matching_files = thats_the_way(directory)
    if not matching_files:
        print("No files starting with 'deep' were found.")
    else:
        print("Files found:", matching_files)
    print("Number of files starting with 'deep':", len(matching_files))
