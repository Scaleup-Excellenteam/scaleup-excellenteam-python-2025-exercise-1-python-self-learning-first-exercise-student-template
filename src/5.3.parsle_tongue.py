import re
import os

def parsle_tongue(filepath=None):
    """
    Extracts secret messages from a binary file.
    Messages must be at least 5 lowercase letters and end with '!'
    """

    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), '../resources/logo.jpg')

    # Searching pattern
    pattern = re.compile(rb'[a-z]{5,}!')

    with open(filepath, 'rb') as f:
        leftover = b''
        while True:
            chunk = f.read(1024)
            if not chunk:
                break

            data = leftover + chunk

            # Find all matches
            for match in pattern.finditer(data):
                yield match.group().decode('utf-8')

            # Save the tail of the chunk to catch cut-off matches
            leftover = data[-10:]


if __name__ == '__main__':
    path = 'resources/logo.jpg'

    for hidden_msg in parsle_tongue(path):
        print(hidden_msg)
