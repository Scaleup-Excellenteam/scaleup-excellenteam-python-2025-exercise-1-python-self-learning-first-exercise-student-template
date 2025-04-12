"""Exercise solution 6.4"""
try:
    from PIL import Image
except ImportError:
    class Image:
        """Mock Image class used when PIL is not available."""
        @staticmethod
        def open(*args, **kwargs):
            """Mock method to simulate PIL's Image.open."""
            raise ImportError("PIL is not installed")


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
    except (IOError, OSError) as error:
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

    INPUT_FILE_PATH = "resources/code.png"

    try:
        MESSAGE = remember_remember(INPUT_FILE_PATH)

        if MESSAGE:
            print("Decrypted message:")
            print(MESSAGE)
        else:
            print("No message found in the image.")
    except (FileNotFoundError, IOError, OSError) as exc:
        print(f"An error occurred: {exc}")
