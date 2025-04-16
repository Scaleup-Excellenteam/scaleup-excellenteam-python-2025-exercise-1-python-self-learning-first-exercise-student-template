"""
This module contains a generator that extracts secret words
hidden in binary files using a regex pattern.
"""

import re
import os

def parsle_tongue():
    """
    Generator that scans a binary file for secret strings.
    Looks inside 'img/logo.jpg' in the project root.
    The pattern must be 5 or more lowercase letters followed by '!'.
    It yields each unique string (without the '!') only once.
    """
    # Compile a regex pattern: 5+ lowercase letters followed by '!'
    pattern = re.compile(rb'[a-z]{5,}!')
    seen = set()  # Keep track of already-yielded strings to avoid duplicates

    # Determine the absolute path to the logo image in 'img/logo.jpg'
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up from /src
    file_path = os.path.join(base_dir, 'img', 'logo.jpg')

    # Open the image file in binary read mode
    with open(file_path, 'rb') as f:
        buffer = b''  # Holds bytes to search across chunks

        while True:
            chunk = f.read(1024)  # Read file in 1KB chunks
            if not chunk:
                break  # End of file

            buffer += chunk  # Append new chunk to buffer

            # Find all matching patterns in the current buffer
            for match in pattern.findall(buffer):
                try:
                    word = match.decode()[:-1]  # Decode and strip the '!' at the end
                    if word not in seen:
                        seen.add(word)  # Mark word as seen
                        yield word  # Yield the word
                except UnicodeDecodeError:
                    continue  # Skip if decoding fails

            buffer = buffer[-10:]  # Keep last 10 bytes to handle overlapping patterns

# Example run: prints found secret words
if __name__ == '__main__':
    for word in parsle_tongue():
        print(word)
