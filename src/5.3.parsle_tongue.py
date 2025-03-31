def parsle_tongue():
    """
        Extracts secret messages from a file by reading its binary content.
        The secret messages are sequences of lowercase letters followed by an exclamation mark,
        and the message must have at least five lowercase letters.

        Parameters:
        file (str): The path to the file from which to extract the secret messages.

        Yields:
        str: The extracted secret messages that match the pattern.
        """
    try:
        # Open the file in binary mode
        with open("/Users/basharyamin/PycharmProjects/exercise-1-python-self-learning-Basharyam/src/logo.jpg", "rb") as file:
            # Read the file and decode it as ASCII, ignoring errors
            binary_data = file.read().decode("ascii", errors="ignore")
            new_str=""

            # Iterate through each character in the decoded data
            for bin in binary_data:
                if bin.islower():
                    new_str += bin
                elif bin == '!':
                    if len(new_str) >= 5:
                        yield new_str
                    new_str = ""
                else:
                    new_str = ""

    except FileNotFoundError:
        print("No such file or directory: ", file)



def main():
    for parse in parsle_tongue():
        print(parse)

if __name__ == "__main__":
    main()
