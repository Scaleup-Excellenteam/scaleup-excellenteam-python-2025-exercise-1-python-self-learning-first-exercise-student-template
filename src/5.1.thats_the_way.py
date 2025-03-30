
import os

START = "deep"
def thats_the_way(directory_path):
    """
    return a list of all files name that start with "deep" in the directory_path
    """
    try:
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path,f)) and f.startswith(START)]
    except FileNotFoundError:
        print("Error: no such directory")
        return None
    except PermissionError:
        print("Error: permission denied")
        return None

if __name__ == "__main__":
    print(thats_the_way(os.getcwd()))