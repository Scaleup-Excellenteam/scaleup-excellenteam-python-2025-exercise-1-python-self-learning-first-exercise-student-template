def my_format(text, **kwargs):
    for key, value in kwargs.items():
        text = text.replace(f"{{{key}}}", str(value))
    return text


if __name__ == '__main__':
    print(my_format("I'm Mr. {name}, look at me!", name="Meeseeks"))
    print(my_format("{a} {b} {c} {c}", a="wubba", b="lubba", c="dub"))
    print(my_format("The universe is basically an animal", animal="Chicken"))
    print(my_format("The universe is basically an animal"))
