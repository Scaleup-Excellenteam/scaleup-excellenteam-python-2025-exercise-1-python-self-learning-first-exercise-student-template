from PIL import Image
import os

def remember_remember(image_path):
    """
    Decodes a hidden message in a PNG image based on black pixel row indices.
    Returns the message, or None if the image can't be opened.
    """
    if not os.path.isfile(image_path):
        print(f"Image file not found: {image_path}")
        return None

    try:
        image = Image.open(image_path)
    except Exception as err:
        print(f"Failed to open image: {err}")
        return None

    msg_chars = []
    w, h = image.size
    pix = image.load()

    for col in range(w):
        for row in range(h):
            r, g, b = pix[col, row][:3]
            if (r, g, b) == (0, 0, 0):
                msg_chars.append(chr(row))
                break

    return ''.join(msg_chars)


if __name__ == "__main__":
    path = "src/code.png"
    decoded = remember_remember(path)
    if decoded:
        print("Decoded message:", decoded)
    else:
        print("No message decoded.")
