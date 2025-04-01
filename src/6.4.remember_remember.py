import os

from PIL import Image


def remember_remember(path: str = None) -> str:
    """
    Checks for black dots in the image of the given path, and converts the row to its ascii equivalent, the order of
    the word is by columns.
    :param path: path to the image
    :return: the message
    """
    if path is None:
        # Get the directory where the current file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, "code.png")

    try:
        # Open image as binary to check black / white
        img = Image.open(path)
        img = img.convert("1")
    except FileNotFoundError:
        return "Error: Image file not found."

    rows, columns = img.size
    message = ""

    # Checks each row and column for black dot
    for row in range(rows):
        for column in range(columns):
            dot = img.getpixel((row, column))
            if dot == 0:
                message += chr(column)
                break

    return message


if __name__ == '__main__':
    relative_path = "../../Notebooks/content/week06/resources/code.png"
    full_path = os.path.abspath(relative_path)
    print(remember_remember(full_path))
