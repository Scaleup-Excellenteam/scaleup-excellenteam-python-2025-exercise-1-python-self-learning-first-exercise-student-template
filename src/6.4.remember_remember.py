"""Exercise solution 6.4"""
from PIL import Image


def remember_remember(image_path):
    """
    Decrypts a message from an image where each column has one black pixel.
    The row position of the black pixel corresponds to the ASCII value of a character.
    """
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return ""
    except Exception as error:
        print(f"Error opening image: {error}")
        return ""

    width, height = img.size
    pixels = img.load()

    result = []

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r < 10 and g < 10 and b < 10:
                result.append(y)
                break

    return ''.join(chr(code) for code in result)


if __name__ == "__main__":

    input_file_path = "resources/code.png"

    try:
        message = remember_remember(input_file_path)

        if message:
            print("Decrypted message:")
            print(message)
        else:
            print("No message found in the image.")
    except Exception as exc:
        print(f"An error occurred: {exc}")
