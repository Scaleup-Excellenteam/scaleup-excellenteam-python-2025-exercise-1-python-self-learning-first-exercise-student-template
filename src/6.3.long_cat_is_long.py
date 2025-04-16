def long_cat_is_long(text):
    """
    Process a string to count the length of each word.

    Punctuation is removed and letters are converted to lowercase.
    Then, the function builds a dictionary where each word maps to its length.

    :param str text: The input string to process.
    :return: A dictionary mapping words to their lengths.
    :rtype: dict[str, int]
    """
    # Remove punctuation and convert all letters to lowercase
    cleaned = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

    # Split the cleaned string into a list of words
    words = cleaned.split()

    # Build a dictionary with each word and its length
    return {word: len(word) for word in words}


if __name__ == '__main__':
    text = """
            You see, wire telegraph is a kind of a very, very long cat.
            You pull his tail in New York and his head is meowing in Los Angeles.
            Do you understand this?
            And radio operates exactly the same way: you send signals here, they receive them there.
            The only difference is that there is no cat.
            """
    result = long_cat_is_long(text)
    print(result)