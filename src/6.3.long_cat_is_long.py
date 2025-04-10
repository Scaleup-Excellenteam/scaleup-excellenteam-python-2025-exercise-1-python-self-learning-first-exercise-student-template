"""
Processes a text string and returns a dictionary of cleaned words and their lengths.

- Converts text to lowercase.
- Removes non-letter characters from each word.
- Ignores empty or non-alphabetic results.
"""


def long_cat_is_long(text):
    """
    Cleans and analyzes words from a given text string.
    Args:
        text (str): Input string of text to process.
    Returns:
        dict: A dictionary mapping each alphabetic word to its length.
    """
    text = text.lower()
    cleaned_words = [''.join(ch for ch in word if ch.isalpha()) for word in text.split()]
    return {word: len(word) for word in cleaned_words if word != ''}


if __name__ == '__main__':
    print(long_cat_is_long("Bla bla bla tra lala 123"))
