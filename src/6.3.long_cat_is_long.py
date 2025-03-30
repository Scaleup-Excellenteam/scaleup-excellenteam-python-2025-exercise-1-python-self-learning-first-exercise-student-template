

def long_cat_is_long(text):
    """
        Removes non-alphabetic characters from words in the input text and converts them to lowercase.
        Returns a dictionary where keys are words and values are their lengths.
        Ignores empty words resulting from non-alphabetic content.
        """
    word_list = [''.join(c for c in word if c.isalpha()) for word in text.lower().split()]
    return {word : len(word) for word in word_list if word}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(long_cat_is_long(text))