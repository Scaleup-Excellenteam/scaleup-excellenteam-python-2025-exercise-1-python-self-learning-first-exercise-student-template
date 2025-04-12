import time
import sys
import io


def change_output_chaneel():
    """
    At This Function Will Change The Standrt Output Chaneel, Well Use It If Well Calcaute The Time Of Print Function's.
    """
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    return old_stdout


def running_2000(function, *paramters, **kwargs):
    """
    At This Function Will Calcuate The Run Time Of Given Function.
    """

    # Change The Standrt Output, For Example If Function Is 'Print' Nothing Will Be Printed To The Standrt Output.
    old_stdout = change_output_chaneel()

    start_time = time.time()
    function(*paramters, **kwargs)
    end_time = time.time()

    # Return The Output To The Standrt Output.
    sys.stdout = old_stdout

    delta = (end_time - start_time)
    return delta


def main():
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main()
