def long_cat_is_long(text):
    # cleanup
    clean_text = ''.join([c if c.isalpha() else ' ' for c in text])
    words = clean_text.split(' ')
    words = [s for s in words if s != '']
    words = set(words)

    # logic
    return {word: len(word) for word in words}
