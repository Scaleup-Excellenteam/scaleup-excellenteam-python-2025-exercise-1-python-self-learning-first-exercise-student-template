"""Exercise solution 6.3"""


def long_cat_is_long(input_text):
    """
    Count the length of each word in a text.
    """

    clean_text = ''.join(char.lower() if char.isalpha() else ' ' for char in input_text)
    words = clean_text.split()
    word_lengths = {word: len(word) for word in words}

    return word_lengths


if __name__ == "__main__":

    SAMPLE_TEXT = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    word_count_result = long_cat_is_long(SAMPLE_TEXT)
    print(word_count_result)
