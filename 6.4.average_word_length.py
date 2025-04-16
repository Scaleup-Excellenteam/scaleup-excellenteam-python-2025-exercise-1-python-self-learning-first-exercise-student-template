def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


if __name__ == '__main__':
    txt = "hello world my name is code"
    print(average_word_length(txt))
