import os


def thats_the_way(path: str) -> list[str]:
    """
    Returns all the files in a given path if they start with 'deep'.
    :param path: Where to look for.
    :return: List of file names.
    """
    deep = []

    # Checks each file in path if it starts with deep and appends in case that it is.
    for filename in os.listdir(path):
        if filename.lower().startswith("deep"):
            deep.append(filename)

    return deep


if __name__ == '__main__':
    relative_path = "../../Notebooks/content/week05/images"
    full_path = os.path.abspath(relative_path)
    print(thats_the_way(full_path))

