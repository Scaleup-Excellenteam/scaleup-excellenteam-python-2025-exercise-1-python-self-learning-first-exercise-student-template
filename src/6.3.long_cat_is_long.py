def long_cat_is_long(text):
    # Replace punctuation with spaces and convert to lowercase
    filtered = []
    for ch in text:
        if ch.isalpha() or ch.isspace():
            filtered.append(ch)
        else:
            filtered.append(' ')
    
    cleaned = ''.join(filtered).lower()
    tokens = cleaned.split()

    # Build a dictionary mapping each word to its length
    lengths = {}
    for word in tokens:
        lengths[word] = len(word)

    return lengths

if __name__ == "__main__":
    sample_text = "Coding is fun! Cats, dogs & birds?"
    result = long_cat_is_long(sample_text)
    print("Word lengths:", result)
