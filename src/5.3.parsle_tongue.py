import os

SECRET_LENGTH = 5
SECRET_SUFFIX = '!'
SECRET_PATH = "secret_message_file.txt"

def extract_secret_messages(file_path):
    """
    Extracts secret messages: words with length >= SECRET_LENGTH and ending with SECRET_SUFFIX.
    Returns:
        - None if file not found
        - [] if file is empty or contains no valid secret words
        - list of words (without suffix) otherwise
    """
    if not os.path.exists(file_path):
        return None

    messages = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            has_content = False
            for line in file:
                if line.strip():
                    has_content = True
                for word in line.split():
                    if len(word) >= SECRET_LENGTH and word.endswith(SECRET_SUFFIX):
                        messages.append(word[:-1])
            if not has_content:
                return []
    except Exception:
        return None

    return messages


def parsle_tongue():
    return extract_secret_messages(SECRET_PATH)


if __name__ == "__main__":
    result = parsle_tongue()
    if result is None:
        print("File not found.")
    elif not result:
        print("No secret messages found.")
    else:
        print("Secret messages found:", result)
