import os

def find_deep_files(directory):
    
    return [
        os.path.join(directory, f) 
        for f in os.listdir(directory) 
        if f.startswith("deep") and os.path.isfile(os.path.join(directory, f))
    ]

directory_path = "C:/Users/farha/Notebooks/content/week05/images"

if __name__ == '__main__':
    print(find_deep_files(directory_path))