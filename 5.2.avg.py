def avg(*numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    print(avg(5, 6))         # 5.5
    print(avg(10, 5, 3))     # 6
    print(avg(2))            # 2
    print(avg())             # None
