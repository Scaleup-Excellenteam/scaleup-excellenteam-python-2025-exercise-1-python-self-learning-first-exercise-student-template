import string

def long_cat_is_long(text):
    """
    Returns a dictionary mapping each word (lowercased) to its length.
    Punctuation is removed before processing.
    """
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return {word: len(word) for word in words}

if __name__ == "__main__":
    sample_text = "Coding is fun! Cats, dogs & birds?"
    result = long_cat_is_long(sample_text)
    print("Word lengths:", result)
