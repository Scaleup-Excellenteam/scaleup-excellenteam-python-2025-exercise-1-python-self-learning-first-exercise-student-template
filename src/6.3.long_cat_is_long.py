
def count_words(text):
    """
    מקבלת טקסט ומחזירה מילון של אורכי המילים שבו לאחר סינון סימנים לא רצויים.
    """
    # מנקים את הטקסט ממסמכים שאינם אותיות
    cleaned_text = ''.join(c if c.isalpha() else ' ' for c in text)
    # מחשבים את אורכי המילים
    return {word: len(word) for word in cleaned_text.lower().split()}


def main():
    
# דוגמת שימוש
    text = '''
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    '''
    result = count_words(text)
    print(result)
    
if(__name__=="__main__"):
    main()
