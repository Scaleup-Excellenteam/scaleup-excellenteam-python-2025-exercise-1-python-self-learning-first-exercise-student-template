import re

"""Read the file and extract each message by the pattern [a-z]{5,}!"""
def parsle_tongue(path="logo.jpg"):
    with open(path, "rb") as logo:
        while True:
            tokens = logo.read(1024)
            if not tokens:
                break
            encrypted = re.findall(b'[a-z]{5,}!', tokens)

            for token in encrypted:
                yield token[:-1].decode()

def main() -> None:

    root = '../exelentim/exercise-1-python-self-learning-Lotem604/content/week05/resources/logo.jpg'
    for element in parsle_tongue(root):
        print(element)

if __name__ == '__main__':
    main()