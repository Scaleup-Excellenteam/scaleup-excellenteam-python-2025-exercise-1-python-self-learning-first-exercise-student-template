"""
This module defines the `long_cat_is_long` function, which processes text
to remove non-alphabetic characters from words, converts them to lowercase,
and returns a dictionary mapping words to their lengths.
"""
TEXT = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
"""

def long_cat_is_long(text):
    """
    Cleans the input text by removing non-alphabetic characters from words and converting them to lowercase.
    Args:
        text (str): The input text to process.
    Returns:
        dict: A dictionary where keys are cleaned words and values are their lengths.
    """
    word_list = [''.join(c for c in word if c.isalpha()) for word in text.lower().split()]
    return {word: len(word) for word in word_list if word}

if __name__ == '__main__':
    print(long_cat_is_long(TEXT))
