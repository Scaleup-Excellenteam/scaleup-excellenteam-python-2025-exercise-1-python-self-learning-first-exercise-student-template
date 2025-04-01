import re

def parsle_tongue():
    """
    Generator function that scans a binary file for secret strings
    matching a specific pattern (5 or more lowercase letters followed by '!').

    Reads the file in binary mode and processes it in chunks to avoid
    memory overload. Strings that match the pattern and can be decoded
    from bytes to UTF-8 are yielded.

    :yield: Decoded secret strings that match the pattern.
    :rtype: generator[str]
    """
    # Compile the regex pattern to match lowercase words of 5+ letters ending in '!'
    pattern = re.compile(rb'[a-z]{5,}!')

    # Open the binary file (e.g., an image or other binary resource)
    with open('resources/logo.jpg', 'rb') as f:
        buffer = b''  # buffer to hold overlapping binary data

        while True:
            chunk = f.read(1024)  # Read 1024 bytes at a time
            if not chunk:
                break  # Stop when end of file is reached

            buffer += chunk  # Append chunk to buffer

            # Find all matches in the current buffer
            matches = pattern.findall(buffer)
            for match in matches:
                try:
                    # Try to decode the match to a UTF-8 string
                    yield match.decode()
                except UnicodeDecodeError:
                    continue  # Skip matches that can't be decoded

            # Retain only the last 10 bytes of the buffer for overlap
            # to catch patterns that might span chunks
            buffer = buffer[-10:]

if __name__ == '__main__':
    secrets = parsle_tongue()
    for secret in secrets:
        print(secret)
