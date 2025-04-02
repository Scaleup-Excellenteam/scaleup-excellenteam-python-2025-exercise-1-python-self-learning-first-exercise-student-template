def parsle_tongue(filename):
    """
    This function takes file name that an image and return the secret message hide in the photo
    :param filename : name of the file to be opened
    :return: secret messages hiding in the image
    """
    # Opening the binary file in binary mode as rb(read binary)
    with open(filename, mode='rb') as file:
        fileContent = file.read()
        message = b''
        # Reading file data with read() method
        for byte in fileContent:
            if 97 <= byte <= 122:  # Lowercase English letters (ASCII values)
                message += bytes([byte])  # Append byte to message
            elif byte == 33:  # Exclamation mark (ASCII value)
                if len(message) >= 5:  # Check if message meets conditions
                    yield message.decode()  # Yield the decoded message
                message = b''  # Reset message buffer
            else:
                message = b''

if __name__ == '__main__':
    for msg in parsle_tongue('logo.jpg'):
        print(msg)