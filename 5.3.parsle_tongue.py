from typing import Generator
import re
import os


def calculate_check_digit(id_without_check: str) -> int:
    total = 0
    for index, digit_char in enumerate(id_without_check):
        digit = int(digit_char)
        num = digit * (1 if index % 2 == 0 else 2)
        if num > 9:
            num -= 9
        total += num
    return (10 - (total % 10)) % 10


def all_israeli_ids() -> Generator[str, None, None]:
    for raw_id in range(1_000_000, 100_000_000):
        base_id = str(raw_id).zfill(8)
        check_digit = calculate_check_digit(base_id)
        yield base_id + str(check_digit)


def perfect_portions() -> Generator[int, None, None]:
    number = 1
    while True:
        divisors = [div for div in range(1, number) if number % div == 0]
        if sum(divisors) == number:
            yield number
        number += 1


def extract_secret_messages(file_path: str) -> Generator[str, None, None]:
    pattern = re.compile(rb"[a-z]{5,}!", re.ASCII)
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            for match in pattern.findall(chunk):
                yield match.decode('ascii')


if __name__ == '__main__':
    print("Check digit for 12345678:", calculate_check_digit("12345678"))

    print("\nPerfect portions (first 5):")
    for count, value in enumerate(perfect_portions()):
        print(value)
        if count == 4:
            break

    print("\nFirst 5 Israeli IDs:")
    for count, identity in enumerate(all_israeli_ids()):
        print(identity)
        if count == 4:
            break

    print("\nSecret messages from logo.jpg:")
    path = os.path.join("resources", "logo.jpg")
    if os.path.exists(path):
        for message in extract_secret_messages(path):
            print(message)
