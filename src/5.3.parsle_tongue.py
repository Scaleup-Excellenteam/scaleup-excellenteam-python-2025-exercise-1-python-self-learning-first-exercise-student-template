import os
import re

def parsle_tongue(file_path: str = None):
    """
    Extracts hidden messages from a file using a generator. Messages are defined as lowercase English letters (at least 5 characters)
    followed by an exclamation mark (!).

    :param file_path: Path to a file
    :yield: Extracted messages one by one
    """
    if file_path is None:
        relative_path = './resources/logo.jpg'
        file_path = os.path.abspath(relative_path)

    PATTERN = re.compile(rb'[a-z]{5,}!') # the hidden messages pattern.
    CHUNK_SIZE = 1024
    messages = []

    try:
        with open(file_path, 'rb') as file:
            buffer = b''
            while chunk := file.read(CHUNK_SIZE):
                buffer += chunk
                pattern_matches = PATTERN.findall(buffer)

                for match in pattern_matches:
                    messages.append(match.decode())

                # keep the last 10 bytes as the beginning of the next chunk in case the message is between chunks.
                # If the message is in the last 10 bytes so find where it ends.
                if any(match in PATTERN.findall(buffer[-10:]) for match in pattern_matches):
                    match_start = buffer.find(match)
                    match_end = match_start + len(match)
                    buffer = buffer[match_end:]
                else:
                    buffer = buffer[-10:]

        return messages

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return ""

if __name__ == '__main__':
    relative_path  = './resources/logo.jpg'
    full_path = os.path.abspath(relative_path)

    found_messages = parsle_tongue()
    if found_messages:
        print("Found messages:", found_messages)
    else:
        print("No hidden messages found.")
