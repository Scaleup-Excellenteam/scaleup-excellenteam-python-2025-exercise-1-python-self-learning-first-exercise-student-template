import os
from PIL import Image

def remember_remember(path):
    """
        Reads a grayscale image from the given file path and extracts a hidden message.
        The message is formed by collecting characters based on pixel values in each column.
        Returns the extracted message as a string or None if the file is not found.
        """
    try:
        img = Image.open(path).convert('L')
        width, height = img.size
        message = []

        for col in range(width):
            for row in range(height):
                pixel = img.getpixel((col, row))
                if pixel == 1:
                    message.append(chr(row))
                    break

    except FileNotFoundError as e:
        print(e)
        return None

    return ''.join(message)


if __name__ == '__main__':
    print(remember_remember(os.path.abspath('./code.png')))
