def extract_even_digits(s):
    return [int(ch) for ch in s if ch.isdigit() and int(ch) % 2 == 0]


if __name__ == '__main__':
    print(extract_even_digits("a2b4c9"))  # [2, 4]
