def most_common_word(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return max(freq, key=freq.get)


if __name__ == '__main__':
    txt = "this is a test this is only a test test"
    print(most_common_word(txt))  # "test"
