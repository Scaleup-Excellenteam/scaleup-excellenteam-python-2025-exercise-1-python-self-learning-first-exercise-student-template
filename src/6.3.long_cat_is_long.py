import string


def long_cat_is_long(text):
    """
    Calculate The Count Of Each Word In The Given Text, And Return It In A Dictionary.
    """
    
    # Clean The Text From All The Punctuation Marks In.
    cleand_text = ''.join(ch for ch in text if ch not in string.punctuation)

    # Get The Word Of The Text To A list.
    word_list = cleand_text.lower().split()
    word_dict = {word: word_list.count(word) for word in word_list if not word.isdigit()}

    word_len_list = {key: len(key) for key in word_dict.keys()}

    return word_len_list


def main():
    text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
    count_words_dic = long_cat_is_long(text)
    print(count_words_dic)


if __name__ == "__main__":
    main()
