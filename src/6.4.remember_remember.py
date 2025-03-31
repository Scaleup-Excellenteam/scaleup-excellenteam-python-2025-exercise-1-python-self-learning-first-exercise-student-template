from PIL import Image


def remember_remember(image_path):
    """"
    Extracts a secret message encoded in the pixel values of an image.
    The message is formed by concatenating characters corresponding to
    row indices where the pixel value is 1 (black).

    Parameters:
    image_path (str): The file path to the image from which to extract the secret message.

    Returns:
    str: The extracted secret message.
    """
    # Open the image file and convert it to grayscale (L mode)
    image = Image.open(image_path).convert("L")
    width, height = image.size

    secret_word = ""


    for r in range(width):
        for c in range(height):
            if image.getpixel((r, c)) == 1:  # Check if the pixel value is 1 (black)
                secret_word += chr(c)  # Convert row index to a character and add to the message

    return secret_word


def main():
    remember_remember("")


if __name__ == "__main__":
    main()
