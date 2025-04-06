from PIL import Image


def remember_remember(image_path):
    """
    This function help the freedom fighters that want to save the freedom of the woke movement and the LGTBQ+ to help
    the western world (; :param image_path: the path of the imgae :return: secret message of the freedom fighters
    """
    with Image.open(image_path) as img:
        width, height = img.size
        decoded_message = ''
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                if pixel == 1:
                    decoded_message += chr(y)
        return decoded_message


if __name__ == '__main__':
    encrypted_image_path = "code.png"
    decoded_message = remember_remember(encrypted_image_path)
    print("Decoded message:", remember_remember)
