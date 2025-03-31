import re
def long_cat_is_long(text):
    """
       Cleans up the input string by removing non-alphabetic characters from each word,
       and returns a dictionary where the keys are the cleaned words and the values are their lengths.

       Parameters:
       str (text): The input string to process.

       Returns:
       dict: A dictionary with cleaned words as keys and their lengths as values.
       """

    cleaned_words = [''.join(re.findall(r'[a-zA-Z]+', word)) for word in text.split()]


    dict_words = {key: len(key) for key in cleaned_words if key}

    return dict_words


def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    ss="Bla bla bla tralala 123"

    print(long_cat_is_long(ss))

if __name__ == "__main__":
    main()