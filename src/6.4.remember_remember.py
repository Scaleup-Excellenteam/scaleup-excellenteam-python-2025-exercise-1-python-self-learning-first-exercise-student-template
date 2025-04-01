from PIL import Image

def decode_message(path):
    """
    Decode a hidden message from an image by scanning black pixels.

    For each column in the image, the function checks pixels from top to bottom.
    If it finds a pixel that is black or nearly black (R, G, B ≤ 10), it adds
    the character corresponding to the Y-coordinate (as a Unicode character)
    to the decoded message and moves on to the next column.

    :param str path: Path to the image file.
    :return: The decoded message string.
    :rtype: str
    """
    # Open the image and ensure it's in RGB mode
    img = Image.open(path)
    img = img.convert("RGB")

    width, height = img.size
    message = ""

    # Iterate through each column in the image
    for x in range(width):
        # For each column, scan from top to bottom
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            # If the pixel is black or nearly black
            if r <= 10 and g <= 10 and b <= 10:
                # Convert the y-position to a character and add to message
                message += chr(y)
                break  # Move to the next column after the first match

    return message

if __name__ == '__main__':

    print(decode_message("resources/code.png"))