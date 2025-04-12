from PIL import Image


def remember_remember(image_path):
    """
    At This Function Will Uplaod A Picture, And Convert All The Black Pixles In The Picture Columns,
    Each Black Pixel Place Will Be Convert And Well Get The Secret String.
    """

    secret_string = ''
    image = Image.open(image_path)
    image = image.convert("RGB")

    width, height = image.size
    image_pixles = image.load()

    # Transition On Each Column And Row Of The Picture
    for x_axis in range(width):
        for y_axis in range(height):

            # Check If Pixel Is Black.
            pixles = image_pixles[x_axis, y_axis]
            if all(val < 10 for val in pixles):
                secret_string += chr(y_axis)

    return secret_string


def main():
    print(remember_remember(
        "C:\\Users\\97254\\Desktop\\Excellenteam\\Excellenteam Advanced Python\\Ex\\resources\\code.png"))


if __name__ == "__main__":
    main()
