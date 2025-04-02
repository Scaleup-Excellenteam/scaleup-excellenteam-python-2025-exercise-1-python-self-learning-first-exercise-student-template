def group_by(function , iterable):
    dictionary = {function(key) : [item for item in iterable if function(key)==function(item)] for key in iterable}
    return dictionary
if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))