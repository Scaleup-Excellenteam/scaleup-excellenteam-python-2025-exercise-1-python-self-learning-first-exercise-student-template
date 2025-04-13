"""Processes a given text to count the length of each unique word."""

import re

def long_cat_is_long(txt: str) -> dict:
    """
    Processes a given text to count the length of each unique word.

    :param txt: A string containing words and punctuation.
    :return: A dictionary where keys are words and values are their lengths.
    """
    words = [word.lower() for word in re.findall(r"[a-zA-Z]+", txt)]
    return {word: len(word) for word in words}

if __name__ == '__main__':
    TXT = """
        You see, wire telegraph is a kind of a very, very long cat.
        You pull his tail in New York and his head is meowing in Los Angeles.
        Do you understand this?
        And radio operates exactly the same way: you send signals here, they receive them there.
        The only difference is that there is no cat.
        """
    result = long_cat_is_long(TXT)
    print(result)
