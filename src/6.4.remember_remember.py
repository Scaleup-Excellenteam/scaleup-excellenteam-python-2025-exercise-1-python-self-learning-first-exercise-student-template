from PIL import Image
import os

BLACK = (0, 0, 0)
DEFAULT_IMAGE_PATH = "src/code.png"

def remember_remember(image_path):
    """
    Decodes a hidden message in a PNG image based on black pixel row indices.
    Returns the message as a string.
    Raises exceptions if the file doesn't exist or can't be opened.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = Image.open(image_path)
    w, h = image.size
    pix = image.load()

    msg_chars = [
        chr(row)
        for col in range(w)
        for row in range(h)
        if pix[col, row][:3] == BLACK
        and not any(pix[col, r][:3] == BLACK for r in range(row))  # only first black per column
    ]

    return ''.join(msg_chars)


if __name__ == "__main__":
    try:
        decoded = remember_remember(DEFAULT_IMAGE_PATH)
        print("Decoded message:", decoded)
    except Exception as e:
        print(f"Error: {e}")
