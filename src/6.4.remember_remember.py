from PIL import Image

def remember_remember(image_path, threshold=10):
    """
    Decodes a hidden message from an image by scanning for near-black pixels in each column.

    :param image_path: Path to the image file.
    :param threshold: Max RGB value considered as black (0 = perfect black).
    :return: Decoded message string.
    """
    # Open the image and make sure it's in RGB mode
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    message = ''

    # Loop through each column
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Check if the pixel is close enough to black
            if r < threshold and g < threshold and b < threshold:
                message += chr(y)
                break  # Move to next column after finding the character

    return message

# Example usage
if __name__ == "__main__":
    image_path = "resources/code.png"
    secret_message = remember_remember(image_path)
    print(secret_message)
