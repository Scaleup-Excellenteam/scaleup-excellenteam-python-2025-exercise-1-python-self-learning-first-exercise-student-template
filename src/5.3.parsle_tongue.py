def parsle_tongue():
    """
    Extracts secret messages from a binary file.
    A secret message is defined as a string of at least 5 lowercase English letters
    ending with an exclamation mark.

    Returns the messages without the exclamation marks.
    """
    file_path = "resources/logo.jpg"  # Default path based on your main code
    chunk_size = 4096
    min_message_length = 6  # Including the exclamation mark
    secret_messages = []
    buffer = b""

    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                buffer += chunk

            buffer_str = buffer.decode('ascii', errors='ignore')
            j = 0
            while j < len(buffer_str):
                start = j
                while j < len(buffer_str) and buffer_str[j].islower():
                    j += 1

                if j < len(buffer_str) and buffer_str[j] == '!':
                    found_message = buffer_str[start:j]  # Exclude the exclamation mark
                    if len(found_message) + 1 >= min_message_length:  # +1 for the excluded exclamation mark
                        secret_messages.append(found_message)
                j += 1
    except Exception as err:
        print(f"An error occurred: {err}")

    return secret_messages


if __name__ == "__main__":
    try:
        messages = parsle_tongue()
        if messages:
            print(f"Found {len(messages)} secret messages:")
            for i, message in enumerate(messages, 1):
                print(f"{i}. {message}")
        else:
            print("No secret messages found.")
    except Exception as e:
        print(f"An error occurred: {e}")
