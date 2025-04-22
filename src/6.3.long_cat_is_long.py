"""
Module: long_cat_words
This module contains a utility function to clean and analyze words in a string,
returning a dictionary of cleaned words with their respective lengths.
"""
import re


def long_cat_is_long(input_text):
    """
        Cleans up the input string by removing non-alphabetic characters from each word,
        and returns a dictionary where the keys are the cleaned words and the values are their lengths.

        Parameters:
            input_text (str): The input string to process.

        Returns:
            dict: A dictionary with cleaned words as keys and their lengths as values.
        """

    cleaned_words = [''.join(re.findall(r'[a-zA-Z]+', word)) for word in input_text.split()]
    dict_words = {key: len(key) for key in cleaned_words if key}
    return dict_words


if __name__ == "__main__":
    long_cat_is_long("")
