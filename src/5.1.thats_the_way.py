import os

def thats_the_way(directory: str):
    """
    Returns a list of all files in the given directory that start with 'deep'.
    """
    result = []
    items = os.listdir(directory)
    for item in items:
        full_path = os.path.join(directory, item)
        if item.startswith("deep") and os.path.isfile(full_path):
            result.append(item)
    return result

if __name__ == "__main__":
    directory = "images"
    matching_files = thats_the_way(directory)
    print("Files found:", matching_files)
    print("Number of files starting with 'deep':", len(matching_files))
