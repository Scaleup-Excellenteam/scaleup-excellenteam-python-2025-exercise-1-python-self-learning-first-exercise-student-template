
def group_by(func,iter1):
    """
        Groups elements in an iterable based on the result of applying a function to each element.

        Parameters:
        func (function): A function that will be applied to each element in the iterable.
        iter (iterable): The iterable containing the elements to group.

        Returns:
        None: This function prints a dictionary where keys are the results of applying `func` to elements,
        and values are lists of elements that have the same result.
        """

    new_dic={func(word):[mila for mila in iter1 if func(word)==func(mila)] for word in iter1}
    return new_dic

def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == "__main__":
    main()