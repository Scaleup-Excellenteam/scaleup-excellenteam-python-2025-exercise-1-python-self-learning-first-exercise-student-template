"""
Extracts hidden messages from a file using a generator.
Messages are defined as lowercase English letters (at least 5 characters)
followed by an exclamation mark (!).
"""

import os
import re

BYTES_PER_CHUNK = 1024

def parsle_tongue(file_path: str = None):
    """
    Extracts hidden messages from a file using a generator.
    Messages are defined as lowercase English letters (at least 5 characters)
    followed by an exclamation mark (!).

    :param file_path: Path to a file
    :yield: Extracted messages one by one
    """
    if file_path is None:
        path = './resources/logo.jpg'
        file_path = os.path.abspath(path)

    pattern = re.compile(rb'[a-z]{5,}!') # the hidden messages pattern.

    chunk_size = BYTES_PER_CHUNK

    messages = []

    with open(file_path, 'rb') as file:
        buffer = b''
        while chunk := file.read(chunk_size):
            buffer += chunk
            pattern_matches = pattern.findall(buffer)

            for match in pattern_matches:
                messages.append(match.decode()[:-1])

            # keep the last 10 bytes as the beginning of the next chunk in case the message is between chunks.
            # If the message is in the last 10 bytes so find where it ends.
            if any(match in pattern.findall(buffer[-10:]) for match in pattern_matches):
                match_start = buffer.find(pattern_matches[-1])
                match_end = match_start + len(pattern_matches[-1])
                buffer = buffer[match_end:]
            else:
                buffer = buffer[-10:]

    return messages

if __name__ == '__main__':
    RELATIVE_PATH  = './resources/logo.jpg'
    FULL_PATH = os.path.abspath(RELATIVE_PATH)

    found_messages = parsle_tongue()
    if found_messages:
        print("Found messages:", found_messages)
    else:
        print("No hidden messages found.")
