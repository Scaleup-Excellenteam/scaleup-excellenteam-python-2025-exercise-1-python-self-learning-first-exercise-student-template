import re
import os

def parsle_tongue():
    """
    Generator that scans a binary file for secret strings.
    Looks inside 'img/logo.jpg' in the project root.
    """
    pattern = re.compile(rb'[a-z]{5,}!')
    seen = set()

    base_dir = os.path.dirname(os.path.dirname(__file__))  # goes up from /src
    file_path = os.path.join(base_dir, 'img', 'logo.jpg')

    with open(file_path, 'rb') as f:
        buffer = b''

        while True:
            chunk = f.read(1024)
            if not chunk:
                break

            buffer += chunk

            for match in pattern.findall(buffer):
                try:
                    word = match.decode()[:-1]  # strip '!' at the end
                    if word not in seen:
                        seen.add(word)
                        yield word
                except UnicodeDecodeError:
                    continue

            buffer = buffer[-10:]


if __name__ == '__main__':
    for word in parsle_tongue():
        print(word)
