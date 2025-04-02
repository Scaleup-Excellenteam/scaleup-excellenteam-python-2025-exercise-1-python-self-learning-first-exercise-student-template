def long_cat_is_long(text):
    cleaned_words = [
        ''.join(c for c in word if c.isalpha())
        for word in text.split()
    ]
    
    return {word: len(word) for word in cleaned_words if word}
print(long_cat_is_long("Hello, world! Test123."))

if __name__ == '__main__':
    print(long_cat_is_long("Hello, world! Test123."))