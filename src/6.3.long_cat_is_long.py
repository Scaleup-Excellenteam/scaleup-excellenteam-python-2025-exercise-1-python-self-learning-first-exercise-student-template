def count_words(text: str) -> dict[str, int]:
    """
    Counts how long is each word of a given text by a dictionary of the word and the length
    :param text: the text to be counted
    :return: the dictionary of the word and the length of the word
    """
    check_chars = [c for c in text.lower() if c.isalpha() or c.isspace()]
    check_chars = "".join(check_chars)

    check_words = check_chars.split()

    return {word: len(word) for word in check_words}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
