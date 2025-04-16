def my_max(*numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


if __name__ == '__main__':
    print(my_max(13, 256, 278, 887, 989, 457, 6510, 18, 865, 901, 401, 704, 640))
    print(my_max(2))
    print(my_max())
