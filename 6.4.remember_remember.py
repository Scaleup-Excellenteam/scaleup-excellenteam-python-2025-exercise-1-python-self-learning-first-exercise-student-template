from PIL import Image
def decode_message(image_path):
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
    decoded_message = decode_message(encrypted_image_path)
    print("Decoded message:", decoded_message)