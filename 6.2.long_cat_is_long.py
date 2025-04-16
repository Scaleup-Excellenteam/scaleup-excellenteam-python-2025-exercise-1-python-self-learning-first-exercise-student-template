def long_cat_is_long(length):
    if length < 2:
        raise ValueError("Length must be at least 2")
    return "=^" + "~" * (length - 2) + "^="


if __name__ == '__main__':
    print(long_cat_is_long(2))    # =^^=
    print(long_cat_is_long(5))    # =^~~~^=
    print(long_cat_is_long(10))   # =^~~~~~~~~^=
