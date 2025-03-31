import os
import re


def find_secret_messages(path: str) -> list[str]:
    """
    Searches for secret messages in a binary opened file, the message needs to be at least 5 characters long and ends
    with an exclamation mark.
    :param path: path to file
    :return: the secret messages
    """
    secret_messages = []
    buffer = b""

    # Reads the file in binary and just little parts each time
    with open(path, "rb") as f:
        while True:
            part = f.read(1024)
            if not part:
                break

            buffer += part

            # Finds what matches as a message
            matches = re.findall(b"([a-z]{5,}!)", buffer)

            for match in matches:
                try:
                    try_decode = match.decode("utf-8")
                    if try_decode not in secret_messages:
                        secret_messages.append(try_decode)
                except UnicodeDecodeError:
                    pass

    return secret_messages


if __name__ == "__main__":
    relative_path = "../../Notebooks/content/week05/resources/logo.jpg"
    full_path = os.path.abspath(relative_path)
    print(find_secret_messages(full_path))
