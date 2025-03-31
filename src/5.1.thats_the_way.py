import os
def thats_the_way(dir):
    """
       Lists all files in the specified directory whose names start with "deep".

       Parameters:
       dir (str): The path to the directory to search for files.

       Returns:
       list: A list of file names that start with "deep".
       """

    try:
        lst =[]
        fold=os.listdir(dir) # Get a list of all files in the directory
        for f in fold:
            if f.startswith("deep"):  # Check if the file name starts with "deep"
                lst.append(f)
        return lst

    except FileNotFoundError:
        print("File not found")







if __name__ == "__main__":
    thats_the_way("")
