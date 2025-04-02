import os

def extract_secret_messages(file_path):
    """
    Reads a file and extracts secret messages: words with length >= 5 and ending with '!'.
    Returns:
        - None if file not found
        - [] if file is empty or contains no valid secret words
        - list of words (without '!') otherwise
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return None

    messages = []

    with open(file_path, 'rb') as file:
        content = file.read()
        if not content.strip():
            print("The file is empty.")
            return []

        chunk_text = content.decode('utf-8', errors='ignore')
        words = chunk_text.split()

        for word in words:
            if len(word) >= 5 and word.endswith('!'):
                messages.append(word[:-1])  # remove the '!'

    return messages


def parsle_tongue():
    """
    Wrapper function expected by the test.
    Assumes 'secret_message_file.txt' is in the current working directory.
    """
    return extract_secret_messages("secret_message_file.txt")



if __name__ == "__main__":
    result = parsle_tongue()
    if result is None:
        print("File not found.")
    elif not result:
        print("No secret messages found.")
    else:
        print("Secret messages found:", result)
