import os


def parsle_tongue():
    """
    Opens the logo.jpg file in binary mode, reads it in chunks, and yields hidden messages
    that are at least 5 characters long, contain only lowercase letters, and end with an exclamation mark.
    """
    filepath = os.path.join(os.path.dirname(__file__), "../resources/logo.jpg")
    message = b''

    with open(filepath, mode='rb') as file:
        while chunk := file.read(1024):  # Read the file in chunks of 1024 bytes
            for byte in chunk:
                if 97 <= byte <= 122:  # a-z
                    message += bytes([byte])
                elif byte == 33:  # '!'
                    if len(message) >= 5:
                        yield message.decode()
                    message = b''
                else:
                    message = b''
